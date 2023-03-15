#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None and type(roman_string) is str:
        roman_dict = {
                "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
                }
        numeral_list = []
        for char in roman_string:
            for key in roman_dict:
                if char == key:
                    is_roman = True
                    numeral_list.append(roman_dict[key])
                    break
                else:
                    is_roman = False
            if is_roman is False:
                return 0
        total = 0
        i = 0
        len_l = len(numeral_list)
        while i < len_l:
            if total < numeral_list[i]:
                total = numeral_list[i] - total
                i += 1
            elif i + 1 < len_l and numeral_list[i + 1] > numeral_list[i]:
                total += numeral_list[i + 1] - numeral_list[i]
                i += 2
            else:
                total += numeral_list[i]
                i += 1
        return total
    return 0
