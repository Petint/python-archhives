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
    result.grid(row=2, column=2)


window = tkinter.Tk()
window.title('01-02 Két beolvasott egész számról állapítjuki meg, hogy melyik a nagyobb.')

input_box1 = tkinter.Entry(window)
input_box2 = tkinter.Entry(window)
button = tkinter.Button(window, text="Feldolgozás", command=feldolgoz)
for i in range(4):
    window.columnconfigure(i, pad=15)
    window.rowconfigure(i, pad=10)
input_box1.grid(row=1, column=1)
button.grid(row=1, column=2)
input_box2.grid(row=1, column=3)

window.mainloop()
