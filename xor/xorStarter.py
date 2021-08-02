    

string = "label"
solution = ""

for c in string:
    solution+=chr(ord(c) ^ 13)

print(f'[*] FLAG: {solution}')