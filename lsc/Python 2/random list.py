from random import randint as randy
list1 = [randy(0,100) for i in range(100)]
evenLst = []
oddLst = []
for i in range(len(list1)):
    if list1[i] % 2 == 0:
        evenLst.append(list1[i])
    else:
        oddLst.append(list1[i])
print(evenLst, end="\n\n")
print(oddLst)
