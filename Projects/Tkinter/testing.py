import tkinter

window = tkinter.Tk()
window.title("My first GUI", )
window.minsize(600, 400)
window.maxsize(600, 400)
window.config(bg="black")

a_label = tkinter.Label(text="Welcome", font=("Comic Sans MS", 20, "bold"), fg="white", bg='black')
a_label.pack()


def button_clicked():
    typed = inputted.get()
    a_label['text'] = typed


button = tkinter.Button(text="Click Me", command=button_clicked, bg='black', fg="red")
button.pack()

inputted = tkinter.Entry(width=10, show='*')
inputted.pack()
window.mainloop()
