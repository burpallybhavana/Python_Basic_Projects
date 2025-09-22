#Leap year checker using if/else

year = int(input("Enter a year: "))
if(year % 4 == 0):
    if(year % 400 == 0):
        print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#Voting Eligibility Checker 
age = int(input("Enter your age: "))
if(age >= 18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#Check whether a number is positive, negative or zero
n = float(input("Enter a number: "))
if(n > 0):
    print(f"{n} is a positive number")
elif(n < 0):
    print(f"{n} is a negative number")
else:
    print("The number is zero")