n=input().split()
divisible_by_3_list = []
for i in n:
    i=int(i)
    if i%3==0:
        divisible_by_3_list+=[i]
print(divisible_by_3_list)