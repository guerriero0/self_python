print(5==5)
print(6==5)

print(type(True))
print(3%2==0)

# Conditional execution
x = 5
if x > 0:
    print(f'{x} is positive')


# Alternative execution
y = 6
if y < 0:
    print(f'{y} is negative')
else:
    pass

if x % 2 == 0:
    print('x is even')
else :
    print('x is odd')

# Chained Conditionals
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

# Nested Conditionals
x = input(f'Please enter your gender: ')
if x == 'Male':
    x_m = input(f'Do you like football? ')
    if x_m == 'Yes':
        print('You are cool!')
    else:
        print('You are an idiot!')
elif x =='Female':
    x_f = input(f'Do you like dance? ')
    if x_f == 'Yes':
        print(f'You are cool!')
    else:
        print(f'You are an idiot!')
elif x == 'None':
    print(f'You are fucked!')
else:
    print(f'ERROR, PLEASE ENTER Male,Female OR None!')








