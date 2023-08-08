def computergrade(score):
    try:
        if score <= 1 and score > 0:
            if(score >= 0.9):
                return print('A')
            elif(score >= 0.8):
                return print('B')
            elif(score >= 0.7):
                return print('C')
            elif(score >= 0.6):
                return print('D')
            elif(score < 0.6 and score > 0):
                return print('F')
        else:
            return print('Enter a positive value between 0 and 1!')
    except:
        return print('ERROR')

computergrade(-0.86)