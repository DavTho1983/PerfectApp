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

    if aliquot == 'Abundant':
        aliStr = 'abundant'
    elif aliquot == 'perfect':
        aliStr = 'perfect'
    else:
        aliStr = 'deficient'

    aliList = []

    for i in range(start, end):
        if classify(i) == aliStr:
            aliList.append(i)

    if aliList == []:
        return 'There are no ' + ' aliStr ' + ' numbers in this range'
    return ', '.join(map(str, aliList))
