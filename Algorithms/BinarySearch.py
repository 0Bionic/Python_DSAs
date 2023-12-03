from BubbleSort import BubbleSort

List = [1,123,412,4,23,12,63,74,34]

def BinarySearch(ValueToFind, List):
    SortedList = BubbleSort(List)
    UpperBound = len(List) - 1
    LowerBound = 0
    Found = False

    while LowerBound <= UpperBound and not Found:
        Mid = (LowerBound + UpperBound) // 2
        if ValueToFind == SortedList[Mid]:
            Found = True
            return Mid
        elif ValueToFind > SortedList[Mid]:
            LowerBound = Mid + 1
        elif ValueToFind < SortedList[Mid]:
            UpperBound = Mid - 1
  
    return -1