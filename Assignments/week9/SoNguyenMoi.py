n = input()
int_n = int(n)
mod = int_n % 3
list_n = list(n)

if mod == 0:
    tmp = 3
elif mod == 1:
    tmp = 2
else:
    tmp = 1
    
for i in range (len(list_n)):
    check = 0
    a = int(list_n[i]) + tmp
    
    if(a <= 9):
        check = 1
        while a <=9:
            check += 1 
            a += 3
    
    if check == 1:
        list_n[i] = str(a)
        break
    elif check > 1:
        list_n[i] = str(a - 3)
        break
    
n_2 = ''.join(list_n)

if (n != n_2):
    print(n_2)
else:
    list_n = list(n)
    if mod == 0:
        tmp = 3
    elif mod == 1:
        tmp = 1
    else:
        tmp = 2
    list_n[-1] = str(int(list_n[-1]) - tmp) 
    print(''.join(list_n))
    

        
