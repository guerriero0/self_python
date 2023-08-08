try:
    temp_c = float(input('Enter Celsius temperature: '))
    temp_f = (temp_c * (9/5)) + 32
    print(f'This is the Fahrenheit temperature: {temp_f}')
    print(type(temp_f))
except:
    print('Please enter a number.')



