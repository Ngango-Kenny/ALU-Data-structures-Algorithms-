#!/usr/bin/python3
import os

def is_integer(value):
    try:
        int(value)
        return True
    except Exception:
        return False
    
input_dir = os.getcwd()+'\hw01\sample_inputs'
output_dir = os.getcwd()+'\hw01\sample_results'

# Iterate through files in the target directory
for filename in os.listdir(input_dir):
    file_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, f"{filename}_results.txt")
    
    with(open(file_path, 'r') as file):
        file_lines = file.readlines()
        my_dict = {}
        unique = []  
        for num in file_lines:
            num = num.strip()
            if not is_integer(num):
                continue

            if int(num) not in range(-1023, 1024):
                continue

            if num in my_dict.keys():
                my_dict[num] += 1
            else:    
                my_dict[num] = 1

        print(my_dict)        

        for key in my_dict.keys():
            if my_dict[key] == 1:
                unique.append(key)

        with(open(output_path, 'w') as output_file):
            for num in unique:
                output_file.write(num)
                output_file.write('\n')
