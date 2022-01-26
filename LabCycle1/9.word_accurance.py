words=input("enter the sentance")
search=input("enter the word to be count")
words=words.split()
counts=0
for word in words:
    if search==word:
        counts+= 1
    else:
        pass

print(counts)
        