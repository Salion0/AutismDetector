import tkinter as tk

var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
array = [var2, var3]


def get_value():
    print("Value: " + var1.get())
    for var in array:
        print("Value:" + var.get())


def make_window():
    root = tk.Tk()

    entry = tk.Entry(master=root, textvariable=var2)
    entry.pack()
    for i in range(0, 2):
        rd_bttn = tk.Radiobutton(master=root, variable=array[i], value="1")
        rd_bttn.pack()

    bttn = tk.Button(master=root, text="Prova", command=get_value)
    bttn.grid(row=1)
    root.mainloop()





