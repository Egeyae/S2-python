import tkinter as tk


COLORS = [
    "blue",
    "green",
    "black",
    "yellow",
    "magenta",
    "red"
]


root = tk.Tk()
root.title("Cible")

size = int(input("Canvas size: "))
nb_circles = int(input("Number of circles: ")) 

cnvs = tk.Canvas(root, width=size, height=size, bg="black")

step = size //2 // nb_circles

for i in range(nb_circles):
    z = step*i
    cnvs.create_oval(z, z, size-z, size-z, fill=COLORS[i%6], width=0)

cnvs.pack()
root.mainloop()