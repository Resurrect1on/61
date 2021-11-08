def rot(num):
    if '6' in num:
        i = num.index('6')
        num[i] = 9
        print(''.join(map(str,num)))
    else:
        print(''.join(map(str,num)))

ch = list(input())
rot(ch)