# might have to change directory
CAS = open(r"D:\Research Project With Dr.Paluch\CAS.txt","r")
database = open(r"D:\Research Project With Dr.Paluch\Water Solvent - Database.txt","r")
cas = []
dict1 = {}
for i in range(16872):
    x = database.readline()
    list1 = x.split()
    if len(list1) == 3:
        number = list1[0]
        temperature = list1[1]
        solvent = list1[2]
        dict1[number] = temperature
    else:
        pass
for i in range(6482):
    y = CAS.readline()
    cas.append(str(y).strip())
for i in range(6482):
    if cas[i] in dict1:
        print(dict1[cas[i]])
    else:
        print("none")




