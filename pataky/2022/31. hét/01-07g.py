import tkinter as tk


def keres():
    output.delete(0, tk.END)
    szoveg = szam.get()
    szam.delete(0, tk.END)
    if 'a' in szoveg:
        output.insert(0, "A szöveg tartalmaz \'a\' betűt.")
    else:
        output.insert(0, 'A szöveg nem tartalmaz \'a\' betűt.')


window = tk.Tk()
window.title('01-07')
txt = tk.Label(window, text='Olvassunk be egy szöveget és írjuk ki, hogy van-e benne kis "a"-be')
szam = tk.Entry(window)
output = tk.Entry(window)
button = tk.Button(window, text='Van benne kis a?', command=keres)
txt.pack()
szam.pack()
button.pack()
output.pack()
window.mainloop()
