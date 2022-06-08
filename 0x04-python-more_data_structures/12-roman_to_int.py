#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == "" or type(roman_string) is not str:
        return(0)
    else:
        r_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        val = 0
        for i in range(len(roman_string)):
            if i > 0 and r_n[roman_string[i]] > r_n[roman_string[i - 1]]:
                val += r_n[roman_string[i]] - 2 * r_n[roman_string[i - 1]]
            else:
                val += r_n[roman_string[i]]
        return (val)
