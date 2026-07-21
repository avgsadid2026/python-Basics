#learning About tuples


# tup=(2,1,3,1)
# print(type(tup))
# print(tup[0])
# tup[0]=5 (tuple and string ee assignment kora jay na )
# tup=()
# print(tup)  /// blank tuple print korar jonno


# single element print korar jonno
# tup=(1,)
# print(tup)
# print(type(tup))

#tup methods______
 #count total occurances


#problem 1 : WAP to ask the user to enter names of their 3 favourite movies and store them in a list
# sol:
# movies=[]
# movies.append(input("Enter the first movie"))
# movies.append(input("Enter the second movie"))
# movies.append(input("Enter the third movie"))
# print(movies)


#problem 2: check PalinDrome Or NOt
list1 =[1,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 ==list1):
    print("palindrome")
else:
    print("Not palindrome ")
