'''
@author : nandakishore723
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    str_output = ''
    for _ in str_input:
    	if _ in '!@#$%^&*':
    		str_output += " "
    	else:
    		str_output += _ 
    print(str_output)
    #print(str_input.Replace("!, @, #, $, %, ^, &, *", " "))
if __name__ == "__main__":
    main()
