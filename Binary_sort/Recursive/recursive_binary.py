def recursive_binaruy_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binaruy_search(list[midpoint+1:], target)
            else:
                return recursive_binaruy_search(list[:midpoint], target)

def verify(result):
    print("Target found:",result)

list = [1,2,3,4,5,6,7,8,9]
result = recursive_binaruy_search(list, 7)
verify(result)  

result = result = recursive_binaruy_search(list, 6)
verify(result)