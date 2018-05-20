mytab = [15, 25, 14, 2, 7, 34, 75, 84, 13, 42, 1337, 546, 128, 1024, 512, 745, 16, 64 ]

def bubleProcess(tab) :
    sorted = True
    
    for i in range(len(tab) -1) :
        if tab[i] > tab[i+1] :
            sorted = False
            tab[i], tab[i+1] = tab[i+1], tab[i]
            
    return sorted
    
def bubleSort(tab):
    
    
    sorted = bubleProcess(tab)
    
    while not sorted :
        sorted = bubleProcess(tab)


def smallestSwap(tab, step):
    biggest = step
  
    for i in range(len(tab) - step):
        if tab[i] > tab[biggest] :
            smallest = i
     
    
    tab[len(tab)-step - 1], tab[smallest] = tab[smallest], tab[len(tab)-step -1 ]
    print(tab[step:])

def insertSort(tab):
    
    step =0
    while len(tab)-step > 1:
        smallestSwap(tab, step)
        print(tab)
        step += 1
        
def split(tab):
    length = len(tab)
    
    if length > 1 :
        key = length//2
        t1 = tab[:key]
        t2 = tab[key:]
        
        return (t1, t2)


def merge(t1, t2):
    res = []
    i = 0
    j = 0
    
    print("t1 :", t1)
    print("t2 : ", t2)
    
    while i < len(t1) and j<len(t2) :
        if t1[i] < t2[j] :
            res.append(t1[i])
            i+=1
        else:
            res.append(t2[j])
            j+=1
            
    res.extend(t2[j:])
    res.extend(t1[i:])
    
    return res
        
        
def merge_sort(tab):
    if len(tab) <= 1:
        return tab
        
    tabs = split(tab)
    
    return merge(merge_sort(tabs[0]), merge_sort(tabs[1]))
    
    
def part(tab, left, right):
    pivot = tab[left]
    i = left + 1
    j = right
    
    while i<= j:
    
        while i <= right and tab[i] <= pivot :
            i+=1
        
        while tab[j] > pivot :
            j -= 1
        
        if i < j :
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j -= 1
            
    tab[left], tab[j] = tab[j], tab[left]
    
    return j
        
    
 
 
def quickSortProcess(tab, left, right):
    
    if left < right :
        
        tmp = part(tab, left, right)
    
        quickSortProcess(tab, left, tmp-1)
        quickSortProcess(tab, tmp+1, right)
    
    
def quickSort(tab):
    quickSortProcess(tab, 0, len(tab)-1)
    
    
    #print(tab)
#    if len(tab) > 1 :
        
#        left = 1
#        right = len(tab)-1
#        pivot = tab[0]
        
        
        
#        while left <= right :
            
#            print("Comparing : ", tab[left], " to pivot ", pivot)
#            if tab[left] > pivot :
                
                
#                tab[left], tab[right] = tab[right], tab[left]
                
                
#                right -= 1
                
#            else :    
#                left+=1
                
            #print("left : ", left, " step : ", step)
        
        
#        print(tab)
#        tab[0], tab[left-1] = tab[left-1], tab[0]
#        print(tab)
        
#        tab1 = tab[:left]
        #print("tab1 : ", tab1)
#        tab2 = tab[left+1:]
        #print("tab2 : ", tab2)
        
#        if len(tab1) != len(tab) and  len(tab2) != len(tab):
        
        
#            quickSort(tab1)
            #quickSort(tab2)
        
            
            #tab = tab1[:]
#            tab.append(pivot)
#            tab.extend(tab2)
       
    
       
                
        
    

    