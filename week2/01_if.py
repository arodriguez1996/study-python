# Conditional Statements
import os
os.system("clear")


#* Simple if

age = 18
if age >= 18:
    print("Adult")
    print("You can vote")
    print("You can drink")
else:
    print("children")
    print("You can't vote")
    print("You can't drink")

#* if-elif-else

rank = 1000
if rank <= 3:
    print("Gold")
elif rank <= 5:
    print("Silver")
else:
    print("Bronze")

#* Nested if

have_identification = True
if age >= 18 and have_identification:
    print("You can vote")
else:
    print("You can't vote")


#! not recomended
if age >= 18:
    if have_identification:
        print("You can vote")
    else:
        print("You can't vote, you need identification")
else:
    print("You can't vote, you need identification and you need to be 18 years old") 


have_monthly_payment_tc = True
have_minimun_monthly_payment_tc = False

if have_monthly_payment_tc or have_minimun_monthly_payment_tc:
    print("You survive this month")
else:
    print("You can't survive this month")

is_weekend = False

if not is_weekend:
    print('Go to work')


#* Ternary Operator

