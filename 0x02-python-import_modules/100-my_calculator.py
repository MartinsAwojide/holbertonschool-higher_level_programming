#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        var = int(argv[1])
        var2 = int(argv[3])
        if argv[2] == '+':
            print("{:d} + {:d} = {:d}".format(var, var2, add(var, var2)))
        elif argv[2] == '-':
            print("{:d} - {:d} = {:d}".format(var, var2, sub(var, var2)))
        elif argv[2] == '*':
            print("{:d} * {:d} = {:d}".format(var, var2, mul(var, var2)))
        elif argv[2] == '/':
            print("{:d} / {:d} = {:d}".format(var, var2, div(var, var2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
