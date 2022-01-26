
lst=[]
lst1=[]
n=int(input("Enter the number of elements in the list:"))

# (a)Generate positive list of numbers from a given list of integers
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print(lst)

for i in lst:
    if(i>=0):
        lst1.append(i)
print(lst1)

# (b)Square of N numbers
print("Enter the square of N numbers of the list",n*n)

# (c)Form a list of vowels selected from a given word
str="PROGRAMING"
vowels="AaEeIiOoUu"

vow=[word for word in str if word in vowels]
print("Vowels of the given string is",vow)









