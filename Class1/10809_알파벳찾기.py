S = input()
alphabet = [-1]*26
for i in range(len(S)):
    if alphabet[ord(S[i])-ord('a')] == -1:
        alphabet[ord(S[i]) - ord('a')] = i

print(" ".join(map(str,alphabet)))
