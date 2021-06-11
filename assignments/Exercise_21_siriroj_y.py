from tkinter import *
import math

def left_click(event) :
    your_body()

def your_body() :
    bmi = float(text_box_weight.get())/math.pow(float(text_box_height.get())/100,2)
    if bmi < 18.5 :
        your_bmi = "you too slim"
    elif bmi <= 22.9:
        your_bmi = "your bmi is standard"
    elif bmi <= 24.9:
        your_bmi = "you starting to get fat"
    elif bmi <= 29.9:
        your_bmi = "you fat"
    elif bmi > 30:
        your_bmi = "you too fat"
    label_bmi.configure(text = your_bmi)

main_window = Tk()
label_height = Label(main_window,text='Height(CM)')
label_height.grid(row=1,column=1)
text_box_height = Entry(main_window)
text_box_height.grid(row=1,column=2)
label_weight = Label(main_window,text='Weight(Kg)')
label_weight.grid(row=2,column=1)
text_box_weight = Entry(main_window)
text_box_weight.grid(row=2,column=2)
calculate_bmi = Button(main_window,text='Cal.BMI')
calculate_bmi.grid(row=3,column=1)
calculate_bmi.bind('<Button-1>',left_click)
label_bmi = Label(main_window,text='your BMI')
label_bmi.grid(row=3,column=2)
main_window.mainloop()