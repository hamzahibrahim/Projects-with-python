from tkinter import *

def convert_from_dollar_to_jd():
    in_dollar = float(In_Dollar.get())
    in_dollar = round(in_dollar, 3)
    list_1.delete(0, END)
    in_jd = in_dollar * .71
    list_1.insert(END, in_jd)

def convert_from_jd_to_dollar():
    in_jd = float(In_JD.get())
    in_dollar = round(in_jd, 3)
    list_2.delete(0, END)
    in_dollar = in_jd * 1.41
    list_2.insert(END, in_dollar)

#========================
win = Tk()
win.configure(bg='blue')
win.wm_title('Currency Converter')
l1 = Label(win, width=14, text='From Dollar to JD', bg='blue')
l1.grid(row=0, column=0)
l2 = Label(win, width=14, text='From JD to Dollar', bg='blue')
l2.grid(row=1, column=0)
In_Dollar = StringVar()
e1 = Entry(win, width=20, textvariable=In_Dollar)
e1.grid(row=0, column=1)
In_JD = StringVar()
e2 = Entry(win, width=20, textvariable=In_JD)
e2.grid(row=1, column=1)
b1 = Button(win, text='Convert', width=10, pady=1,
            bg='green', command=convert_from_dollar_to_jd)
b1.grid(row=0, column=3)
b2 = Button(win, text='Convert', width=10, pady=1,
            bg='green', command=convert_from_jd_to_dollar)
b2.grid(row=1, column=3)
list_1 = Listbox(win, height=1, width=20)
list_1.grid(row=0, column=4)
list_2 = Listbox(win, height=1, width=20)
list_2.grid(row=1, column=4)

b3 = Button(win, text='Exit', width=15,
             bg='sky blue', command=win.destroy)
b3.grid(row=2, column=4)
win.mainloop()
