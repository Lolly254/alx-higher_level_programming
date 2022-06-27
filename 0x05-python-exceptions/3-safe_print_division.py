#!/usr/bin/python3

def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except:
        return None
    finally:
        print('Inside result:{:f}'.format(result))
        print('{:d} / {:d} = {:f}'.fomrat(a, b, result))
