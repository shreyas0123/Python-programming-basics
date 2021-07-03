

#################### problem1 #############################

# 1.Construct 2 lists containing all the available data types  (integer, float, string, complex and Boolean) and do the following..
# a.Create another list by concatenating above 2 lists
# b.Find the frequency of each element in the concatenated list.
# c.Print the list in reverse order.

list1 = [20,30.5,"shreyas",30+3j,'true']
list2 = [20,60.5,"nithin",20+4j,'true']
list3 = list1 + list2 #concatenating the 2 lists
list3
list3.count(20) #finding frequency
list3.count(30.5)
list3.count('shreyas')
list3.count(30+3j)
list3.count('true')
list3.count(60.5)
list3.count("nithin")
list3.count(20+4j)
list3.reverse() # reversing a list
list3
##################### problem2 ##################################

# 2.Create 2 Sets containing integers (numbers from 1 to 10 in one set and 5 to 15 in other set)
# a.Find the common elements in above 2 Sets.
# b.Find the elements that are not common.
# c.Remove element 7 from both the Sets.

set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {5,6,7,8,9,10,11,12,13,14,15 }
inter = set1.intersection(set2)#finding common
notcm = set1^set2 #finding not common
notcm
set1.discard(7)#to remove 7
set1
set2.discard(7)
set2
###################### problem3 ####################################


# 3.Create a data dictionary of 5 states having state name as key and number of covid-19 cases as values.
# a.Print only state names from the dictionary.
# b.Update another country and it’s covid-19 cases in the dictionary.
 
dictn = {'karnataka':50000,'kerala':40000,'delhi':30000,'tamilnadu':2000,'andrapradesh':10000}
dictn.keys()#print states
dictn['america'] = 100000#adding another keys and values to the existing dictn
dictn
