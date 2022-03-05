import json
import os

print("1.Signup\n2.Login")
login_signup=int(input("choose You longin/Singup----->> "))

if login_signup==1:

    print(" <<<<------------------<<<<<1.Singup>>>>>------------------->>>>")
 
    a=["name","lastname","password","profile","email/phone_no"]
    
    first_name=input("Creat firt name-->>")

    file=open("login.json","r")
    py=file.read()
    if first_name in py:
        print("allready exict")
        print("please try again another name")

    else:
        last_name=input("Creat last name-->>")
        num=input("Creat Password--->>")
        password1=input("Confirm Password--->>")

        if num>'A'and num<'Z' and num>'a'and num<'z' or '@' in num or '#'in num or'&' in num and num>'0' and num<9:
            if len(num)<=12:
                if num==password1:
            
                    email_phone_no=input("entr email/phone_no--->> ")
                    gender=input("enter your gender--->>")
                    dob=input("enter DOB-->>")
                    hobbi=input("Enter you hobbi--->>>")
                
                    dicription=input("enter discription-->>>")

                    c=["dicription","dob","hobbi","gender"]
                    e=[dicription,dob,hobbi,gender]

                    d2={}
                    l=[]
                    j=0
                    while j<len(c):
                        d2[c[j]]=e[j]
                        j+=1

                    b=[first_name,last_name,num,d2,email_phone_no]
               
                    d1={}
                    i=0
                    d={}
                    while i<len(a):
                        d[a[i]]=b[i]
                        i+=1
                    l.append(d)
                    d1["user"]=l
                    print("   !!! <<----- Sign up success fully ------->>  !!!")

                    if os.path.exists("login.json"):
                        file= open("login.json","r")
                        py=json.load(file)
                
                        if "user" in py:
                            l=py["user"]
                        l.append(d)
                        d1["user"]=l
                        f=open("login.json","w")
                        json.dump(d1,f,indent=6)
                        f.close()

                    else:
                        f=open("login.json","w")
                        json.dump(d1,f,indent=6)
                        f.close()
              
                
                else:
                    print("try again")
            else:
                print("maximum len of 6")
        else:
             print("invalid password ,Try again")





    
    



elif login_signup==2:
    print(" <<<<------------------<<<<<2.Login>>>>>------------------->>>>")
    first_name1=input("Enter first name---->>>")
    password=input("Enter valid password-->>")
    file=open("login.json","r")
    py=file.read()
    if first_name1 in py:
        if password in py:
            print("   !!! <<----- login success fully ------->>  !!!")
        else :
            print("invailed password please check!!")
    else:
        print("invailed name please check !!") 

    

else:
    print("Please try")

            
    










