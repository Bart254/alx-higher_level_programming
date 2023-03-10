#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    for e in range(len(sys.argv)):
        if e != 0:
            total += int(sys.argv[e])
    print(f'{total}')
