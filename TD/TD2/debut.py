import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400 #def de la taille du canvas

root = tk.Tk()  #création de la win principale

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT) #création du canvas

# Début de votre code
x = CANVAS_WIDTH / 2

y1 = 51
y2 = CANVAS_HEIGHT -50

canvas.create_line(x, y1, x, y2)

canvas.create_oval(x - 50, y1 + 50, x + 50, y1 - 50)

canvas.create_oval(x - 50, y2 + 50, x + 50, y2 - 50)
canvas.create_oval(x - 50, (y1+y2)/2 + 50, x + 50, (y1+y2)/2 - 50)

# Fin de votre code

canvas.grid(row=0, column=0)
root.mainloop()