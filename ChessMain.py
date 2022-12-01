# 
# Tämä ohjaa GameState objektia ja ottaa vastaan pelaajan inputit
#

import pygame as p
#from Scripts import ChessEngine
from ChessEngine import GameState
from ChessEngine import Move
import sys

#sys.path.insert(0, GitHub_koodia/shakki_peli/Scripts/ChessEngine.py)
WIDTH = HEIGHT = 512    # pikseliä
DIMENSION = 8            # lauta on 8x8
SQ_SIZE = HEIGHT // DIMENSION  # koko lauta jaettuna 8 palaseen eli ruutuun
MAX_FPS = 15 # for animation
IMAGES = {}

# Alustetaan globaali kuva sanakirja. Ladataan vain kerran alussa, eikä esim joka vuoro

def loadImages():
    #IMAGES['wp'] = p.image.load("images/wp.png")  näin pitää tehä kaikille kerran niin miten tehdä vaikka loopilla
    pieces = ['wp', 'bp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bR', 'bN', 'bB', 'bQ', 'bK', ]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("piece_pictures/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    #Note Kuviin pääsee käsiksi 'IMAGES['wp']'

#
# Main Driver: Käsittelee inputit ja grafiikan
#
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    #gs = ChessEngine.GameState()
    gameState = GameState()
    moveFunction = Move()
    loadImages() # tee tämä vain kerran ettei kuvia ladata kokoajan, kun resurssi rankkaa
    running = True
    squareSelected = () # alustetaan hiiren valinta, aluksi tyhjä tuple eli (rivi, kolumni)
    playerClicks = [] # ylläpitää pelaajan painalluksia esim(kaksi tuplea: [(6,4), (4,4)])

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x,y) koordinaatit hiirelle
                column = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if squareSelected == (row, column): # chekki painaako pelaaja kahdesti samaa ruutua
                    squareSelected = ()  # poistaa painalluksen
                    playerClicks = [] # poistaa pelaajan painalluksen
                else:
                    squareSelected = (row, column)
                    playerClicks.append(squareSelected) # append ensimmäisen ja toisen painalluksen
                if len(playerClicks) == 2: # eli toinen painallus, eli liikkuminen
                    move = moveFunction(playerClicks[0], playerClicks[1], gameState.board)  
                    print(moveFunction.getChessNotation())
                    gameState.makeMove(move)  
                    squareSelected = () #resetoi pelaajan klikkaus
                    playerClicks = []

        drawGameState(screen, gameState)
        clock.tick(MAX_FPS)
        p.display.flip()

# Piirtää laudan grafiikat nykyisessä game statessa
def drawGameState(screen, gameState):
    drawBoard(screen) # piirtää neliöt laudalle
    drawPieces(screen, gameState.board) # piirtää hahmot laudalle
    #uusi funktio tulevaisuudessa mikä highlaittaa hahmot tai ehdottaa sallitut liikkumiset

# Piirtää neliöt laudalle
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Piirtää hahmot laudan päälle nykyisestä gameState.board:sta
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()

