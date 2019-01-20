import os
import time

customerName = ''
cId = ''
balance = 0
prevTrans = 0

def cls():
    os.system('clear')

def customer():
    cId = input('Enter your Id: ')
    customerName = input('Enter your name: ')
    input('Enter your password: ')
    showMenu()

def deposit(amount):
    global balance, prevTrans
    balance = balance + amount
    print('You have deposited Rs ', amount, '. Your total balance is Rs ', balance)
    prevTrans = amount

def withdraw(amount):
    global balance, prevTrans
    balance = balance - amount
    prevTrans = -amount

def getPreviousTransaction():
    if prevTrans <= 0:
        print('You have withdrawn ', prevTrans , 'amount')
    elif prevTrans > 0:
        print('You have deposited ', prevTrans,  'amount')


def showMenu():
    print('Welcome to Nepal Rastra Bank' + customerName)
    time.sleep(0.5)
    print('1. Check Balance')
    print('2. Deposit Balance')
    print('3. Withdraw Amount')
    print('4. Previous Transaction')
    print('5. Exit')

    option = input('Enter your choice: ')
    if option == '1':
        print('Your current ammount is ', balance)
    elif option == '2':
        amount = int(input('Enter amount to be deposited: '))
        deposit(amount)
    elif option == '3':
        amount = int(input('Enter amount to be withdrawn: '))
        withdraw(amount)
    elif option == '4':
        getPreviousTransaction()
    elif option == '5':
        print('***************')

    else:
        print('Invalid choice. Try again!')

    print('Thank you for using our service. Visit again')

customer()
