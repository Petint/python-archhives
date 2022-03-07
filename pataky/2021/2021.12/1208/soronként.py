pataky = open("szamok.txt","rt")
opf = open("outpt.txt","wt")
i = 0
for ln in pataky:
    if i == 3:
        i = 0
        opf.write(ln)
    i+=1
opf.close()
pataky.close()

