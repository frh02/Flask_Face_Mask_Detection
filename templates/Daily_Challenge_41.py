def sum_subset(lst,k):
    k = int(input())
    sum_sub = []
    for i in range(len(lst)):
        if sum(sum_sub) != k:
            sum_sub.append(lst[i])
    return sum_sub

