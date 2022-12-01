#
# Tämä tallentaa peli-tilanteen. Tämä myös tarkistaa validit liikkeet nykyisessä lauta-tilanteessa. 
# Myös ylläpitää liikumishistorian.
#

class GameState():
    def __init__(self):
        # lauta on 8x8 2d lista. Joka listassa on kaksi merkkiä.
        # ensimmäinen kirjain on väri ja toinen palasen tyyppi 'K', 'Q', 'R', 'B', 'N', 'p'
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"], # mustien palaset
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"], #bp = black piece
            ["--", "--", "--", "--", "--", "--", "--", "--"], # tyhjä rivi, (--) koska kaksi merkkiä kuten palasillakin
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"], 
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"], # wp = white piece
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]  # valkoisten palaset 
        ]
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        self.board[move.startRow][move.startColumn] = "--"
        self.board[move.endRow][move.endColumn] = move.pieceMoved
        self.moveLog.append(move) #tallentaa siirron logiin
        self.whiteToMove = not self.whiteToMove # vuoron vaihto mustalle

class Move():
    # mäppää "key" "valueen"
    # key : value
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4":4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()} # tää muuntaa ranksToRows takaisin, eli jos on 3 niin tulee 3: "5"
    filesToColumns = {"h": 7, "g": 6, "f": 5, "e":4, "d": 3, "c": 2, "b": 1, "a": 0}
    columnsToFiles = {v: k for k, v in filesToColumns.items()} #sama kun yllä mutta kolumneille

    def __init__(self, startSquare, endSquare, board):
        self.startRow = startSquare[0]
        self.startColumn = startSquare[1]
        self.endRow = endSquare[0]
        self.endColumn = endSquare[1]
        self.pieceMoved = board[self.startRow][self.startColumn]
        self.pieceCaptured = board[self.endRow][self.endColumn]

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startColumn) + self.getRankFile(self.endRow, self.endColumn)

    def getRankFile(self, row, column):
        return self.columnsToFiles[column] + self.rowsToRanks[row]

