fname=[]
strn=int(input("Enter the number of names to be inputed"))
print("Enter full names:")
for i in range(0,strn):
    f=input().split(" ")[0]
    fname.append(f)
print(fname)
for i in fname:
    acount=i.count("a")
    print("Number of 'a's in {0} is {1}".format(i,acount))
