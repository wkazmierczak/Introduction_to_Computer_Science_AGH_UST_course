def multi(T):
    best = 0
    for word in T:
        l = len(word)

        if l < 2:
            continue

        div = l - 1
        while div > 0:
            if l % div == 0:
                corr = True
                for i in range(l):
                    if word[i] != word[i % div]:
                        corr = False
                        break
                if corr:
                    break
            div -= 1

        if corr:
            if best < l:
                best = l
    return best


if __name__ == '__main__':
    T = ["AAAA", "ABCABCABC", "ADEFADEGADEF"]
    print(multi(T))