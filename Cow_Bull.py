import random
name=input("enter your name-->>")
print("<<<----------------",name,"-------------------->>>")
print( "   | WELL COME TO COWS AND BULLS GAME |"       )
print("<<<-------------------------------------------->>")
def gcb():
    number=list(range(10))
    random.shuffle(number)
    return number

def gcb1():
    num=gcb()
    secret_num=[]
    for i in range(5):
        secret_num.append(num[i])
    return secret_num
    
def gcb2():
    bull=[]
    cow=[]
    num1=gcb1()
    print(num1)
    turns=10
    while turns>0:
        guss=int(input("Enter your guss number--->>"))
        position=int(input("Enter position of guss number--->>"))
        print("<<<<<---------<<<<->>>>----------->>>>")
        if guss in num1:
            index=num1.index(guss)
            if index==position:
                if guss not in bull:
                    bull.insert(index,guss)
                    print("Bull=",bull)
                else:
                    print("Ap ne pahale hi dal chuke hain yah number",guss)
                    print("Please try again (-_-)")
            else:
                cow.append(guss)
                print("Cow=",cow)
        if bull==num1:
            print(name,"Congutulation !!! You win the game")
            break
        else:
            print(name,"You loose the game ")
            print(name,"please try again")
        turns-=1
        print(turns,"Turns are left")
    print("Bull",bull)
    print("Cow",cow)
    # print("you loose")
def gcb3():
    print()
    print("kya ap  khelna chahate hai")
    while True:
        user=input("Enter Yes for y or Not for n -->>")
        if user =="y":
            gcb2()
            print("kya ap fir se khelna chahate hai")
        else:
            print("Ok thanks you can left <<--->>Bey")
            break
gcb3()









