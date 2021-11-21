 #String
xto = "Christopher Nzan"
print("Christopher Nzan")

#Cocantinate string
print(xto + " Is a big man")

print(xto + " " + xto)

#string methods
print(xto.lower()) #convert to lower
print(xto.islower()) #verify case
print(xto.isupper()) #verify case
print(xto.upper()) #convert to lower
print(xto.isupper()) #verify case
print(xto.islower()) #verify case
print(xto.upper().isupper()) #convert to upper and verify case
print(xto.lower().islower()) #convert to lower and verify case
print(len(xto)) #verify length of character in string
print(xto[0]) #verify position of character by index
print(xto.index("n")) #index of a character in a string
print(xto.index("N")) #index of a character in a string
print(xto.index("Nzan")) #index of character in a string
print(xto.replace("Nzan", "Ekok")) #replacing characters in string


                                                #Interger
print(-419.999)
digit = 419
print(50 * 2 / 2)

#interger operators
print(1+1) #addition
print(1-1) #Substraction
print(1*1) #Multiplication
print(1/1) #Division
print(1%1) #Remainder/Mudulies

print(digit) #printing interger varable

print(str(digit)) #converting number to string

#concantinating interger and string
print(str(digit) + xto)

#interger methods
print(abs(digit)) #absulute value of a number
print(pow(419, 2)) #raising numbers to a specific power
print(pow(digit , 2)) #raising number to a specific power
print(max(2, 4, 6, 8)) #validating the maximum number
print(min(2, 4, 6, 8)) #validating the minimum number
print(round(4.777)) #rounding up numbers

from math import * #Import math function
print(floor(4.789)) #picking the lowest number in a decimal
print(sqrt(49)) #square root

'''' #Commented out input functions and varables

                                                    #Getting Input
input("Enter Something:") #Calling an input
something = input("Enter Something : ") #defining an input varable

print(something + xto + str(digit)) #Concantinating an input, string and interger varables



#Basic Calculator
number1 = input("Enter first number: ")
number2 = input("enter second number: ") #all inputs fuctions are string
result = int(number1) + float(number2)  #converting string to int and float
print(result)

#Assignment: Script a madlib using input.

'''

                                                    #List
months = [
    "January","February","March","April","May","June","July","August","September","October","November","December"
    ]
months_code = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
]

#Call List
print(months) #Call list
print(months[9]) #Call element in list by index
print(months[-1]) #Call list backward by index
print(months[6:]) #call list by range from index to end.
print(months[3:6]) #call list by specific index range

#Modifying list
print(months[0]) #call element in list by index
months[0] = "First month" #modify list by index position
print(months) #Call modified list
print(months[0]) #Call specific modified element by index position

#List methods
months.extend(months_code) #concantinate 2 list 
print(months) #call concantinated list
months.append("Extra month") #Adding element to the end of a list
months_code.append(13) #Adding element to the end of a list
print(months) #calling appended list
print(months_code) #calling appended list
months_code.insert(1, 1.5) #insert an element to a list
print(months_code) #call list with inserted element
months_code.remove(13) #Remove an element from a list
print(months_code) #call modified list
months_code.pop() #remove the last element in the list
print(months_code) #call popped list
print(months_code.index(5)) #call element in list by index
print(months_code.count(5)) #count number of element in list
months_code.sort() #Arrange elements in accending or alphabetical order
print(months_code) #call modified list
months_code.reverse() #reversr the order of a list
print(months_code) #call the modified list
months_code2 = months_code.copy()
print(months_code2)
months_code.clear() #clear all element from a list
print(months_code) #call cleared list


                                        #Tuples

quater = (1, 2, 3, 4) #tuple are immutable
print(quater)
print(quater[0]) #calling tuple element by index


                                        #Function


def x(): #defining a function
    print(123)
x() #calling a function

def y(a): #passing a single parameter to a funtion
    print(a) #defining the body
y(7) #calling a function with params

def z(b,c): #passing multiple params to a function
    print(b,c) #defining the body
z(1,3) #calling function with multiple params

def ax(i): # 
    return i * i #return function
print(ax(3)) #calling return function


                                        #If Statement
if xto is "religious":
    print(xto + " is a catholic")
elif xto is not "religious":
    print(xto + " is irreligious")
else:
    print(xto +" is neither religious nor irreligious")

#Complex if statement
def friends(gender,name): #combination of def and if 
    if gender == "male" and name == "Ayo":
        print(name + " is my main man")
    elif gender == "female" and name == "Benee":
        print (name + " Is the LOML")
    else:
        print("Try again")

gender = input("What's your friends gender? ")
name = input("What's your friend's name? ")

friends(gender, name)

