# Import stuff
import tkinter
from random import randint
# Code
window = tkinter.Tk()


def new_num():
    result_label.delete(0, 10)
    result_label.insert(1, str(randint(int(start_entry.get()), int(end_entry.get()))))
    result_label.update()


# Create components
start_label = tkinter.Label(window, text='Start number')
start_entry = tkinter.Entry(window)
end_label = tkinter.Label(window, text='End number')
end_entry = tkinter.Entry(window)
new_number_button = tkinter.Button(window, text='New number', command=new_num)
result_lbl = tkinter.Label(window, text='Current number')
result_label = tkinter.Entry(window)
# place components
for i in range(4):
    window.columnconfigure(i, pad=15)
    window.rowconfigure(i, pad=10)
"""
start_label.grid(row=1, column=1)
start_entry.grid(row=1, column=2)
end_label.grid(row=2, column=1)
end_entry.grid(row=2, column=2)
"""
# Show components
start_label.pack()
start_entry.pack()
end_label.pack()
end_entry.pack()
new_number_button.pack()
result_lbl.pack()
result_label.pack()
window.mainloop()
