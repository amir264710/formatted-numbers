def format_number(num):
    formatedNum = ''

    for i in range(1, len(str(num))+1):
        formatedNum += str(num)[-i]
        if i%3 == 0:
            formatedNum += ','
    
    formatedNum=formatedNum[::-1]

    return formatedNum

print(format_number(4648461684964984694648646486))
