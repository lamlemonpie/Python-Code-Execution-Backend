import sys
import io

def executer(code):
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    exec(code)

    output = new_stdout.getvalue()

    sys.stdout = old_stdout
    return output


code = '''
for i in range(0,10):
    print(i)
'''


