numc = [5, 6, 2, 1, 3, 4]

def bubble_sort(ls):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i+1], ls[i+1] = ls[i+1], ls[i]
                swapped = True


#bubble_sort(numc)
#print(numc)

def salection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if i in ls[j] < ls[lowest]:
                lowest = j
            ls[i], ls[lowest] = ls[lowest], ls[i]


salection_sort(numc)
print(numc)