# CodeEval: https://www.codeeval.com/open_challenges/18/ 

import os

#print(os.path.dirname(os.path.realpath(__file__)))
#print(os.getcwd())
#print(os.path.realpath(__file__))

filepath = os.path.dirname(os.path.realpath(__file__)) + "/" + "multiples_of_a_number.txt"

numbers = open(filepath , "r")
lines = numbers.readlines()
numbers.close()

print(lines)

for i in range(0,len(lines)):
    currentLine = lines[i].strip(' \t\n\r')
    
    print(currentLine)
    
    xstr, nstr = currentLine.split(",", 2)
    
    print("x = " + xstr)
    print("n = " + nstr)

    x = float(xstr)
    n = float(nstr)

    result = int((int((x - 1) / n ) + 1) * n)
    
    print("Result: " + result.__str__())
