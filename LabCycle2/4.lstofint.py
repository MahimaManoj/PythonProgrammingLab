lst1=[]
lst2=[]

n1=int(input("Enter the size of first list:"))
print('Enter the elements to insert in the first list:')
for i in range(0,n1):
    ele1=int(input())
    lst1.append(ele1)
print("the first list is:",lst1)

n2=int(input("Enter the size of the second list:"))
print("Enter the elements:")
for i in range(0,n2):
    ele2=int(input())
    lst2.append(ele2)
print("The second list is:",lst2)

#(a) Whether list are of same length
len1=len(lst1)
len2=len(lst2)

if(len1==len2):
    print("both the list are of same length")
else:
    print("both the list are of different length")

#(b) whether list sums to same value
sum1=sum(lst1)
sum2=sum(lst2)

if(sum1==sum2):
    print("Sum of both the lsit is same")
else:
    print("Sum of both the list is not same")

#(c) whether any value occur in both
for ele in lst1:
    for el in lst2:
        if(ele==el):
            print(ele,"is present in both the list")
