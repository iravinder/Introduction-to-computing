#Ravinder Kumar SID: 21103120
#PythonAssignment#2

#======================================== Question1 ========================================

#String given in the question
string = "Python is a case sensitive language"

#a. Length of the input string
print("The length of the string is:",len(string))

#b. Reversing the order of the string
print(string[::-1])

#c. Storing "a case sensitive in a new string"
string2 = string[10:26]
print(string2)

#d. Replacing "a case sensitive" with "object oriented"
print(string.replace("a case sensitive", "object oriented"))

#e. Finding the index of substring "a"
print("The index of 'a' is:",string.find("a"))

#f. Removing the spaces between the substrings
print(string.replace(" ",""))


#======================================== Question2 ========================================

#Format provided in the question
format = '''\nHey, ABC Here!
My SID is 2110XXXX
I am from XYZ department and my CGPA is X.X'''

#Asking user for the credentials
name = str(input("Enter your name: "))
SID = str(input("Enter your SID: "))
department = str(input("Enter the name of your department: "))
CGPA = str(input("Enter your CGPA: "))

#Replacing the required substrings as per the user input 
format = format.replace("ABC", name)
format = format.replace("2110XXXX", SID)
format = format.replace("XYZ", department)
format = format.replace("X.X", CGPA)

print(format)


#======================================== Question3 ========================================

a=56
b=10

#a. Value of a&b
print("The value of a&b is:",a&b)

#b. Value of a|b
print("The value of a|b is:",a|b)

#c. Value of a^b
print("The value of a^b is:",a^b)

#d. Left shift both a & b with 2 bits
print("\nThe value of",a,"after left shift of 2 bits is:",a<<2)
print("The value of",b,"after left shift of 2 bits is:",b<<2)

#e. Right shift both a & b with 2 bits
print("\nThe value of",a,"after right shift of 2 bits is:",a>>2)
print("The value of",b,"after right shift of 2 bits is:",b>>2)


#======================================== Question4 ========================================

#Asking input of three numbers from the user
num1 = int(input("Enter the first number: ")) #first number
num2 = int(input("Enter the second number: ")) #second number
num3 = int(input("Enter the third number: ")) #third number

#Applying conditions for the comparison
if num1>=num2 and num1>=num3:
    print(num1,"is the greatest")

elif num2>=num1 and num2>=num3:
    print(num2,"is the greatest")

else:
    print(num3,"is the greatest")


#======================================== Question5 ========================================

#Asking user for the string as input
string = str(input("Enter the string: "))

#Applying condition if 'name' is present in the string entered by the user
if("name" in string):
    print("Yes, 'name' is present in the string")

else:
    print("No, 'name' is not present in the string")


#======================================== Question6 ========================================

#Asking user for the value of the sides
side1 = int(input("Enter the value of the first side "))
side2 = int(input("Enter the value of the second side "))
side3 = int(input("Enter the value of the third side "))

#Conditions of sum of sides for a triangle are:-
# (side1+side2)>side3
# (side1+side3)>side2
# (side2+side3)>side1

if ((side1+side2)>side3 and (side1+side3)>side2 and (side2+side3)>side1):
    print("Yes, the given combination of sides form a triangle")

else:
    print("No, the given combination of sides don't form a triangle")


#end
