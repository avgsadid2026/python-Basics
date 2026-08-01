#loops in python..
# loops are used to repeat instruction

#while loop

# count =1
# while count<=5 :
#     print("hello",count)
#     count +=1
# print(count)

#problem 2: print the multiplication table of a number n
# i=1
# while i<=10:
#     print(3*i)
#     i+=1

#prints the elements of the following list using a loop
# nums=[1,2,3,4,5,6]
# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1


#Break And Continue
#Break
# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1
# print("ENd Of Loop ")

#continue
# i=1
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue #skip
#     print(i)
#     i+=1

#for Loop: sequential Traversal er Jonno Ei loop use kori
# nums=[1,2,3,4]
# for val in nums:
#     print(val)

#1) print the elements of the following list using a loop
# nums=[1,4,9,16,25,81,100]
# for el in nums:
#     print(el)

#2) Find Number in tuples:
# nums=(1,2,3,4,5,4,6)
# x=4
# idx=0
# for el in nums:
#     if(el==x):
#         print(idx)
#     idx+=1




#Range Function
# seq=range(10)
# for i in seq:
    # print(i)
##and Aro Short Vabe
# for i in range(10): #range(stop)
#     print(i)

# for i in range (2,10): #range(start , stop)
#     print(i)

# for i in range (2,10,2): #range(start , stop , step)
#     print(i)

#problem 1: print a multiplication table of a number n
# n=int(input("enter the number:"))
# for i in range (1,11):
#     print(n*i)






#pass Statement: pass is a null statement that does nothing , it is  used as a placeholder for future code
# for i in range(5):
#     pass
# if i>7:
#     pass
# print(" Some usefull work")

#problem 1): sum of n numbers
# n=5
# sum=0
# for i in range (1,n+1):
#     sum+=i
# print("total sum=",sum)

#problem 2): find the factorial of n numbers
# n=5
# fact=1
# for i in range (1,n+1):
#     fact*=i
# print(fact)