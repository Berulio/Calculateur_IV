# GUI for calculator.

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QLineEdit, QGridLayout, QComboBox, QSpinBox
from PySide6.QtGui import QIntValidator
import definitions as df
import Nature
import calculation as calc

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculateur d'IV")
        self.layoutization()

    def get_stats(self):
        return df.PokemonStats(
                hp=int(self.stat_hp.text()),
                atk=int(self.stat_atk.text()),
                dfs=int(self.stat_def.text()),
                spatk=int(self.stat_spatk.text()),
                spdef=int(self.stat_spdef.text()),
                spd=int(self.stat_spd.text())
            )
    
    def disp(self):
        print(self.lvlbox.text(),
              self.selector.currentText(),
              self.stat_hp.text())

    def setup_stats_grid(self):
        grid = QGridLayout()

        self.stat_hp    = QLineEdit()
        self.stat_atk   = QLineEdit()
        self.stat_def   = QLineEdit()
        self.stat_spatk = QLineEdit()
        self.stat_spdef = QLineEdit()
        self.stat_spd   = QLineEdit()

        self.stat_hp.setPlaceholderText("HP: 0")
        self.stat_atk.setPlaceholderText("Atk: 0")
        self.stat_def.setPlaceholderText("Def: 0")
        self.stat_spatk.setPlaceholderText("SpAtk: 0")
        self.stat_spdef.setPlaceholderText("SpDef: 0")
        self.stat_spd.setPlaceholderText("Spd: 0")

        # Check if the stats entered are integers within a normal stats range.
        chkstat = QIntValidator(0, 999, self)
        self.stat_hp.setValidator(chkstat),
        self.stat_atk.setValidator(chkstat),
        self.stat_def.setValidator(chkstat),
        self.stat_spatk.setValidator(chkstat),
        self.stat_spdef.setValidator(chkstat),
        self.stat_spd.setValidator(chkstat)

        # addWidget(widget, ligne, colonne)
        # Ligne 0
        grid.addWidget(self.stat_hp,    0, 0)
        grid.addWidget(self.stat_atk,   0, 1)
        
        # Ligne 1
        grid.addWidget(self.stat_def,   1, 0)
        grid.addWidget(self.stat_spatk, 1, 1)
        
        # Ligne 2
        grid.addWidget(self.stat_spdef, 2, 0)
        grid.addWidget(self.stat_spd,   2, 1)

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
    
    def layoutization(self):
        # Layout 0: Text saying anything
        l0 = QVBoxLayout()
        self.blabla = QLabel("Entrez les stats de votre pokémon à évaluer...")
        l0.addWidget(self.blabla)

        # Layout 1: Analyzed pokemon stats
        l1 = QVBoxLayout()
        grid = self.setup_stats_grid()
        l1.addWidget(self.setup_level_box())
        l1.addWidget(self.setup_nature_selector())
        l1.addLayout(grid)

        # layout 2: button to process the stats entered. Basically saying "Hey I'm done entering the stats!"
        l2 = QVBoxLayout()
        button = QPushButton("Calculer! :D")
        button.clicked.connect(self.submain)
        l2.addWidget(button)

        l3 = QHBoxLayout()
        btn = QPushButton("Voir les stats!")
        btn.clicked.connect(self.disp)
        l3.addWidget(btn)

        # Master layout
        ml = QVBoxLayout()
        ml.addLayout(l0)
        ml.addLayout(l1)
        ml.addLayout(l2)
        ml.addLayout(l3)

        # master container
        mc = QWidget()
        mc.setLayout(ml)

        self.setCentralWidget(mc)
        self.show()
    
    def submain(self):
        db = calc.db_init()
        lvl = self.lvlbox.value()
        nature = self.selector.currentText()
        calc.calc_IV(calc.get_base_stat(db, "Carapuce"),self.get_stats(),lvl,nature)


def main():
    app = QApplication([])
    window = MainWindow()
    app.exec()

if __name__ == "__main__":
    sys.exit(main())