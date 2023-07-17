import tkinter

window = tkinter.Tk()
window.title("Km to miles Converter")
window.config(padx=40, pady=20)


def km_to_mile():
    km = float(km_input.get())
    miles = km * 0.621371
    value_miles['text'] = f'{round(miles, 2)}'


km_input = tkinter.Entry(width=10)
km_input.grid(column=1, row=0)

Km = tkinter.Label(text="Km")
Km.grid(column=2, row=0)

equal = tkinter.Label(text="Is : ")
equal.grid(column=0, row=1)

value_miles = tkinter.Label(text="0")
value_miles.grid(column=1, row=1)

miles_txt = tkinter.Label(text="Miles")
miles_txt.grid(column=2, row=1)

calculate = tkinter.Button(text="Calculate", command=km_to_mile)
calculate.grid(column=1, row=3)
window.mainloop()
