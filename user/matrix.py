# 矩阵计算
import numpy as np

list1=[[1,1,1,1],
      [1,2,3,1],
      [1,4,9,16],
      [1,8,27,64]]
A=np.array(list1)
print(np.linalg.det(A))

list3=[[1,2,5],
       [1,3,-2],
        [2,5,3]]
B=np.array(list3)
print(np.linalg.det(B))
