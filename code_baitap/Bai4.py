print('Bai4')

candies = [12,1,12]
extraCandies = 10



def kidsWithCandies(candies, extraCandies):
    kq = []
    max = candies[0]
    for i in candies:
        if i > max:
            max = i
    for i in candies:
        if i+extraCandies >= max:
            kq.append(True)
        else:
            kq.append(False)
    return kq

print(kidsWithCandies(candies, extraCandies))    

