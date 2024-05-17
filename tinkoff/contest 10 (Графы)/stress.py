from os import popen

one = popen("python3 hello.py").read()

print(one)
