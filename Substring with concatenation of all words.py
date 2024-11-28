def findSubstring(s, words):
    d={}
    # dictionary of words
    for y in range(len(words)):
        if words[y] not in d:
            d[words[y]]=1
        else:
            d[words[y]]+=1
    d2=d.copy()
    indexes=[]
    word_length=len(words[0])
    # print((len(words))*word_length)
    for a in range(len(s)):
        # print()
        if a+(word_length*len(words))<=len(s):
            # print(a+(word_length*len(words)))
            curr=s[a:a+(word_length*len(words))]
            # print(s[a:a+(word_length*len(words))])
            start=0
            for b in range(len(words)):
                segment=curr[start:start+word_length]
                if segment in d:
                    d[segment]-=1
                start=start+word_length
            # print(d)
            if all(v==0 for v in d.values()):
                indexes.append(a)
            d = d2.copy()

    return indexes


# print(findSubstring("aaaaaaaaaaaaaa",["aa","aa"]))
# print(findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))
print(findSubstring("barfoothefoobarman",["foo","bar"]))



