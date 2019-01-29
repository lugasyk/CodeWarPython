from collections import Counter
def anagrams(word, words):
    result = []
    counter_word = Counter(word)
    for other_word in words:
        if Counter(other_word) == counter_word:
            result.append(other_word)
    return result