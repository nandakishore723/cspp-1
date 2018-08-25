'''
@author : nandakishore723
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''
def freq_graph(dictionary):
    """frequency graph"""
    keys = sorted(dictionary.keys())
    for key in keys:
        var = ""
        for i in range(dictionary[key]):
            var += '#'
            i = i + 1
        print(key, '-', var)

def main():
    """main"""
    dictionary = eval(input())
    freq_graph(dictionary)

if __name__ == '__main__':
    main()
