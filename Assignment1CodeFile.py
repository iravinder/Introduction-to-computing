#Ravinder Kumar BTech CSE 1st year (21103120)

#Assignment1

#================Question1=====================

#Taking input from the user
num1 = float(input("Enter the first number "))
num2 = float(input("Enter the second number "))
num3 = float(input("Enter the third number "))

#Equation for calcualting average
avg = (num1+num2+num3)/3

print("The average of the given numbers is",avg)



#================Question2=====================

#Asking user for the gross income and number of dependents
gross_income = int(input("Enter your gross income(in dollars) "))
dependents = int(input("Enter the number of dependents "))

#Standard Deduction which all the taxpayers are allowed
standard_deduction = 10000

#Deduction per dependent
dependent_deduction = 3000

flat_tax_rate = 0.2

taxable_income = gross_income - standard_deduction - (dependent_deduction*dependents)
tax = taxable_income*flat_tax_rate

print("The amount of tax you have to pay is ",tax,"dollars")



#================Question3=====================

#Asking student details from the user
SID = int(input("Enter the student's SID "))
name = str(input("Enter the student's name "))
age = int(input("Enter the student's age "))
gender = str(input("Enter the student's gender F/M "))
course_name = str(input("Enter the student's course name "))
CGPA = float(input("Enter the student's CGPA "))

#Assigning the list option
Std_Details = [SID, name, age, gender, course_name, CGPA]

#Printing the list
print(Std_Details)



#================Question4=====================

#Asking user for the marks of the students
marks_std1 = int(input("Enter the marks of first student "))
marks_std2 = int(input("Enter the marks of second student "))
marks_std3 = int(input("Enter the marks of third student "))
marks_std4 = int(input("Enter the marks of forth student "))
marks_std5 = int(input("Enter the marks of fifth student "))

#Assigning the list option
list = [marks_std1, marks_std2, marks_std3, marks_std4, marks_std5]

#Sorting the list
sorted_list = sorted(list)

print(sorted_list)



#================Question5(a)=====================

#List of colour
color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#Printing initial color list
print("Prior color list: ",color_list)

#Removing 4th element
color_list.remove('Black')

#Printing the list after the removal of 4th element
print("Color list after removal of the 4th element: ",color_list)



#================Question5(b)=====================

#List of colour
color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#Printing initial color list
print("Prior color list: ",color_list)

#Replacing Black and Pink with Purple
color_list[3:5] = ['Purple']

#Printing the list after the replacing Black and Pink with Purple
print("Color list after replacing Black and Pink with Purple ",color_list)
