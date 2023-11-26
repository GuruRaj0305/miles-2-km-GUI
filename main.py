from tkinter import *

window = Tk()
window.title("Miles to KiloMeter Converter")
window.config(padx=40, pady=40)

def m_to_km():
    miles = float(miles_input.get())
    km = miles * 1.689
    km_value.config(text=f"{km}")

miles_input = Entry(width=7)
miles_input.place(x=20 ,y=0)

label = Label(text="Miles")
label.place(x=50 ,y=0)

lable_eq = Label(text="-->")
lable_eq.place(x=0 ,y=30)

km_value = Label(text="0")
km_value.place(x=20 ,y=30)

km_lable=Label(text="KiloMeters")
km_lable.place(x=50 ,y=30)

calculate_button = Button(text="Calculate", command=m_to_km)
calculate_button.place(x=30 ,y=100)


window.mainloop()