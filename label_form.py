import tkinter
from tkinter import ttk

form = tkinter.Tk()
form.title = "zino"
form.geometry("700x500")
lbl1 = ttk.Label( form, text = "label1" )
lbl2 = ttk.Label( form, text = "label2" )
lbl3 = ttk.Label( form, text = "label3" )

lbl1.pack()
lbl2.pack()
lbl3.pack()

form.mainloop()
