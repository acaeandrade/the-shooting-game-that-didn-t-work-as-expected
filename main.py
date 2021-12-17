from tkinter import *
from tkinter.ttk import *

class MainGame():

    def __init__(self):
        root = Tk();
        root.title('T-Block');
        root.geometry('520x520');
        root.resizable(False, False)

        tab = Canvas(root, bg='white', height=500, width=500)
        playerBase = tab.create_rectangle(, fill='black');
        player = tab.create_bitmap(50, 50, bitmap='questhead');


        tab.pack()
        root.mainloop()

    def PlayerControl(self):
        pass

    def WallBlocks(self):
#Cria paredes padrões do tabuleiro
        pass

    def Ways(self):
        pass
#Função responsável por criar blocos de caminho para o jogador
MainGame();
