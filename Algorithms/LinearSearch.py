List = [1,123,412,4,23,12,63,74,34]


def LinearSearch(ValueToFind, List):
    # Returns the index of the value to be found in the List
    found = False
    count = 0
    while count != len(List) and found == False:
        if ValueToFind == List[count]:
            found = True
            return count
        else:
            found = False
        count = count + 1
    if found == False:
        return -1