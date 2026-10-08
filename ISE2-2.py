f = open("student.txt","w")

f.write("101 Shreyash 83\n")
f.write("102 Prathmesh 84\n")
f.write("103 Vighnesh 90\n")

f.close()

roll = input("Enter roll no:  ")

f = open("student.txt","r")

for line in f:
    data = line.split()
    if data[0]==roll:
        print("Record:",line)
        break

    f.close()
