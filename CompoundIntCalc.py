# python compound interest calculator

principal = 0
rate = 0
time = 0

while principal <=0:
    principal = float(input(f'Enter the principal amount: '))
    if principal <=0:
        print('Principal can not be less than or equal to zero')

while rate <= 0:
    rate = float(input('Enter the interest rate: '))
    if rate <=0:
        print('Interest rate can not be less than or equal to zero')

while time <= 0:
    time = int(input('Enter the time in years: '))
    if time <=0:
        print('Time can not be less than or equal to zero')

total = principal * pow((1 + rate / 100), time)
print (f'Balance after {time} year/s: {total: ,.2f}')
