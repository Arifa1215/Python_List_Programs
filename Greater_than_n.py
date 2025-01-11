num_list = [1, 6, 32, 93, 71, -20, 30, -90, 50] 
list_1 = []
n=int(input())
for i in num_list:
    if i>n:
        list_1 = list_1 + [i]
print(list_1)