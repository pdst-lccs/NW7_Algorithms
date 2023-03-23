import random

def simple_selection_sort(L):
    swaps = 0
    comparisons = 0
     #print("Before: ", L)
    
 # Traverse over all list elements
    for i in range(len(L)):
        min_idx = i   # Find the minimum to the right of i
        for j in range(i+1, len(L)):
            comparisons = comparisons + 1
            if L[j] < L[min_idx]:
                min_idx = j

             # Swap minimum element with the current element
                L[i], L[min_idx] = L[min_idx], L[i]
                swaps = swaps + 1

        #print("After: ", L)
    print("N(%d), #Comparisons(%d),#Swaps(%d)"%(len(L),comparisons, swaps))
# Driver code ...
# ... run this code for a list sizes 5, 10, 100 and 1000
# ... run for already sorted, reversed and randomised lists
# ... record the #comparisons and #swaps in the manual
L = list(range(5)) # generate the ordered list
#L.reverse() # uncomment this line to reverse the list
random.shuffle(L) # uncomment this line to randomise the list
simple_selection_sort(L)