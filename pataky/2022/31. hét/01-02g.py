import tkinter as tk


def nagyobb():
    output.delete(0, tk.END)
    nums = szam1.get(), szam2.get()
    szam1.delete(0, tk.END)
    szam2.delete(0, tk.END)
    if nums[0] == nums[1]:
        output.insert(0, "A kér szám egyenlő.")
    else:
        output.insert(0, str(max(nums)))


window = tk.Tk()
window.title('01-02')
txt = tk.Label(window, text='Adj meg két számot')
szam1 = tk.Entry(window)
szam2 = tk.Entry(window)
output = tk.Entry(window)
button = tk.Button(window, text='Melyik nagyobb?', command=nagyobb)
txt.pack()
szam1.pack()
szam2.pack()
button.pack()
output.pack()
window.mainloop()
