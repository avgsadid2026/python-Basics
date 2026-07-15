# str1="this is sadid"
# str2= 'sadidahmed'

# "this is sadid's tutorial"

# 'this is sadid"s tutorial'


#lenth of a string
# str1="this is a string.\n we are creating a python code"
# print (str1)
# print (len(str1))


#concatenation
# str1="sadid"
# str2="ahmed"
# str3= str1+str2
# final_str= str1+ " " + str2
# print (final_str)

#indexing
# str="Sadid Ahmed"
# print (str[3])


#slicing
# (Accessing parts of a string )
#str[starting_idx : ending_idx] ending idx is not included
# str= "Sadid Ahmed"
# print(str[1:4])
# print (str[0:]) evabeo last index porjonto jaoa jay
 #NEGATIVE INDEX (-1 theke shuru hoy)
# A  P  P  L  E
#-5 -5 -3 -2  -1
# str="Aplle"
# print (str[-3 : -1])



#string Functions 

#1
# str="I am sadid Ahmed"
# print (str.endswith("ed")) #mane last ee joto tuku die ends hoise sheta

#2
# str="i am sadid AHmed"
# print (str.capitalize()) #captalize 1st character  # eta korar por kintu new ekta string create kortese
# print(str) #agertake change kortese na 

#3
# str="I am Sadid Ahmed Shishir"
# print (str.replace("am","was")) #new string die old string replace kore 

#4
# str="I am sadid Ahmed"
# print (str.find("s"))  #first e letter ta jei word theke start hbe shetar index return korbe 

#5
# str= "this is me is sadid"
# print (str.count("is")) oi string ta kotobar ase shetar count 




#conditional Statement 
# light = "green"

# if (light=="red"): #if condition always check korbei , jotota if thakbe tototai
#     print ("stop")
# elif(light=="green"): #if condition jodi false hoy tokhn elif check korbe
#     print("go")
# else:
#     print ("light is broken")

# print("end of code there")


#PROBLEM 1:-
# marks = int (input ("Enter Your marks here :"))

# if(marks >=90):
#     garde="A"
# elif(marks >=80 and marks <90):
#     grade ="B"
# elif(marks >=70 and marks <80):
#     grade="c"
# else:
#     grade="D"

# print ("grade of a student ->:",grade)

#probelm-2:
a=int (input ("enter first number :"))
b=int (input ("enter Second number :"))
c=int (input ("enter third number :"))

if(a>=b and a>=c):
    print ("first number is largest",a)
elif(b>=c):
    print("second number is largest", b)
else:
    print ("third number is largest",c)











