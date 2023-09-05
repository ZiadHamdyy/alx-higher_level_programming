#!/usr/bin/python3
my_range = range(97, 123)
output_string = ""
for ascii_value in my_range:
    output_string += f"{chr(ascii_value):s}"

print(output_string, end = "")
