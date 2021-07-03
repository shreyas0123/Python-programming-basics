#################### problem1 ##################
#1.A) list1=[1,5.5,(10+20j),’data science’].. Print default functions and parameters exists in list1.
# B) How do we create a sequence of numbers in Python.
# C)  Read the input from keyboard and print a sequence of numbers up to that number

list1 = [1,5.5,(10+20j),'data science']
dir(list1)# print default function and parameters exist in list1 
#B.
[x for x in range (10,20)] #creating sequence numbers

#c.
num = int(input("enter the number : "))
for num in range(1,num+1):
    print(num)
    
###################### problem2 #################
# 2.Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) and other 
# list contains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
#  Create a dictionary such that list2 are keys and list 1 are values..
    
list2 = [x for x in range(0,10)]
list2
list3 = ['zero' ,'one','two','three','four','five','six','seven','eight','nine']
dictn = {list3[i] : list2[i] for i in range(len(list3))}
print(dictn)
########################### problem3 ###################
#3.Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that Add 10 to the even number and multiply with 5 if it is odd number in the list1..

list5 = [3,4,5,6,7,8]
list6 = []
for i in range(len(list5)):
    if list5[i] %2 == 0:
        a = list5[i]+10
        list6.append(a)
    else:
        b = list5[i]*5
        list6.append(b)
print(list6)

########################## problem4 #######################
 # 4.Write a simple user defined function that greets a person in such a way that :
 # i) It should accept both name of person and message you want to deliver.
 # ii) If no message is provided, it should greet a default message ‘How are you’
 # Ex: Hello ---xxxx---, How are you  - default message.
 # Ex: Hello ---xxxx---, --xx your message xx---

def digiworld():
    nam = input("enter the name :")
    msg = input("type the msg :")
    if msg == "":
        print("Hello, " +nam+ " How are you")
    else:
        print("Hello, " +nam+ " " +msg+ "")
    
digiworld()
    
