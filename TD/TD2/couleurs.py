import tkinter as tk
from random import randint


CANVAS_WIDTH, CANVAS_HEIGHT = 256, 256


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

root = tk.Tk()
root.title("Couleurs")

cnvs = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black")

def draw_pixel(i, j, color):
    cnvs.create_rectangle(i, j, i+1, j+1, width=0, fill=color)

def ecran_aleatoire():
    for i in range(CANVAS_WIDTH):
        for j in range(CANVAS_HEIGHT):
            draw_pixel(i, j, get_color(randint(0, 255), randint(0, 255), randint(0, 255)))

def degrade_gris():
    for i in range(CANVAS_WIDTH):
        for j in range(CANVAS_HEIGHT):
            draw_pixel(i, j, get_color(i, i, i))

def degrade_2D():
    for i in range(CANVAS_WIDTH):
        for j in range(CANVAS_HEIGHT):
            draw_pixel(i, j, get_color(i, 0, j))

btn_aleatoire = tk.Button(root, text="Aléatoire", fg="blue", bg="white", command=ecran_aleatoire)
btn_grey = tk.Button(root, text="Dégradé gris", fg="blue", bg="white", command=degrade_gris)
btn_2D = tk.Button(root, text="Dégradé 2D", fg="blue", bg="white", command=degrade_2D)

btn_aleatoire.grid(row=0, column=0)
btn_grey.grid(row=1, column=0)
btn_2D.grid(row=2, column=0)

cnvs.grid(row=0, column=1, rowspan=3)

root.mainloop()