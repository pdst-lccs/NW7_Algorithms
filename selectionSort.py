# Initialise an unsorted list
the_list = [9, 6, 10, 4, 8, 5, 7]
print("Unsorted:", the_list)

# Traverse through all list elements
for i in range(len(the_list)):
    # Find the minimum element to the right of the current element
    index_of_min = i
    for j in range(index_of_min+1, len(the_list)): 
        if the_list[j] < the_list[index_of_min]:
            index_of_min = j

    # Exchange the smallest element with the current element
    temp = the_list[i] # save the current element
    the_list[i] = the_list[index_of_min] # copy 1
    the_list[index_of_min] = temp # copy 2
    
# Display the sorted list
print("Sorted:", the_list)
