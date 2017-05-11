tab = [15, 25, 14, 2, 7, 34, 75, 84, 13, 42, 1337, 546, 128, 1024, 512, 745, 16, 64 ]
tab.sort()

tab2=[1,2, 3, 4, 5]

def find(t, elem, start, end):
    mid = (start + end)//2
    
    print(str(start) + " " + str(end)) 
    
    if (end - start) <= 1:
        return False
        
    else:
        if t[mid] == elem:
            return True
        else:
            if t[mid] > elem:
                return find(t, elem, start, mid)
            else:
                return find(t, elem, mid, end)
                

print(find(tab, 3, 0, len(tab)-1))