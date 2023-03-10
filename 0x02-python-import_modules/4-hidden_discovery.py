#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hidden_list = dir(hidden_4)
    for e in range(len(hidden_list)):
        if hidden_list[e][0] != '_' and hidden_list[e][1] != '_':
            print(f'{hidden_list[e]')
