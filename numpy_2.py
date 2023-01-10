# numpy 数组的形状
import numpy as np
t0 = np.array(range(0,10))
print(t0)
print(t0.shape)

t1 = np.array([[3,4,5,6],[4,5,6,7]])
print(t1)
print(t1.shape)

t2 = np.array([[3,4,5,6,7],
               [4,5,6,7,8]])
print(t2)
print(t2.shape)

t3 = np.array([range(3,8),range(4,9)])
print(t3)
print(t3.shape)

t4 = np.array([[3,4,5],[4,5,6],[7,8,9]])
print(t4)
print(t4.shape)

t5 = np.array([[3,4,5],[4,5,6],[7,8,9],[11,51,14]])
print(t5)
print(t5.shape)

t6 = np.array([[3,4,5],[4,5,6],
               [7,8,9],[11,51,14]])
print(t6)
print(t6.shape)

# 数组的计算：广播机制等