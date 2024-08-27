import matplotlib.pyplot as pl
from LinearAlgebra.playLA.matrix import Matrix
points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4], [1, 3],
           [2, 3], [2, 2], [1, 2], [1, 0]]
# x=[ item[0] for item in points]
# y=[ item[1] for item in points]
# # 设置大小
# pl.figure(figsize=(5,5))
# # 设置坐标最大值和最小值
# pl.xlim(-10,10)
# pl.ylim(-10,10)
# pl.plot(x,y)

# P = Matrix([[-1,0],[0,1]])
T = Matrix(points)
# R=P.dot(T.T())
T[0,1]
print(T[0,1])
# pl.show()


