def classify(num):
    factors = []

    for i in range(1, num):
        if num % i == 0:
            factors.append(i)

    if sum(factors) > num:
        return 'abundant'
    elif sum(factors) < num:
        return 'deficient'
    return 'perfect'

def listInRange(start, end, aliquot):

    aliList = []

    for i in range(start, end + 1):
        if classify(i) == aliquot:
            aliList.append(i)

    if aliList == []:
        return 'There are no ' + str(aliquot) + ' numbers in this range'
    return ', '.join(map(str, aliList))
