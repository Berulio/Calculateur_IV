# GUI for calculator.

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QLineEdit, QGridLayout, QComboBox, QSpinBox
from PySide6.QtGui import QIntValidator
import definitions as df
import Nature
import calculation as calc
import sqlite3 as sql
import toolz

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.pkmn_stats = df.PokemonStats()
        self.pkmn_ivs = df.PokemonIVs()

        # inputs
        self.stat_hp_input = QLineEdit()
        self.stat_atk_input = QLineEdit()
        self.stat_def_input = QLineEdit()
        self.stat_spatk_input = QLineEdit()
        self.stat_spdef_input = QLineEdit()
        self.stat_spd_input = QLineEdit()

        # output
        self.iv_hp_output = None
        self.iv_atk_output = None
        self.iv_def_output = None
        self.iv_spatk_output = None
        self.iv_spdef_output = None
        self.iv_spd_output = None

        # do stuff
        self.setWindowTitle("Calculateur d'IV")
        self.layoutization()

    def get_stats_input(self):
        return df.PokemonStats(
                hp=int(self.stat_hp_input.text()),
                atk=int(self.stat_atk_input.text()),
                dfs=int(self.stat_def_input.text()),
                spatk=int(self.stat_spatk_input.text()),
                spdef=int(self.stat_spdef_input.text()),
                spd=int(self.stat_spd_input.text())
            )

    def setup_stats_grid(self):
        grid = QGridLayout()

        self.stat_hp_input.setPlaceholderText("HP: 0")
        self.stat_atk_input.setPlaceholderText("Atk: 0")
        self.stat_def_input.setPlaceholderText("Def: 0")
        self.stat_spatk_input.setPlaceholderText("SpAtk: 0")
        self.stat_spdef_input.setPlaceholderText("SpDef: 0")
        self.stat_spd_input.setPlaceholderText("Spd: 0")

        # Check if the stats entered are integers within a normal stats range.
        chkstat = QIntValidator(0, 999, self)
        self.stat_hp_input.setValidator(chkstat),
        self.stat_atk_input.setValidator(chkstat),
        self.stat_def_input.setValidator(chkstat),
        self.stat_spatk_input.setValidator(chkstat),
        self.stat_spdef_input.setValidator(chkstat),
        self.stat_spd_input.setValidator(chkstat)

        # addWidget(widget, ligne, colonne)
        grid.addWidget(self.stat_hp_input,    0, 0)
        grid.addWidget(self.stat_atk_input,   1, 0)
        grid.addWidget(self.stat_def_input,   2, 0)
        grid.addWidget(self.stat_spatk_input, 3, 0)
        grid.addWidget(self.stat_spdef_input, 4, 0)
        grid.addWidget(self.stat_spd_input,   5, 0)

        return grid
    
    def setup_nature_selector(self):
        self.selector = QComboBox()
        self.selector.addItems(Nature.NATURE.keys())

        # set default nature to a neutral one (one that has no stat modifiers)
        self.selector.setCurrentText("Bizarre")
        
        return self.selector
    
    def setup_level_box(self):
        self.lvlbox = QSpinBox()
        self.lvlbox.setRange(1, 100)
        self.lvlbox.setPrefix("Niveau : ")

        return self.lvlbox
    
    def setup_name_box(self):
        self.namebox = QComboBox()
        
        try:
            db = sql.connect(df.DATA_DIR/df.DB_NAME)
            cursor = db.cursor()

            cursor.execute("SELECT nom FROM pkmn_table ORDER BY nom ASC")
            namelist = [item[0] for item in cursor.fetchall()]
            print(namelist[1])
            namelist.sort(key=toolz.normalize_name)
            self.namebox.addItems(namelist)
            db.close()
        except Exception as e:
            print(f"Erreur lors du chargement de la base de données: {e}")

        # set default name to the first one on the list
        self.namebox.setCurrentIndex(0)

        return self.namebox
    
    def setup_eval_table(self):
        grid = QGridLayout()

        iv_hp_label    = QLabel("pv")
        iv_atk_label   = QLabel("atk")
        iv_def_label   = QLabel("def")
        iv_spatk_label = QLabel("atk.spe")
        iv_spdef_label = QLabel("def.spe")
        iv_spd_label   = QLabel("vit")

        self.iv_hp_output = QLabel(f"{self.pkmn_ivs.hp_low}~{self.pkmn_ivs.hp_high}")
        self.iv_atk_output = QLabel(f"{self.pkmn_ivs.atk_low}~{self.pkmn_ivs.atk_high}")
        self.iv_def_output = QLabel(f"{self.pkmn_ivs.dfs_low}~{self.pkmn_ivs.dfs_high}")
        self.iv_spatk_output = QLabel(f"{self.pkmn_ivs.spatk_low}~{self.pkmn_ivs.spatk_high}")
        self.iv_spdef_output = QLabel(f"{self.pkmn_ivs.spdef_low}~{self.pkmn_ivs.spdef_high}")
        self.iv_spd_output = QLabel(f"{self.pkmn_ivs.spd_low}~{self.pkmn_ivs.spd_high}")

        # addWidget(widget, ligne, colonne)
        grid.addWidget(iv_hp_label,          0, 0)
        grid.addWidget(self.iv_hp_output,    0, 1)
        print(f"ID au moment de l'ajout au layout : {id(self.iv_hp_output)}")

        grid.addWidget(iv_atk_label,         1, 0)
        grid.addWidget(self.iv_atk_output,   1, 1)

        grid.addWidget(iv_def_label,         2, 0)
        grid.addWidget(self.iv_def_output,   2, 1)

        grid.addWidget(iv_spatk_label,       3, 0)
        grid.addWidget(self.iv_spatk_output, 3, 1)

        grid.addWidget(iv_spdef_label,       4, 0)
        grid.addWidget(self.iv_spdef_output, 4, 1)

        grid.addWidget(iv_spd_label,         5, 0)
        grid.addWidget(self.iv_spd_output,   5, 1)

        return grid

    def layoutization(self):
        # Layout 0: Text saying anything
        l0 = QVBoxLayout()
        blabla = QLabel("Entrez les stats de votre pokémon à évaluer...")
        l0.addWidget(blabla)

        # Layout 1: Analyzed pokemon stats
        l1 = QVBoxLayout()
        l1.addWidget(self.setup_name_box())
        l1.addWidget(self.setup_level_box())
        l1.addWidget(self.setup_nature_selector())
        
        l2 = QHBoxLayout()
        grid = self.setup_stats_grid()
        self.iv_eval_grid = self.setup_eval_table()
        l2.addLayout(grid)
        l2.addLayout(self.iv_eval_grid)

        # layout 2: button to process the stats entered. Basically saying "Hey I'm done entering the stats!"
        l3 = QVBoxLayout()
        button = QPushButton("Calculer! :D")
        button.clicked.connect(self.submain)
        l3.addWidget(button)

        # Master layout
        ml = QVBoxLayout()
        ml.addLayout(l0)
        ml.addLayout(l1)
        ml.addLayout(l2)
        ml.addLayout(l3)
        # ml.addLayout(l4)

        # master container
        mc = QWidget()
        mc.setLayout(ml)

        self.setCentralWidget(mc)
        self.show()

    def update_display(self):
        self.iv_hp_output.setText(f"{self.pkmn_ivs.hp_low}~{self.pkmn_ivs.hp_high}")
        self.iv_atk_output.setText(f"{self.pkmn_ivs.atk_low}~{self.pkmn_ivs.atk_high}")
        self.iv_def_output.setText(f"{self.pkmn_ivs.dfs_low}~{self.pkmn_ivs.dfs_high}")
        self.iv_spatk_output.setText(f"{self.pkmn_ivs.spatk_low}~{self.pkmn_ivs.spatk_high}")
        self.iv_spdef_output.setText(f"{self.pkmn_ivs.spdef_low}~{self.pkmn_ivs.spdef_high}")
        self.iv_spd_output.setText(f"{self.pkmn_ivs.spd_low}~{self.pkmn_ivs.spd_high}")

    
    def submain(self):
        db = calc.db_init()
        lvl = self.lvlbox.value()
        nature = self.selector.currentText()
        self.pkmn_ivs = calc.calc_IV(calc.get_base_stat(db, self.namebox.currentText()),self.get_stats_input(),lvl,nature)
        self.update_display()
        print(f"ID au moment du calcul : {id(self.iv_hp_output)}")
        print(self.pkmn_ivs)


def main():
    app = QApplication([])
    window = MainWindow()
    app.exec()

if __name__ == "__main__":
    sys.exit(main())