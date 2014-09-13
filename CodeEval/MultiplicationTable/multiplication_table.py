# Multiplication Table: https://www.codeeval.com/open_challenges/23/

line = ""
for i in range(1,13):
    for j in range(1,13):
        line +=  ('{: >4}'.format(j * i))
      
    print(line)
    line = ""