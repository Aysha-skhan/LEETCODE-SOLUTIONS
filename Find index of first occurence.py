def strStr(haystack: str, needle: str) -> int:
    if len(haystack) == len(needle):
        if haystack == needle:
            return 0
        else:
            return -1
    else:
        for k in range(len(haystack)):
            if haystack[k] == needle[0]:
                z = k + 1
                for y in range(1, len(needle)):
                    if z >= len(haystack) or haystack[z] != needle[y]:
                        break
                    z += 1
                # print(z)
                if z == (k + len(needle)):
                    return k
        return -1

print(strStr('sad23','sad'))