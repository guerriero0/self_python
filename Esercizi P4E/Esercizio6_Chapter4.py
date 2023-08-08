def computepay(hours, rate):
    pay = hours*rate
    pay_alt = hours*rate + (hours-40)*rate*1.5
    if hours <= 40 and hours >= 0:
        return print(pay)
    elif hours > 40:
        return print(pay_alt)
    elif (hours or rate) < 0:
        return print('Enter a positive value!')

computepay(40,30)


