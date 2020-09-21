ref = open(r"D:\Research Project With Dr.Paluch\Reference Data.txt","r")
CAS = open(r"D:\Research Project With Dr.Paluch\MOSCED Data.txt","r")
dict={}
for a in ref:
    x = a.split()
    casnumber = str(x[0])
    dict[casnumber]=x[0]
for i in CAS:
    i = i.strip()
    if i in dict:
        print(dict[i])
    else:
        print("none")
#Testing