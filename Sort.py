def sort(array):
    if len(array) <= 5:
        return insertionSort(array)
    else:
        return sort([x for x in array[1:] if x < array[0]]) + [array[0]] + sort([x for x in array[1:] if x >= array[0]])

def insertionSort(L):
	for i in range(len(L)-1):
		for j in range(i+1,len(L)):
			if L[j] < L[i]:
				L[i], L[j] = L[j], L[i]
	return L
