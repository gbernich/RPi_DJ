import subprocess

# subprocess.call(["ls", "-l"])

feedback = subprocess.check_output(["echo", "Hello World!"])

print feedback