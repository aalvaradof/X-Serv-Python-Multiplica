#!/usr/bin/python3

import sys
from sys import argv

def help():
    print('Usage: calculadora.py function op1 op2')
    print('Possible functions: sumar restar multiplicar dividir')

N_ARGS = 4

if len(sys.argv) != N_ARGS:
	sys.exit("Invalid number of arguments")

func = argv[1]
op1 = argv[2]
op2 = argv[3]

try:
    op1 = float(op1)
    op2 = float(op2)
except ValueError:
    help()
    sys.exit("Introduced not numeric arguments")

if func == 'sumar':
    print(op1 + op2)
elif func == 'restar':
    print(op1 - op2)
elif func == 'multiplicar':
    print(op1 * op2)
elif func == 'dividir':
    try:
        print(op1 / op2)
    except ZeroDivisionError:
        print("Cannot divide by 0")
else:
	sys.exit("Invalid operation")
	

