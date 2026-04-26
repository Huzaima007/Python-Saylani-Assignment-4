
# 1 Positive / Negative / Zero

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 2 Even 

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# 3 Voting Eligibility

age = int(input("Enter age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# 4 Larger Number

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(num1, "is larger")
elif num2 > num1:
    print(num2, "is larger")
else:
    print("Both numbers are equal")



# 5 Pass / Fail

marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")


# 6 Grade

marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")



# 7 Leap Year

year = int(input("Enter year: "))
if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


# 8 Password Check

password = input("Enter password: ")
if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")


# 9 Temperature Check

temp = int(input("Enter temperature in Celsius: "))
if temp > 35:
    print("Very Hot")
elif temp >= 25:
    print("Hot")
elif temp >= 15:
    print("Normal")
else:
    print("Cold")


# 10 Marks Category

marks = int(input("Enter marks: "))
if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Very Good")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Average")
else:
    print("Fail")


# 11 Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")


# 12 Age Category

age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")


# 13 Login System

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")


# 14 FizzBuzz

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print("Not divisible by 3 or 5")


# 15 ATM

balance = int(input("Enter balance: "))
withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= balance:
    if withdraw % 500 == 0:
        print("Transaction Successful")
    else:
        print("Amount must be multiple of 500")
else:
    print("Insufficient Balance")


# 16 Exam Eligibility

attendance = int(input("Enter attendance %: "))
fee = input("Fee paid (yes/no): ")

if attendance >= 75:
    if fee == "yes":
        print("Eligible for Exam")
    else:
        print("Pay exam fee first")
else:
    print("Not eligible due to low attendance")


# 17 Online Order

amount = int(input("Enter order amount: "))
user = input("Enter user type (regular/premium): ")

if amount >= 1000:
    if user == "premium":
        print("20% discount")
    else:
        print("10% discount")
else:
    print("No discount available")


# 18 Driving Check

age = int(input("Enter age: "))
license = input("Do you have license (yes/no): ")

if age >= 18:
    if license == "yes":
        print("You can drive")
    else:
        print("Get a driving license")
else:
    print("You are underage")


# 19 Internet Status

status = input("Internet status (on/off): ")
data = int(input("Enter data balance MB: "))

if status == "on":
    if data > 0:
        print("You are connected to the internet")
    else:
        print("No data balance")
else:
    print("Internet is off")


# 20 Strong Password

password = input("Enter password: ")

if len(password) >= 8:
    if "@" in password:
        print("Strong password")
    else:
        print("Add a special character")
else:
    print("Password too short")


# 21 Movie Ticket

age = int(input("Enter age: "))
permission = input("Parental permission (yes/no): ")

if age >= 18:
    print("Ticket Allowed")
else:
    if permission == "yes":
        print("Ticket Allowed with Permission")
    else:
        print("Ticket Not Allowed")


# 22 Online Exam

login = input("Logged in (yes/no): ")
webcam = input("Webcam status (on/off): ")

if login == "yes":
    if webcam == "on":
        print("Exam Started")
    else:
        print("Turn on webcam")
else:
    print("Please login first")


# 23 Bank Loan

income = int(input("Enter monthly income: "))
score = int(input("Enter credit score: "))

if income >= 50000:
    if score >= 700:
        print("Loan Approved")
    else:
        print("Low credit score")
else:
    print("Income too low")


# 24 App Subscription

subscription = input("Subscription type (free/premium): ")
feature = input("Feature name (download/stream): ")

if subscription == "premium":
    print("Access Granted")
else:
    if feature == "stream":
        print("Access Granted")
    else:
        print("Upgrade to Premium")


# 25 Device Charging

charger = input("Charger connected (yes/no): ")
battery = int(input("Battery percentage: "))

if charger == "yes":
    if battery < 100:
        print("Charging")
    else:
        print("Battery Full")
else:
    print("Connect charger")




# 26 Traffic Fine System


speed = int(input("Enter speed: "))
emergency = input("Emergency vehicle? (yes/no): ")
rainy = input("Rainy weather? (yes/no): ")

if emergency == "yes":
    print("No fine")
else:
    fine = 0

    if speed <= 60:
        fine = 0
    elif speed <= 80:
        fine = 500
    elif speed <= 100:
        fine = 2000
    else:
        print("License suspended")

    if speed <= 100:
        if rainy == "yes" and speed > 60:
            fine = fine + (fine * 0.5)

        if fine == 0:
            print("No fine")
        else:
            print("Fine =", fine)


# 27 Company Candidate Filter

experience = int(input("Enter experience in years: "))
skill = int(input("Enter skill score: "))
test_score = int(input("Enter test score: "))
criminal_record = input("Criminal record? (yes/no): ")
job_switches = int(input("Job switches in last 2 years: "))

if criminal_record == "yes":
    print("Rejected immediately")
elif job_switches > 3:
    print("Flagged as unstable")
elif experience >= 5 and skill >= 80:
    print("Shortlisted")
elif 2 <= experience <= 4 and skill >= 70:
    print("Interview")
elif experience < 2 and test_score >= 85:
    print("Selected as Fresher")
else:
    print("Not Selected")


# 28 Passenger Clearance

baggage_weight = int(input("Enter baggage weight: "))
passport_valid = input("Passport valid? (yes/no): ")
visa_status = input("Visa status (valid/invalid): ")
criminal_check = input("Criminal check (clear/flagged): ")

if passport_valid == "no":
    print("Rejected")
elif visa_status == "invalid":
    print("Rejected")
elif criminal_check == "flagged":
    print("Security hold")
else:
    if baggage_weight > 30:
        print("Extra charge")
    print("Cleared for boarding")


# 29 Insurance Eligibility

age = int(input("Enter age: "))
smoker = input("Smoker? (yes/no): ")
disease = input("Existing disease? (yes/no): ")
income = int(input("Enter annual income: "))

if age < 18:
    print("Rejected")
elif smoker == "yes" and disease == "yes":
    print("High premium category")
elif income < 200000:
    print("Limited coverage")
elif age > 60:
    print("Special medical check required")
else:
    print("Normal approval")


# 30 Suspicious Banking Transaction

amount = int(input("Transaction amount: "))
location_match = input("Location match? (yes/no): ")
time = input("Time of transaction (day/night): ")
count = int(input("Previous transactions count: "))
device = input("Device verified? (yes/no): ")

if count > 10:
    print("Freeze account")
elif location_match == "no" and amount > 100000:
    print("Fraud alert")
elif time == "night" and device == "no":
    print("High risk")
elif amount > 100000:
    print("Suspicious")
else:
    print("Normal transaction")


# 31 Police Risk Level

criminal_record = input("Criminal record? (yes/no): ")
cases = int(input("Number of cases: "))
travel_flagged = input("Travel history flagged? (yes/no): ")
financial_score = int(input("Financial activity score: "))
last_activity = int(input("Last activity days ago: "))

if criminal_record == "yes" and cases > 3:
    print("High Risk")
elif travel_flagged == "yes" and financial_score > 80:
    print("High Risk")
elif last_activity > 365:
    print("Monitor")
elif criminal_record == "no" and financial_score <= 80 and last_activity <= 365:
    print("Low Risk")
else:
    print("Medium Risk")
