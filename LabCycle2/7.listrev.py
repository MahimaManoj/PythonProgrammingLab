lst1=[]

n1=int(input("Enter the size of first list:"))
print('Enter the elements to insert in the first list:')
for i in range(0,n1):
    ele1=int(input())
    lst1.append(ele1)
print("the first list is:",lst1)
revList = list(reversed(lst1))
print(revList)