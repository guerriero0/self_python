str = 'X-DSPAM-Confidence:0.8475'

print(str.find(':'))
x = float(str[19:])
print(x)

str = str.replace(':','-')
print(str)
