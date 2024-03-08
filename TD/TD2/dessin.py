import tkinter as tk
from random import randint

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 800
BORDERWIDTH = 10
CIRCLE_SIZE = 50
POSS_COLOR = ["blue", "white", "black", "green", "cyan", "yellow"]

"""
RELIEF STYLES:
    FLAT
    RAISED
    SUNKEN
    GROOVE
    RIDGE
"""

root = tk.Tk()
root.title("Mon dessin")

cnvs = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black", \
    borderwidth=BORDERWIDTH, relief=tk.RIDGE)

def draw_circle():
    """
    dessin d'un cercle de 2*CIRCLE_SIZE de diamètre (ici 100), choix de x et y aléatoire dans les limites possibles
    offset de 1 pour éviter de dépasser
    + BORDERWIDTH => jsp pas trop, ms sans on atteint pas la border
    """
    x, y = randint(BORDERWIDTH+1, CANVAS_WIDTH-CIRCLE_SIZE*2+BORDERWIDTH-1),  randint(BORDERWIDTH+1, CANVAS_HEIGHT-CIRCLE_SIZE*2+BORDERWIDTH-1)

    cnvs.create_oval(x, y, x+CIRCLE_SIZE*2, y+CIRCLE_SIZE*2, fill=POSS_COLOR[0])

def draw_square():
    """
    dessin d'un carré de côté 2*CIRCLE_SIZE (ici 100)
    choix de x et y aléatoire
    + BORDERWIDTH => same as draw_circle()
    """
    x, y = randint(BORDERWIDTH+1, CANVAS_WIDTH-(2*CIRCLE_SIZE)+BORDERWIDTH-1),  randint(BORDERWIDTH+1, CANVAS_HEIGHT-(2*CIRCLE_SIZE)+BORDERWIDTH-1)

    cnvs.create_rectangle(x, y, x+(2*CIRCLE_SIZE), y+(2*CIRCLE_SIZE), fill=POSS_COLOR[0])

def draw_cross():
    """
    dessin d'une croix inscrite dans un carré comme précédemment, épaisseur = 20px
    choix de x, y aléatoire
    """
    x, y = randint(BORDERWIDTH+1, CANVAS_WIDTH-(2*CIRCLE_SIZE)+BORDERWIDTH-1),  randint(BORDERWIDTH+1, CANVAS_HEIGHT-(2*CIRCLE_SIZE)+BORDERWIDTH-1)

    cnvs.create_rectangle(x+CIRCLE_SIZE-10, y, x+CIRCLE_SIZE+10, y+(2*CIRCLE_SIZE), fill=POSS_COLOR[0])
    cnvs.create_rectangle(x, y+CIRCLE_SIZE-10, x+(2*CIRCLE_SIZE), y+CIRCLE_SIZE+10, fill=POSS_COLOR[0])

def choose_color():
    print("Please choose a color from the following list: ")
    for c in range(len(POSS_COLOR)):
        print(f"\t{c} - {POSS_COLOR[c]}")
    user_input = input("Your choice: ")
    if not user_input in [str(x) for x in range(len(POSS_COLOR))]:
        print("Invalid choice")
        return
    user_input = int(user_input)
    POSS_COLOR[0], POSS_COLOR[user_input] = POSS_COLOR[user_input], POSS_COLOR[0]
    print("OK")
    
btn_color = tk.Button(root, text="Choisir une couleur", relief=tk.FLAT, bg="floralwhite", command=choose_color)

btn_circle = tk.Button(root, text="Cercle", relief=tk.FLAT, bg="floralwhite", fg="deepskyblue1", command=draw_circle)
btn_square = tk.Button(root, text="Carré", relief=tk.FLAT, bg="floralwhite", fg="firebrick1", command=draw_square)
btn_cross = tk.Button(root, text="Croix", relief=tk.FLAT, bg="floralwhite", fg="gold1", command=draw_cross)


btn_color.grid(row=0, column=1, padx=3, pady=(13,3))

btn_circle.grid(row=1, column=0, padx=(13,3), pady=3)
btn_square.grid(row=2, column=0, padx=(13,3), pady=3)
btn_cross.grid(row=3, column=0, padx=(13,3), pady=3)

cnvs.grid(row=1, column=1, rowspan=3, padx=10, pady=10)

root.mainloop()
