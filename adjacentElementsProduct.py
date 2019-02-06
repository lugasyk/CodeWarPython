def adjacentElementsProduct(inputArray):
    prev = inputArray[0]
    product = prev * inputArray[1]
    for i in inputArray[1::]:
        if (prev * i > product):
            product = prev * i

        prev = i
    else:
        return product