import numpy as np

arr2d = np.random.rand(4,4)
print(arr2d)

row2 = arr2d[1,:].copy()
print(row2)

col3 = arr2d[:,2].copy()
print(col3)

arr2d[0:2,0:2] = 0.21
print(arr2d)

# arr8 = np.ones([8,8])
# # print(arr8)

# for i, row in enumerate(arr8):
#     if(i % 2) == 0:
#         arr8[i,1::2] = 0
#     else:
#         arr8[i,::2] = 0
# print(arr8)

arr9 = np.ones([8,8])
arr9[0::2,0::2] = 0
arr9[1::2,1::2] = 0
print(arr9)