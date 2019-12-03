'''
Mike Cao
9/20/18
Merchants.py Lab 3
'''

import collections
import sys
import time

Merchant = collections.namedtuple('Merchant', ('name', 'location'))

def reader(filename: str) -> list:
    '''
    Opens up the file and creates a tuple with the file data of merchants.

    :param filename: file of data (merchants and locations)
    :return: tuple of merchants and their locations
    '''
    merchants = list()
    with open(filename) as f:
        for line in f:
            profile = line.split(' ')
            merchants.append(Merchant(str(profile[0]), int(profile[1])))
    return merchants

def findOptimalLocation(merchants, t):
    '''
    Takes a sorted list of merchants and their locations and finds the optimal location which is the median of the list of numbers.
    If len(merchants) is even, return the average of the two numbers at the center.
    If odd, return the middle number.

    :param merchants: unsorted list of merchants and their location
    :return: sorted list of merchants based on location
    '''
    if t == 'merchant':
        return merchants[int((len(merchants))/2)]
    else:
        return int(merchants[int((len(merchants)) / 2)].location)
    #else:
        #return (int(merchants[int((len(merchants)/2)-1)].location) + int(merchants[int(len(merchants)/2)].location))/2

def distance(merchants, speed) -> int:
    '''
    Returns total distance to other locations from optimal location.
    :param merchants: list of merchants
    :param speed: slow or fast to use quick sort or quick seleck
    :return: total distance(int)
    '''
    tdis = 0
    if speed == 'slow':
        opdis = int(findOptimalLocation(quick_sort(merchants), 'int'))
        for x in merchants:
            tdis += abs(opdis - int(x.location))
        return tdis
    else:
        opdis = int(findOptimalLocation(quick_select(merchants, k = len(merchants)/2), 'int'))
        for x in merchants:
            tdis += abs(opdis - int(x.location))
        return tdis

def quick_sort(merchants):
    '''
    Performs the quick sort.
    :param merchants: list of merchants and their locations
    :return: sorted list of merchants
    '''
    smaller = []
    larger = []
    same = []
    if len(merchants) == 0:
        return []
    elif len(merchants) == 1:
        return merchants
    else:
        pivot = merchants[int(len(merchants) / 2)].location
        for x in merchants:
            if int(x.location) > int(pivot):
                larger.append(x)
            elif int(x.location) == int(pivot):
                same.append(x)
            else:
                smaller.append(x)
    return quick_sort(smaller) + same + quick_sort(larger)

def quick_select(merchants, k):
    '''
    Performs the quick select.
    :param merchants: list of merchants and their location
    :param k: index of median element
    :return: merchant in the optimal location
    '''
    smaller = []
    larger = []
    same = []
    if len(merchants) == 0:
        return []
    elif len(merchants) == 1:
        return merchants
    else:
        pivot = merchants[int(len(merchants) / 2)].location
        for x in merchants:
            if int(x.location) > int(pivot):
                larger.append(x)
            elif int(x.location) == int(pivot):
                same.append(x)
            else:
                smaller.append(x)
    m = len(smaller)
    count = len(merchants) - m - len(larger)
    if k >= m and k < m + count:
        return pivot
    elif m > k:
        return quick_select(smaller, k)
    else:
        return quick_select(larger, k - m - count)

def main() -> None:
    '''
    Inputs file name and calls functions. Prints search type, number of merchants, elapsed time, optimal store location, and sum of distances.
    '''
    sys.argv[0], sys.argv[1] = str(input("$ python3 merchants.py [slow|fast] input-file ")).split()
    assert sys.argv[0] == 'slow' or sys.argv[0] == 'fast'
    merchants = reader(sys.argv[1])
    if sys.argv[0] == 'slow':
        print("Search type: slow")
        print("Number of merchants: " + str(len(merchants)))
        start = time.clock()
        quick_sort(merchants)
        elapseds = time.clock() - start
        print("Elapsed time: " + str(elapseds) + " seconds")
        print("Optimal Store Location: " + str(findOptimalLocation(quick_sort(merchants), 'merchant')))
        print("Sum of distances: " + str(distance(merchants, sys.argv[0])))
    else:
        k = len(merchants)/2
        print("Search type: fast")
        print("Number of merchants: " + str(len(merchants)))
        start = time.clock()
        quick_select(merchants, k)
        elapsedf = time.clock() - start
        print("Elapsed time: " + str(elapsedf) + " seconds")
        print("Optimal Store Location: " + str(findOptimalLocation(quick_select(merchants, k), 'merchant')))
        print("Sum of distances: " + str(distance(merchants, sys.argv[0])))

if __name__ == '__main__':
    '''
    Calls main.
    '''
    main()
