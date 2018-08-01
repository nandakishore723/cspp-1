'''
 @author : nandakishore
 This Program helps to compare the variable and print among the
 avariable.
'''
VARA = 5
VARB = 7
if VARA > VARB:
    print('Greater')
elif VARA < VARB:
    print('Smaller')
elif VARA == VARB:
    print('equal')
elif (isinstance(VARA) == str) or (isinstance(VARB) == str):
    print('strings involved')
