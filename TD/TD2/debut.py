import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400 #def de la taille du canvas

root = tk.Tk()  #création de la win principale

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT) #création du canvas

# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100

y1 = CANVAS_HEIGHT - 100
y2 = CANVAS_HEIGHT / 2
canvas.create_line(x0, y1, x0, y2)
canvas.create_oval(x0 - 50, y2 + 50, x0 + 50, y2 - 50)
canvas.create_oval(x1 - 50, y2 + 50, x1 + 50, y2 - 50)
canvas.create_oval((x0 + x1) / 2 - 50, y2 + 50, (x0 + x1) / 2 + 50, y2 - 50)

# Fin de votre code

canvas.grid(row=0, column=0)
root.mainloop()