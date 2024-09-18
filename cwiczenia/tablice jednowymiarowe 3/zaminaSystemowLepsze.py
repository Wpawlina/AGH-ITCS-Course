def zamianaSys(num,sys):
    result=''
    while num!=0:
        digit=num%sys
        num=num//sys
        if digit >= 10:
            result=chr(ord('A')+digit-10)+result
        else:
            result = str(digit) + result
    return result

print(zamianaSys(239,16))
    