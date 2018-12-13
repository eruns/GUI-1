import tkinter as tk
# root = tk.Tk()
# ...
var = tk.StringVar()
button = tk.Button(root, text="Click Me", command=lambda: var.set('asdf'))
button.place(relx=.5, rely=.5, anchor="c")

print("waiting...")
button.wait_variable(var)
print(var)
print("done waiting.")

# class MyWindow(tk.Frame):
#     def __init__(self, parent):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Hello, world")
#         label.pack()
#         label.bind("<1>", self.quit)
#     def quit(self, event=None):
#         sys.exit()
#
# root = tk.Tk()
# MyWindow(root).pack()
# root.mainloop()