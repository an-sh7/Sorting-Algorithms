def main():
    list = [34,52,41,31,643,24]
    n = len(list)

    for i in range(n-1):
        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    for i in range(n):
        print(list[i])

main()