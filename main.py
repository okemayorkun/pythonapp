def execute(score):
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

#execute(-200)

def simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    print(simple_interest)

#simple_interest(760000, 10.6, 0.5)

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

change_date('9/10/2020')