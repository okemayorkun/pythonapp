from bankAccount import BankAccount
from student import Student

x = 'thursday'

def execute(score):
    print(x)
    if score >= 70 and score <= 100 :
        print('A')
    elif score >= 60 and score <= 69 :
        print('B')
    elif score >= 50 and score <= 59 :
        print('C')
    elif score >= 45 and score <= 49 :
        print('D')
    elif score >= 40 and score <= 44 :
        print('E')
    elif score >= 0 and score <= 39:
        print('F')
    else :
        print('error') 

def simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    print(simple_interest)

def get_month_name(month):
    month_names = [
        'JANUARY',
        'FEBRUARY',
        'MARCH',
        'APRIL',
        'MAY',
        'JUNE',
        'JULY',
        'AUGUST',
        'SEPTEMBER',
        'OCTOBER',
        'NOVEMBER',
        'DECEMBER'
    ]
    return month_names[int(month) - 1]

def change_date(input_date):
    content = input_date.split('/')
    print(content)
    print(content[0] + ' ' + get_month_name(content[1]) + ' ' + content[2])
 
#print(x)
#execute(-200)
#simple_interest(760000, 10.6, 0.5)
#change_date('9/10/2020')

account = BankAccount('Mayokun Oke', '2122500103', '387247272092', 100000)
print('Account Name: ', account.get_account_name())
print('Account Number: ', account.get_account_number())
print('BVN:', account.get_bvn())
print('Balance:',account.get_balance())
account.deposit(23500)
print('Balance:',account.get_balance())
account.withdraw(500000)
#account.withdraw(123000)

pupil = Student('Mayokun Oke', 'Female', 'PDS/APP/1999079', 'Engineering')
pupil.add_subject("Mathematics")
pupil.add_subject("English")
pupil.add_subject("Chemistry")
pupil.add_subject("Physics")
print('Subject: ', pupil.get_subjects())