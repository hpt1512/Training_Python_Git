print('Bai10')

def findComplement(num):
    st = []
    st2 = []
    while(num!=0):
        sd = num % 2
        st.append(sd)
        num = num // 2  
    for i in st:
        if i == 1:
            i = i - 1
        elif i == 0:
            i = i + 1 
        st2.append(i)   
    # nối chuỗi
    b = ''
    while(st2 != []):
        b = b + str(st2.pop())
    
    def BinToDec(binaryNumber):
        p = 0
        decNumber = 0
        while(binaryNumber > 0):
            decNumber = decNumber + (binaryNumber % 10) * pow(2, p)
            p = p + 1
            binaryNumber = binaryNumber // 10
        return decNumber

    return BinToDec(int(b))


print(findComplement(5))    