file1 = open("a_example.txt",'r')
output = []
x="x"
while x!="":
    x=file1.readline()
    output.append(x)

file1.close()
print(output)

