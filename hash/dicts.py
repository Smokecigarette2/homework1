def check_anagrams(w1, w2):
    dict = {}
    dict2 = {}
    for i in w1:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for j in w2:
        if j in dict2:
            dict2[j] +=1
        else:
            dict2[j] = 1

    return dict == dict2

print(check_anagrams("hello", "world"))


def find_common(text):
    dict = {}
    for i in text:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for j in dict:
        most_common = j
        for k in dict:
            if dict[k] > dict[j]:
                most_common = k

    return most_common

print(find_common(""))
