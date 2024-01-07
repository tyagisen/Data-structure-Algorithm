def merge_sorted_array(arr1, arr2):
    sorted_array = []
    i = 0
    j=0
    flag =0
    # check if either one of the array is empty.
    if len(arr1)==0:
        return arr2
    elif len(arr2)==0:
        return arr1
    while i < len(arr1) and j < len(arr2):
        if (arr1[i]<=arr2[j]):
            sorted_array.append(arr1[i])
            i+=1
        else:
            sorted_array.append(arr2[j])
            j+=1
        if i==len(arr1):
            flag=1
    
    if flag==1:
        # for item in arr2[j:]:
        #     sorted_array.append(item)
        sorted_array.extend(iter(arr2[j:]))
    else:
        # for item in arr1[i:]:
        #     sorted_array.append(item)
        sorted_array.extend(iter(arr1[i:]))
    return sorted_array


print(merge_sorted_array([1,3,12], [2, 4,6]))