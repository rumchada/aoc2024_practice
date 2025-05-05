#mul(X,Y) X, Y= 1-3 digit numbers
# mul(44,46) 44 *46 --> 2024
# mul (123,4)  --> 123*44
# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# only mul(2,4), mul(5,5), mul(11,8) , mul(8,5)

# function clean mul
# input the string
# output is a list of mul commands

# function parse mul commands
# a list of mul commands
# output result of mul()

import re
file = "C:/Users/gdtbo/aoc2024_practice/data/mul_data.txt"
mul_string = ""
with open(file, "r") as file:
    for line in file:
        mul_string = mul_string + line

def mul_finder(mul_string):
    mul_list = re.findall(r"mul\(\d+,\d+\)",mul_string)
    mul_list = [eval(i.strip("mul")) for i in mul_list]
    result_list = sum([set[1] * set[0] for set in mul_list])
    return result_list

print(mul_finder(mul_string))
