"""
print("Két beolvasott egész számról állapítjuki meg, hogy melyik a nagyobb.")
nums = int(input("Adj meg egy egész számot: ")), int(input("Adj meg egy egész számot: "))
if nums[0] == nums[1]:
    print("A két szám egyenlő.")
else:
    print(max(nums))
"""
import tkinter

window = tkinter.Tk()
window.title('01-02')
feladat = tkinter.Label(window, text="Két beolvasott egész számról állapítjuki meg, hogy melyik a nagyobb.")
input_lable = tkinter.Label(window, text="Adj meg egy egész számot")
feladat.pack()
input_lable.pack()
window.mainloop()
