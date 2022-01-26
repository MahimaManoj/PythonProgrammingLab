lst=[]
n=int(input("enter the size of list"))
# print("ENTER THE ELEMENTS TO INSERT INTO THE LIST")
for i in range(0,n):
    ele=int(input())
    if(ele>100):
        print("OVER")
        lst.append("OVER")
    else:
        lst.append(ele)
print(lst)