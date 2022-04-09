"""I hathe this."""
import tkinter
input_box = None
paratlanablak = None


def paratlanfeladat():
    global input_box, paratlanablak
    paratlanablak = tkinter.Toplevel(window)
    instrukcio = tkinter.Message(paratlanablak, text='Addj meg egy szamot es megmondom hogy paros-e')
    input_box = tkinter.Entry(paratlanablak)
    the_button = tkinter.Button(paratlanablak, text='ellenorzes', command=paratlan_check)
    instrukcio.pack()
    input_box.pack()
    the_button.pack()
    paratlanablak.mainloop()


def paratlan_check():
    global input_box, paratlanablak
    num = int(input_box.get())
    isparatlan = num % 2 == 1
    if isparatlan:
        rtxt = 'A szam paratlan.'
    else:
        rtxt = 'A szam paros.'
    eredmeny = tkinter.Label(paratlanablak, text=rtxt)
    eredmeny.pack()


def nagyobbdupla():
    nagyobbablak = tkinter.Toplevel(window)
    instrukcio = tkinter.Message(paratlanablak, text='Addj be ket szamot es kiadom a nagyobb dulajat.')
    input_box1 = tkinter.Entry(paratlanablak)
    the_button = tkinter.Button(paratlanablak, text='szamol')
    instrukcio.pack()
    input_box1.pack()
    the_button.pack()
    nagyobbablak.mainloop()


window = tkinter.Tk()
window.title('Fuggvenyes feladatok')
paratlan = tkinter.Button(window, text='03-01', command=paratlanfeladat)
dupla = tkinter.Button(window, text='03-02', command=nagyobbdupla)
paratlan.grid(row=1, column=1)
dupla.grid(row=1, column=2)
window.mainloop()
