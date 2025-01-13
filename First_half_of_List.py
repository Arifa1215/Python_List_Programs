n=input().split()
len_n = len(n)
if len_n%2==0:
    word_length = len_n//2 
else:
    word_length = (len_n // 2 ) +1

print(n[:word_length])
