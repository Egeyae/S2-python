import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 800

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

btn_color = tk.Button(root, text="Choisir une couleur", relief=tk.FLAT, bg="floralwhite")

btn_circle = tk.Button(root, text="Cercle", relief=tk.FLAT, bg="floralwhite", fg="deepskyblue1")
btn_square = tk.Button(root, text="Carré", relief=tk.FLAT, bg="floralwhite", fg="firebrick1")
btn_cross = tk.Button(root, text="Croix", relief=tk.FLAT, bg="floralwhite", fg="gold1")

cnvs = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black", \
    borderwidth=10, relief=tk.RIDGE)


btn_color.grid(row=0, column=1)

btn_circle.grid(row=1, column=0)
btn_square.grid(row=2, column=0)
btn_cross.grid(row=3, column=0)

cnvs.grid(row=1, column=1, rowspan=3)

root.mainloop()
