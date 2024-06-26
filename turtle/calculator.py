from tkinter import *


root = Tk()
root.title("Calculator")
root.geometry("280*380")
# root.resizable(0,0)
root.configure(background='black')


result_label = Label(root, text=0)

root.mainloop()