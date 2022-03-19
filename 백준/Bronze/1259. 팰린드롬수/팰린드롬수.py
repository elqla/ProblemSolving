while 1:
    word = input()
    res = 'yes'
    if word == '0':
        break
    l = len(word)
    for i in range(l//2):
        if word[i]!=word[l-i-1]:
            res = 'no'
        else:
            continue

    print(res)