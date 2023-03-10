#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_args = len(sys.argv)
    if total_args == 1:
        print(f'{total_args - 1} arguments.')
    elif total_args == 2:
        print(f'{total_args - 1} argument:')
        print("1: {}".format(sys.argv[1]))
    else:
        print(f'{total_args - 1} arguments:')
        for e in range(total_args):
            if e != 0:
                print("{}: {}".format(e, sys.argv[e]))
