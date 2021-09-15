music = list(map(int,input().split()))
if music==sorted(music):
    print('ascending')
elif music==sorted(music,reverse=True):
    print('descending')
else:
    print('mixed')

# res = ''
# for i in range(len(music)-1):
#     if res == '':
#         if music[i]>music[i+1]:
#             res='descending'
#         elif music[i]<music[i+1]:
#             res='ascending'
#         else:
#             res=''
#     elif res == 'ascending':
#         if music[i]>music[i+1]:
#             res='mixed'
#             break
#         elif music[i]<=music[i+1]:
#             res='ascending'
#     elif res == 'descending':
#         if music[i]>music[i+1]:
#             res = 'descending'
#         elif music[i]<=music[i+1]:
#             res = 'mixed'
#             break
#     else:
#         res='mixed'
#         break
# print(res)
