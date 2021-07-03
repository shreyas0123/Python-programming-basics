############## problem1 ###########################

# 1.Take a variable ‘age’ which is of positive value and check the following:
# a.If age is less than 10, print “Children”.
# b.If age is more than 60 , print ‘senior citizens’
# c.If it is in between 10 and 60, print ‘normal citizen’

age = 10
if age < 10:
    print("children")
elif age > 60:
    print("senior citizens")
elif age >= 10 and age <= 60:
    print("normal citizen")
############### problem2 ###########################

# 2.Find  the final train ticket price with the following conditions. 
# a.If male and sr.citizen, 70% of fare is applicable
# b.If female and sr.citizen, 50% of fare is applicable.
# c.If female and normal citizen, 70% of fare is applicable
# d.If male and normal citizen, 100% of fare is applicable
# [Hint: First check for the gender, then calculate the fare based on age factor.. For both Male and Female ,consider them as sr.citizens if their age >=60]

gen = input("enter the Gender(M/F) :")
age = int(input("enter the age : "))
if(gen == "M" and age >= 60):
    print(" 70% of fare is applicable")
elif(gen == "F" and age >= 60):
    print(" 50% of fare is applicable")
elif(gen == "F" and age < 60):
    print("70% of fare is applicable")
elif (gen == "M" and age <60):
    print("100% of fare is applicable")

############### problem3 ##########################

# 3.Check whether the given number is positive and divisible by 5 or not.  
  
num = int(input("enter the num : "))
if (num>0):
    print('positive')
    if (num % 5 ==  0):
        print('num is divisible by 5')
    else:
        print('num is not divisible by 5')
else:
    print(" num is negative")
    if(num % 5 == 0):
        print('num is divisible by 5')
    else:
        print('num is not divisible by 5')
    
    
    
