# Tools and utils for the app.

def normalize_name(name: str) -> str:
    name = name.lower()

    name = name.replace('é', 'e').replace('è', 'e').replace('ê', 'e')
    name = name.replace('ç', 'c').replace('à', 'a')
    return name




