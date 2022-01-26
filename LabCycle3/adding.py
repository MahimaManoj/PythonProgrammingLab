a=input("enter the word:")
def word(w):
    w1=w[3:]
    if w1!="ing":
        print("adding,'ing'=",w+"ing")
    else:
        print("adding,'ly'=",w+"ly")
        word(w=a)