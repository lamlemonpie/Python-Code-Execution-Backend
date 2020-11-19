import sys
import io

def executer(code):
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    exec(code, globals(), globals())

    output = new_stdout.getvalue()

    sys.stdout = old_stdout
    return output
