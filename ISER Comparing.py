ISER = open(r"D:\Research Project with Dr.Paluch\ISER Database.txt", "r")
CAS = open(r"D:\CAS Octanol Database.txt", "r")
def count_line(x):
    return int(sum(1 for line in x))
dict = {}
for a in ISER:
    x = a.split()
    casnumber = str(x[0])
    dict[casnumber] = x[2]
for i in CAS:
    i = i.strip()
    if i in dict:
        print(dict[i])
    else:
        print("none")





