def checkPalindrome(inputString):
    inputString = inputString.casefold()
    rev_str = reversed(inputString)
    if list(inputString) == list(rev_str):
        return True
    else:
        return False