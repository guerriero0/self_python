try:
    hours = int(input('Enter Hours: '))
    rate = round(float(input('Enter Rate: ')), 2)
    if hours <= 40 and hours > 0:
        print(f'Pay: {hours*rate}')
    else:
        print(f'Pay: {hours*rate + (hours-40)*rate*1.5}')
except:
    print('Error, please enter numeric input')