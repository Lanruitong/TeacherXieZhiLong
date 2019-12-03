import matplotlib.pyplot as plt
import numpy as np
import seaborn
import math

seaborn.set()
# 随机生成十个点并用蓝色显示
arr = np.random.randint(0, 50, (10, 2))
for i in range(10):
    plt.scatter(arr[i][0], arr[i][1], c='b', s=50)

# 随机生成一个点用红色表示
arr_random = np.random.randint(0, 50, (1, 2))
plt.scatter(arr_random[0][0], arr_random[0][1], c='r', s=50)

# 计算每个点到随机点的距离放入distance数组
distance = []
for i in range(10):
    distance.append(math.sqrt((arr[i][0] - arr_random[0][0]) ** 2
                              + (arr[i][1] - arr_random[0][1]) ** 2))


# 计算K个距离最小的点,返回存放这K个最小点坐标的数组
def distance_compute(K):

    min_number = []
    for _ in range(K):
        temp = 0
        min = distance[0]
        for j in range(10):
            if distance[j] < min:
                min = distance[j]
                temp = j
        min_number.append(temp)

        distance[temp] = 100000
    return min_number


# 重新对K个最小的点着绿色
def repaint(min_number):
    for i in min_number:
        plt.scatter(arr[i][0], arr[i][1], c='g', s=50)


a = distance_compute(5)
repaint(a)
plt.show()
