# Write a program that uses a for loop to print months of the year
def writeMonths(alist):
    for value in alist:
        print(f'One of the months of the year is {value}')
        

myList = ["January", "Febuary", "March", "April"]   

writeMonths(myList)

def anotherWay(alist):
    for word in alist:
        print("One month of the year is {}".format(word))
        
myList2 = ["March", "October", "June", "July"]

anotherWay(myList2)