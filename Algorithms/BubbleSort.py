List = [1,123,412,4,23,12,63,74,34]

def BubbleSort(List):
    #Sorts the List in the parameter using Bubble Sort
    x = -1
    for each in List:
        x = x+1

    while x>=0:
        i = 0
        while i < x:
            if List[i] > List[i+1]:
                temp = List[i]
                List[i] = List[i+1]
                List[i+1] = temp
            i = i+1
        x = x - 1
    return List