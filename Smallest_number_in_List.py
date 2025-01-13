n=input().split()
smallest_number = 0 
for i in n:
    i=int(i)
    if i<smallest_number:
        smallest_number = i 

print(smallest_number)