"""
print("Két beolvasott egész számról állapítjuki meg, hogy melyik a nagyobb.")
nums = int(input("Adj meg egy egész számot: ")), int(input("Adj meg egy egész számot: "))
if nums[0] == nums[1]:
    print("A két szám egyenlő.")
else:
    print(max(nums))
"""
import tkinter


def feldolgoz():
    nums = int(input_box1.get()), int(input_box2.get())
    if nums[0] == nums[1]:
        text = "A két szám egyenlő."
    else:
        text = str(max(nums))
    result = tkinter.Label(window, text=text)
    result.pack()


window = tkinter.Tk()
window.title('01-02')
feladat = tkinter.Label(window, text="Két beolvasott egész számról állapítjuki meg, hogy melyik a nagyobb.")
input_box1 = tkinter.Entry(window)
input_box2 = tkinter.Entry(window)
button = tkinter.Button(window, text="Feldolgozás", command=feldolgoz)
feladat.pack()
input_box1.pack()
input_box2.pack()
button.pack()
window.mainloop()
