# if文

# if else
age = 23
age_alcohol = 20
age_drive = 18
if age > age_alcohol:
    print("you can drink beer!")
else:
    print("you are too young to drink beer")

# if elif else
if age > age_alcohol:
    print("you can drink beer!")
elif age < age_drive:
    print("you cannot even drive!")
else:
    print("you are not allowed to drink beer but you can drive... only if you have a driver's license!")

# if not
age = int(input("how old are you?"))
if not 0 < age < 120:
    print("the value is invalid!")


# challenge1
balance = 3000000
withdrawal = 23000

if balance > withdrawal:
    # balance = balance - withdrawal
    balance -= withdrawal
    print("Your new balance is {}".format(balance))
else:
    print("You don't have money.... do you? ")

# challenge2
withdrawal_limit = 1000000

if withdrawal > withdrawal_limit:
    print("The withdrawal limit is {}".format(withdrawal_limit))
elif balance > withdrawal:
    # balance = balance - withdrawal
    balance -= withdrawal
    print("Your new balance is {}".format(balance))
else:
    print("You don't have money.... do you? ")

#論理演算子を使ってもOK
if withdrawal < withdrawal_limit and balance > withdrawal:
    # balance = balance - withdrawal
    balance -= withdrawal
    print("Your new balance is {}".format(balance))
else:
    print("Withdrawal exceeds limit ({}) or balance ({})".format(withdrawal_limit, balance))

