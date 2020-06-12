CAS = open(r"D:\Research Project With Dr.Paluch\CAS.txt","r")
database = open(r"D:\Research Project With Dr.Paluch\Octanol - Database.txt","r")
cas = []
dict1 = {}
for i in range (13540):
    x  = database.readline()
    list1 = x.split()
    if len(list1) == 3:
        number = list1[0]
        logK = list1[1]
        K = list1[2]
        dict1[number] = K
    else:
        pass
for i in range (6482):
    y = CAS.readline()
    cas.append(str(y).strip())
for i in range (6482):
    if cas[i] in dict1:
        print(dict1[cas[i]])
    else:
        print("none")