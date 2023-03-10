DATABASE = './db/movies.sqlite'

DNA_CONVERT_RULES = {
    "A": {
        "A": [[["C", "T"], "N"], [["A", "G"], "K"]],
        "C": [[["C", "T", "A", "G"], "T"]],
        "G": [[["C", "T"], "S"], [["A", "G"], "R"]],
        "T": [[["C", "T", "A"], "I"], [["G"], "M"]]
    },
    "C": {
        "A": [[["C", "T"], "H"], [["A", "G"], "Q"]],
        "C": [[["C", "T", "A", "G"], "P"]],
        "G": [[["C", "T", "A", "G"], "R"]],
        "T": [[["C", "T", "A", "G"], "L"]]
    },
    "G": {
        "A": [[["C", "T"], "D"], [["A", "G"], "E"]],
        "C": [[["C", "T", "A", "G"], "A"]],
        "G": [[["C", "T", "A", "G"], "G"]],
        "T": [[["C", "T", "A", "G"], "V"]]
    },
    "T": {
        "A": [[["C", "T"], "Y"], [["A", "G"], "U"]],
        "C": [[["C", "T", "A", "G"], "S"]],
        "G": [[["C", "T"], "C"], [["A"], "U"], [["G"], "W"]],
        "T": [[["C", "T"], "F"], [["A", "G"], "L"]],
    }
}

DNA_CONVERT_OFFSET = 0
