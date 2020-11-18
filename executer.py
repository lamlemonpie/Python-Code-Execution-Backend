import sys

def executer(code,output):
    sys.stdout = open(output, "w")
    exec(code)
    sys.stdout.close()


code = '''
for i in range(0,10):
    print(i)
'''
output = "output.txt"

executer(code, output)

