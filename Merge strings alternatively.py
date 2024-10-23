def mergeAlternately( word1: str, word2: str):
    fin = ''
    maxx = max(len(word1), len(word2))
    for k in range(maxx):
        if k <len(word1):
            fin += word1[k]
        if k <len(word2):
            fin += word2[k]
    return fin

