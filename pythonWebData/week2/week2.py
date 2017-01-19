import os
import re

testfile = open('D:\/regex_sum_238824.txt', 'r')
total_number = []

for line in testfile:
    number_array = re.findall('[0-9]+', line)
    if len(number_array) > 0:
        total_number = total_number + number_array
    else:
        continue
total_sum_number = 0
for numbers in total_number:
    total_sum_number = total_sum_number + int(numbers)

print total_sum_number