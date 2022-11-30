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
