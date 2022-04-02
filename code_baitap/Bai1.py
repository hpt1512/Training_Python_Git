print('Bai1')

def numJewelsInStones(jewels, stones):
    dem = 0
    for i in jewels:
        for j in stones:
            if i == j :
                dem = dem + 1
    return dem
      
   
print('Nhap jewels: ')
jewels = input()
print('Nhap stones: ')
stones = input()      

print(numJewelsInStones(jewels,stones))