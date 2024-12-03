def isIsomorphic(s: str, t: str):
    wrong=-1
    count_s=[]
    count_t = []
    curr = s[0]
    curr_count=1
    curr_t=t[0]
    curr_t_count=1
    for a in range(1,len(s)):
        # print(curr,'curr_s',s[a],'curr_value_s')
        if s[a]==curr:
            curr_count+=1
        else:
            count_s.append(curr_count)
            curr=s[a]
            curr_count=1
        if t[a]==curr_t :
            curr_t_count+=1
        else:
            count_t.append(curr_t_count)
            curr_t=t[a]
            curr_t_count=1
    # print(count_t,'t''\n',count_s,'s')
    check_for_single_mapping={}
    if count_s==count_t:
        for k in range(len(s)):
            if s[k] in check_for_single_mapping:
                if check_for_single_mapping[s[k]]!=t[k]:
                    wrong+=1
                    break
            elif t[k] in check_for_single_mapping.values():
                wrong += 1
                break
            else:
                check_for_single_mapping[s[k]]=t[k]
    else:
        wrong += 1

    if wrong<0:
        return True
    else:
        return False

print(isIsomorphic('badc','baba'))


