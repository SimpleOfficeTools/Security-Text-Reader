from runpy import run_path


print("THANK YOU FOR USEING PyPRINT, THE SECURE WAY TO VIEW ANY TEXT FILE                                                                                                              ")
lines = []
with open('Readthis.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    print(f'line {count}: {line}')
    
run_path('System file1.py')
