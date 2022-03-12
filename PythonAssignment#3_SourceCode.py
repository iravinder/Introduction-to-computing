#21103120 Ravinder Kumar


#========================= Question 1 ===========================


# defining the fuction
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

#asking user for the input string
string = input("Enter the string: ")

#printing the required output
print("The number of words or elements are:\n",word_count(string))


#========================= Question 2 ===========================

def Next_Date():
    list1=[1,3,5,7,8]
    list2=[4,6,9,11]
    list3=[2]
    list4=[12]
    while(True):                 #while loop is used so that if any wrong value is entered  then values will be entered again
        day=int(input("Enter the day: "))
        if(1<=day<=31):
            break
        else:
            print("Please Enter a valid day")
    while(True):                  #while loop is used so that if any wrong value is entered  then values will be entered again
        month=int(input("Enter the month: "))
        if(1<=month<=12):
            break
        else:
            print("Please Enter a valid month")
    while(True):                #while loop is used so that if any wrong value is entered  then values will be entered again
        year=int(input("Enter the year: "))
        if(1800<=year<=2025):
            break
        else:
            print("Please Enter year from 1800 to 2025 only")
    if month in list1 :    
        if(day==31):
            day=1
            month=month+1
            print(day,"/",month,"/",year)
        elif(day<31):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("INVALID DATE TRY AGAIN")
            Next_Date()
    
    elif month in list2 :
        if(day==30):
            day=1
            month=month+1  
            print(day,"/",month,"/",year)   
        elif(day<30):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("INVALID DATE TRY AGAIN") 
            Next_Date()      
    elif month in list3:
        if(year % 4 == 0):  
            if(day==29):
                day=1
                month=month+1
                print(day,"/",month,"/",year)
            elif(day<29):
                day+=1
                print(day,"/",month,"/",year)
            else:
                print("INVALID DATE TRY AGAIN")
                Next_Date()
        else:
            if(day==28):
                day=1
                month+=1
                print(day,"/",month,"/",year)
            elif(day<28):
                day+=1
                print(day,"/",month,"/",year)
            else:
                print("INVALID DATE TRY AGAIN")
                Next_Date()
    elif month in list4:
        if(day==31):
            day=1
            month=1
            year+=1  
            print(day,"/",month,"/",year)
        elif(day<31):
            day+=1
            print(day,"/",month,"/",year)
        else:
            print("INVALID DATE TRY AGAIN")
            Next_Date()
        
    else:
        print("INVALID DATE TRY AGAIN")
        Next_Date()
Next_Date()
print("\n")


#========================= Question 3 ===========================


#asking user for the number of elements or upto which he wants the squares of respective numbers
n = int(input("Enter the number upto which you want the list: "))

#defining the list
square_list = [(i, i**2) for i in range(1,n+1)]

#printing the list
print(square_list)


#========================= Question 4 ===========================


#defining the function for the grade and performance
def grade(p):
    if p==4:
        print("Your grade is 'D' and Poor performance")

    elif p==5:
        print("Your grade is 'C' and Below Average performance")

    elif p==6:
        print("Your grade is 'C+' and Average performance")

    elif p==7:
        print("Your grade is 'B' and Good performance")

    elif p==8:
        print("Your grade is 'B+' and Very Good performance")

    elif p==9:
        print("Your grade is 'A' and Excellent performance")

    elif p==10:
        print("Your grade is 'A+' and Outstanding performance")

    elif p<4 and p>10:
        print("Error! Grade points are out of the range")

#asking user for the grade points
grade_points = int(input("Enter the grade points(1-10): "))

#printing the grade and performance
grade(grade_points)


#========================= Question 5 ===========================


#Asking user for the number of lines of the sequence
n = int(input("Enter the value of n: "))

#defining the loop
for i in range(1,n+1): #range for lines
    print() #to print in a new line
    print(" "*(i-1),end="") #spaces for the respective lines
    for j in range(1,(2*n-(2*i-1))+1): #to print the alphabets as per the question
        print(chr(65 + (j-1)),end="")


#========================= Question 6 ===========================


sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}

while True:
    option = input("Do you want to enter another student entry(Y or N):").upper()
    if option == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif option == 'N':
        break
    else:
        print('Invalid input!')

#part a. print the dictionary
print("<a>",students)

#part b. sort acc to the names
print("<b>",{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#part c. sort acc to the SIDs
print("<c>",{k:v for k,v in sorted(students.items())})

#part d. search for a student by their SID
sid = int(input("Search Name with SID: "))
print("<d>",students[sid])


#========================= Question 7 ===========================


#defining the fuction for the sequence using recursion
def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

#Asking user for the number of terms in the series
n = int(input("Enter th number of terms in the sequence: "))

if n <= 0:     
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(n):
       print(fibonacci(i), " ", end="")
       sum=sum+fibonacci(i)

#Avergae of the fibonacci series
average = sum/n
print("\nThe average of the fibonacci series is: ",average)


#========================= Question 8 ===========================


Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# part a
Set_Union = Set1.union(Set2)
Set_Intersection = Set1.intersection(Set2)
Part_A_Set = Set_Union - Set_Intersection
print("<a>", Part_A_Set)

# part b(Subtracting intersection of sets taken two at a time from the Union of all three sets)
Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("<b>", Part_B_Set)

# part c(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
Part_C_Set=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("<c>",Part_C_Set)
# part d(Excluding the numbers from 1 to 10 that are occuring in Set1)
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("<d>", Part_D_Set)
# part e(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("<e>", Part_E_Set)
