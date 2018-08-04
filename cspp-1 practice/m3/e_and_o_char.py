'''
@author : nandakishore723
'''
S = input()
L = len(S)
E = ''
O = ''
I = 0
J = 1
NEW = ""
VEW = ""
ADD = ""
while I <= L - 1:
    E = S[I]
    NEW = NEW+E
    I += 2
    while J <= L - 1:
        O = S[J]
        VEW = VEW+O
        J += 2
ADD = NEW+ '  ' +VEW
print(ADD)
