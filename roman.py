rules = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def solution(roman):
    sum = 0
    for i, n in enumerate(roman):
        sign = 1
        if i < len(roman) - 1 and rules[n] < rules[roman[i + 1]]:
            sign = -1
        sum += rules[n] * sign

    return sum
    print sum

if __name__ == "__main__":
    solution("MCMXC")