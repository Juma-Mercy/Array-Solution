#initialize Array, N , including its elements
N = {0: 100000}
A = [{-2, 147, 483, 648}, {-1, 147, 483, 648}, {0, 147, 483, 648}, {1, 147, 483, 648}, {2, 147, 483, 647}]

#function for calculating the denominator of array A (elements)

def assumptionFunction(A):
    lenth = len(A)
    half = lenth / 2
    my_dict = {lenth: A}

    #dictionary obtaining the keys and values
    #use for loop to loop in the number of integers
    for n in N:
        #use if condition to compare the indexes
        if n > half:
            n = n+1
            print(n)
        else:
            #if target is not achivd, initialize the index n to -1
            n = n - 1
            #print the results of the indexes
        print(n)



















