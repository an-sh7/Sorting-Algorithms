def main():
    list = [2,54,82,34,25,62,343,1003]
    n = len(list)
    
    for i in range(1,n):
        key = list[i]
        j = i - 1

        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        
        list[j + 1] = key

    for i in range(n):
        print(list[i])     

main()