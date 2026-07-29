#dictonary = they are unodered and mutable and don't allow duplicate keys

# info={
#     "key":"value ",
#     "name":"sadid Ahmed",
#     "learning":"coding",
#     "age":23,
#     "subjects":["python","c","java"], #list oo store kora jay
#     "topics":("dict","set"), #tuples oo store kora jay
#     12:12.3

# }
# print (info["name"]) #alada alada vabe value access kora jay 
# info["name"]= "messi" #new vabe value oo store kora jay
# print(info)



# null_dict={}
# null_dict["name"]="sadid"
# print(null_dict)


#nested Dictionary
# student={
#     "name":"Sadid AHmed",
#     "subjects":{
#         "phy":97,
#         "math":78
#     }
# }
# print(student["subjects"]["math"])


#Dictionary Methods :
# student={
#     "name":"Sadid AHmed",
#     "subjects":{
#         "phy":97,
#         "math":78
#     }
# }
# print(list(student.keys())) #type cast kore ami student.keys() ei method ta use korsi


# print(list(student.values())) #student.values()mehtod use hoese


# pairs=list(student.items())#student.items() method use kora hoese
# print(pairs[0]) #indivudually Access kora jasse


# print(student["name"])
# print(student.get("name"))
#2 ta dekhte same holeo , 1st ee jodi ami print(student["name22"]) kori tahole error through korbe and baki line gulo print hbe na 
# and second tay jodi print(student.get("name2")) kori vul kore , tahole "none" print korbe kintu error through korbe na , baki line gulo thik thak cholbe
# print(student["name2"]) 
# print ("sadid") # ei line ar print hbe na
# print(student.get("name2")) # none output dekhabe and porer line print korbe 
# print("sadid")

# student.update({"city":"Rangpur"})
# print(student)






#set in phython 
#set is the collection of  the unorder items
#each element in the set must be unique and immutable , but set nijei mutable
#set er modhey kokhno list and dictionary store hbe na

# collection = {1,2,3,4, "hello", "hello"} #duplicate value ke ignore korbe
# print(collection)
# print(type(collection))
# print(len(collection))

#syntax of empty set
# collection = set() 
# print(type(collection))

#set methods
# collection =set()
# collection.add(1)
# collection .add(2)
# collection.add(2)
# collection.remove(1) 
# #jodi kono element exist na kora sotteo ami jodi remove korte chai , tahole key error ashbe
# collection.add((1,2,3))
# print(len(collection))
#unhashable means jader value change hoe jay as  example = dict,list
# collection={"hello","sadid", "ahmed"}
# print(collection.pop())#randomly value pop korbe

# set1={1,2,3}
# set2={3,4,5}
# print(set1.union(set2))
# print(set1.intersection(set2))






#practise problems:
#1) store some words in python dictionary
# dictionary={
#     "cat":"a small animal",
#     "table": ("a piece of furniture", "list of facts")
# }
# print(dictionary)

#problem 2:
# marks={}
# x=int(input("enter phy:"))
# marks.update({"phy":x})
# x=int(input("enter math:"))
# marks.update({"math":x})
# x=int(input("enter chem:"))
# marks.update({"chem":x})
# print(marks)


#problem 3: Figure Out A way to store 9 & 9.0 as separate values in the set
values={
    ("float",9.0) ,#tuples er madhome pair set ee add korlam
    ("int", 9)
}
print(values)
