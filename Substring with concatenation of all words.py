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
# a=[1,2,3,4,5]
# for k in range(len(a)-1):
#     b=a[k:k+2]
#     print(b)


# def findSubstring(s, words):
#     d={}
#     # dictionary creation to store count of words
#     for y in range(len(words)):
#         if words[y] not in d:
#             d[words[y]]=1
#         else:
#             d[words[y]]+=1
#     chkk=len(words[0])
#     segmented=[]
#     done=-1
#     for g in range(len(s)-(chkk-1)):
#         subb=s[g:g+chkk]
#         if subb in d:
#             if done<g-1:
#                 segmented.append(s[done+1:g])
#                 print('first',s[done+1:g-1],'done = ',done)
#                 done=(g+chkk)-1
#                 segmented.append(s[g:g+chkk])
#                 print('second',s[g:g+chkk],'done = ',done)
#             elif done==g-1:
#                 done = (g + chkk) - 1
#                 segmented.append(s[g:g + chkk])
#                 print('third', s[g:g + chkk],'done = ',done)
#
#     chkk2=len(words)
#     sub_string_count=[]
#     position=0
#     for a in range(len(segmented)-(chkk2-1)):
#         check_substring=segmented[a:a+chkk2]
#         count_all_words=0
#         for b in range(len(check_substring)):
#             if check_substring[b] not in d:
#                 break
#             else:
#                 if check_substring.count(check_substring[b])==d[check_substring[b]]:
#                     count_all_words+=1
#         if count_all_words==len(words):
#             sub_string_count.append(position)
#         position+=len(check_substring[0])
#         # print(position,'val')
#
#
#     return sub_string_count,segmented

# -----------------------------------------------------------------------------------
# def findSubstring(s, words):
#     d={}
#     # dictionary creation to store count of words
#     for y in range(len(words)):
#         if words[y] not in d:
#             d[words[y]]=1
#         else:
#             d[words[y]]+=1
#     count=0
#     start=-1
#     indexes=[]
#     print(len(words[0])*len(words),'checlll')
#     for m in range(len(s)-(len(words[0]))):
#         sub=s[m:m+(len(words[0]))]
#         print(sub,m,'-',m+(len(words[0])-1))
#         if sub in d:
#             # print(sub, m, '-', m + (len(words[0]) - 1))
#             count+=1
#             if start==-1:
#                 start=m
#         elif sub not in d and m+(len(words[0])-1)>=(start + (len(words[0])*len(words))-1):
#             count=0
#             start=-1
#         print(count, 'count','\nstart: ',start,'m: ',m+(len(words[0])-1))
#         if count==len(words):
#             # print(sub, m, '-', m + (len(words[0]) - 1))
#             indexes.append(start)
#             count=1
#             start=m
#     return indexes
