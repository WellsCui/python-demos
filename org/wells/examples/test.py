def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    size = len(states)
    def getStates(index):
        if index == 0:
            if states[1] == 0:
                return 0
            else:
                return 1
        if index == size-1:
            if states[size-2] == 0:
                return 0
            else:
                return 1
        if (states[index-1] == 0 and states[index+1] == 0 ) or (states[index-1] == 1 and states[index+1] == 1 ):
            return 0
        else:
            return 1

    for day in range(days):
        states = [getStates(index) for index in range(size)]
    return states



def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    def getFactors(n):
        fs = []
        for i in range(1, n):
            print(i)
            if (n % i) == 0:
                fs.append(i)
        fs.sort()

        return fs

    factors = getFactors(arr[0])
    print(factors)


    for item in arr:
        while len(factors)> 0:
            if (item % factors[-1]) == 0:
                break
            else:
                factors.pop()

    return factors[-1]


print(generalizedGCD(4, [2,4,6,8]))
