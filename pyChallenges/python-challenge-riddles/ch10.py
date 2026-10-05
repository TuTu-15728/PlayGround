#!/usr/bin/env python3

import requests

# url = "http://www.pythonchallenge.com/pc/return/bull.html"
auth = ('huge', 'file')
# res = requests.get(url, auth=auth)

# print(res.text)
print("+"*70)

url_2 = "http://www.pythonchallenge.com/pc/return/sequence.txt"
res_2 = requests.get(url_2, auth=auth)

print(res_2.text)
print("+"*70)


# Look and Say (COPIED)

def count_and_say(n):
    if n == 1:
        return "1"

    ret = ""
    str_to_count = count_and_say(n - 1)
    stack = []

    for i in range(len(str_to_count) + 1):
        if i == len(str_to_count) or (stack and stack[-1] != str_to_count[i]):
            to_add = str(len(stack)) + stack[-1]
            ret += to_add
            stack.clear()

        if i != len(str_to_count):
            stack.append(str_to_count[i])

    return ret


def main():
    n = 31
    print(len(count_and_say(n)))


if __name__ == "__main__":
    main()
