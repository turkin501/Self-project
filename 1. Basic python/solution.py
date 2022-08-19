def input_function():
    s = input('''Input operation of 2 large numbers \n(In case of subtraction the first number has to be higher than the second one)\n''')
    operation = min(x for x in s if x != '.')
    oppos = s.find(operation)
    return s[:oppos], s[oppos+1:], operation

def printnum(ditc):
    i = max(ditc)
    while i>=0:
        print(ditc[i], sep='', end='')
        i-=1
    if min(ditc)<0:
        j = min(ditc)
        while ditc[j]==0:
            #loai bo cac chu so 0 tan cung ben phai phan thap phan
            j+=1
        if j<0:
            print('.', sep='', end='')
        while i>=j:
            print(ditc[i], sep='', end='')
            i-=1

def get_digit(strdigit):
    ditc = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return ditc[strdigit]

def numstr_to_dict(numstr):
    if numstr.find('.'):
        dpos = numstr.find('.')
    else:
        dpos = len(numstr)
    ditc = {}
    
    level = 0
    for x in reversed(numstr[:dpos]): 
        #luu cac chu so nguyen vao ditc 
        ditc[level] = get_digit(x)
        level += 1
    
    level = -1
    for x in numstr[dpos+1:]: 
        #luu cac so thap phan vao ditc 
        ditc[level] = get_digit(x)
        level -= 1
    return ditc
    
def add(num1, num2):
    res = {}
    
    #dong nhat level bang cach them vao cac chu so 0
    num1 = num1 | {}.fromkeys([x for x in num2 if x not in num1], 0)
    num2 = num2 | {}.fromkeys([x for x in num1 if x not in num2], 0)        
    
    decimal = min(num1)
    intt = max(num1)
    carry = 0
    for i in range(decimal, intt+1):
        temp = num1[i] + num2[i] + carry
        res[i] = temp%10
        carry = temp//10
    
    if carry>0:
        res[intt+1] = carry
    return res

def subtract(num1, num2):
    '''Chi xu ly truong hop so thu nhat lon hon so thu hai'''
    res = {}
    
    #dong nhat level bang cach them vao cac chu so 0
    num1 = num1 | {}.fromkeys([x for x in num2 if x not in num1], 0)
    num2 = num2 | {}.fromkeys([x for x in num1 if x not in num2], 0)        
    
    decimal = min(num1)
    intt = max(num1)
    carry = 0
    for i in range(decimal, intt+1):
        if num1[i] < num2[i] + carry:
            temp = 10 + num1[i] - (num2[i] + carry)
            carry =1
        if num1[i] >= num2[i] + carry:
            temp = num1[i] - (num2[i] + carry)
        res[i] = temp
    
    if res[intt] == 0:
        res.pop(max(res))
    return res

def multiply(num1, num2):
    res = {}

    decimal = min(num1) + min(num2)
    intt = max(num1) + max(num2)
    carry = 0
    for i in range(decimal, intt+1):
        temp = 0
        for i1 in range(min(num1), max(num1)+1):
            i2 = i - i1
            if i2 in num2:
                temp += num1[i1] * num2[i2]
        temp += carry
        res[i] = temp%10
        carry = temp//10

    if carry>0:
        res[intt+1] = carry
    return res

def divide(num1, num2):
    pass

def run():
    numstr1, numstr2, operation = input_function()
    num1 = numstr_to_dict(numstr1)
    num2 = numstr_to_dict(numstr2)
    if operation == '+':
        res = add(num1,num2)
    if operation == '-':
        res = subtract(num1,num2)
    if operation == '*':
        res = multiply(num1,num2)
    if operation == '/':
        res = divide(num1,num2)
    printnum(res)


run()
   
