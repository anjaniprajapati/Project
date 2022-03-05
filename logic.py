
# import json 
# languages=["english","hindi","tamil","gujrati","bengali","english","english","gujrati","marathi","bengali","hindi","hindi","hindi"]		
# i=0;dic={} ; l1=[]
# count1=0;count2=0;count3=0;count4=0;count5=0;count6=0
# while i <len(languages):
# 	if languages[i] not in l1:
# 		l1.append(languages[i])
	
# 	if languages[i]=="english":
# 		count1+=1
# 	if languages[i]=="hindi":
# 		count2+=1
# 	if languages[i]=="tamil":
# 		count3+=1
# 	if languages[i]=="gujrati":
# 		count4+=1
# 	if languages[i]=="bengali":
# 		count5+=1
# 	if languages[i]=="marathi":
# 		count6+=1	
# 	i+=1
# l=[count1,count2,count3,count4,count5,count6]
# j=0
# while j<len(l):
#     dic[l1[j]]=(l[j])
#     j+=1
# json_ob=json.dumps(dic,indent=6)
# print(json_ob)

# import json
# l=["english","hindi","tamil","gujrati","bengali","english","english","gujrati","marathi","bengali","hindi","hindi","hindi"]
# i=0
# l3=[]
# while i<len(l):
#     if l[i] not in l3:
#         l3.append(l[i])
#     a=l.count("english")
#     a1=l.count("hindi")
#     a2=l.count("tamil")
#     a3=l.count("gujrati")
#     a4=l.count("bengali")
#     a5=l.count("marathi")
#     i+=1
# l2=[a,a1,a2,a3,a4,a5]
# d={}
# j=0
# while j<len(l2):
#     d[l3[j]]=l2[j]
#     j+=1
# json_ob=json.dumps(d,indent=6)
# print(json_ob)


# import json
# l=["english","hindi","tamil","gujrati","bengali","english","english","gujrati","marathi","bengali","hindi","hindi","hindi"]
# i=0
# l3={}
# while i<len(l):
#     l3[l[i]]=l.count(l[i])
#     i+=1
# file=open("anj.json","w")
# json_ob=json.dump(l3,file,indent=6)
# file.close()
# file1=open("anj.json","r")
# py=json.load(file1)
# print(py)
# file1.close()
# print(json_ob)
# json_ob=json.dumps(l3,indent=6)
# print(json_ob)

a=input("name")
b=input("pass")
c={"n":"Anjani","s":"we","p":"123"}
for i in c:
    
    if c[i]==a and c[i]==b:
        print("yes")
        break
else:
    print("no")