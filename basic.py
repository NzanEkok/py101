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

#List Methods
months.extend(months_code) #concantinate 2 list 
print(months) #call concantinated list
months.append("Extra month") #Adding element to the end of a list
months_code.append(13) #Adding element to the end of a list
print(months) #calling appended list
print(months_code) #calling appended list
months_code.insert(1, 0.5) #insert an element to a list
print(months_code) #call list with inserted element




