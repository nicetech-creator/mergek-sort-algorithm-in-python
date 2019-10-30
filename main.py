#helper functions for radix sort
def countingSort(arr, exp1): 
    n = len(arr) 
    output = [0] * (n) 
    count = [0] * (10) 
    for i in range(0, n): 
        index = int((arr[i]/exp1)) 
        count[ (index)%10 ] += 1
    for i in range(1,10): 
        count[i] += count[i-1] 
    i = n-1
    while i>=0: 
        index = int((arr[i]/exp1)) 
        output[ count[ (index)%10 ] - 1] = arr[i] 
        count[ (index)%10 ] -= 1
        i -= 1
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 

def radixSort(arr): 
    max1 = max(arr) 
    exp = 1
    while max1/exp > 0: 
        countingSort(arr,exp) 
        exp *= 10

#helper functions for bucket sort
def bucket_sort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])
 
    for i in range(length):
        insertion_sort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp


#helper functions for merge-k sort
def mergesort(alist, blist):
    result = []
    while(len(alist) > 0 and len(blist) > 0):
        if(alist[0] <= blist[0]): result.append(alist.pop(0))
        else : result.append(blist.pop(0))
    result += alist
    result += blist
    return result

def kmerge(l, r):
    if l == r:
        return sub_data[l]
    if l + 1 == r:
        return mergesort(sub_data[l], sub_data[r])
    return mergesort(kmerge(l, (l + r) // 2), kmerge((l + r) // 2 + 1, r)) 

#helper function for checking sort result
def isSorted(alist):
    max = alist[0]
    for i in range(1, len(alist)):
        if alist[i] < max: return False
        max = alist[i]
    return True
#read data into an array
file = open('rand1000000.txt')
lines = file.readlines()
data = []
for line in lines:
    ws = line.split(' ')
    for w in ws:
        if len(w.strip()) > 0:
            data.append(int(w.strip()))
lines = []

#split data into 100 sub list
sub_data = [0] * 100
for i in range(100):
    sub_data[i] = data[i * 10000 : (i + 1) * 10000]

data = []

#sort 50 sub list using radix sort
for i in range(50):
    radixSort(sub_data[i])
    print ("radix sort - sub_data " + str(i))
for i in range(50, 100):
    sub_data[i] = bucket_sort(sub_data[i])
    print ("bucket sort - sub_data " + str(i))

data = kmerge(0, 99)
print(isSorted(data))
file.close()
