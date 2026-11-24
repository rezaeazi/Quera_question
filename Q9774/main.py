number_str = input().strip()

for char in number_str:
    
    digit = int(char)
    
    print(f"{char}: {char * digit}")