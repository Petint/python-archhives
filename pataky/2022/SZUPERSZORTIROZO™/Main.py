"""
Szzuperszortírovó™ V3
© 2021 Petrás Bálint
Ez a SZUPERSZORTÍROZÓ, ami BÁRMILYEN számot BÁRHOGY sorba tud rendezni!
És SOHA nem hibásodik meg! Hiszen MINDEN hiba le van kezelve.
Ez a program TÖKÉLETES!!!!
"""

# Importing data from a file
def ImportData(FileName):
    print("Importind data... ",end="") # Report to DU
    global ImputFileError
    try:
        ImputFile = open('./'+FileName,"rt") # Get file
    except: # If Imput file doesn't exist
        print(f"Error, {FileName} can't be found")
        ImputFileError = True
        input()
        exit()
    #return file data as a List of floats
    FileData = ImputFile.read() # Store file contents
    del ImputFile # The variable 'ImputFlie' is no longer needed
    FileDataList = FileData.split('\n')
    # FileDataList = FileDataList.split(',') Broken, don't use.
    del FileData # Delete variable
    FileDataFloat = []
    for x in FileDataList:
        FileDataFloat.append(float(x))
    del FileDataList # Delete old list
    print("Done")
    return FileDataFloat # Return Data as a List of floats



try: # Import numbers
    ImputFileError = False # To keep track of a possible file error
    Nums = ImportData("out.txt") # Importing nums
except: # File error detection
    if ImputFileError: # Stop code whitout giving false formatting-type error.
        exit()
    print("\nError, File is emty, or is not correctly formatted.\n Please make sure you ony have a single number in a line and that you don't have any empty lines.")
    input()
    exit()
# for testing
# print(Nums)

# Asking DU witch way to sort
StDir = input("\nWitch way to sort?(up/down): ")
dirUp = False
if StDir.lower() == "up": dirUp = True  # Convert to bool
del StDir
#print(dirUp)
# Sorting


def bubbleSort(arr):
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
        print("Sorting: ",i)
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] < arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 

if dirUp: # Sort up
   bubbleSort(Nums)
   """ Old sorting
   for i in range(0,Nums.__len__()-1):
        for j in range(i+1,len(Nums)):
            print(i,j)
            if Nums[j] < Nums[i]:
                Nums[j], Nums[i] = Nums[i], Nums[j]
    """
else: # Sort down
    for i in range(0,Nums.__len__()-1):
        print(i)
        for j in range(i+1,len(Nums)):
            if Nums[j] > Nums[i]:
                Nums[j], Nums[i] = Nums[i], Nums[j]
print("Done")
# print(Nums)
# Get min and max
Xmin = Xmax = Nums[0]
for x in Nums:
    if x > Xmax:
        Xmax = x
    if x < Xmin:
        Xmin = x
print(f"Ther biggest number is: {Xmax}\nAnd the smallest is: {Xmin}")

# Writing results to a new file.
try:
    fileOut = open("Sorted.txt","x")
except:
    input("Error: Output file allready exists.\nPlease delete \'Sorted.txt\' and press return.")
    fileOut = open("Sorted.txt","x")
print("Writing output to file... ",end="")
for x in Nums:
    fileOut.write(str(x)+'\n')
print("Done")
input()
