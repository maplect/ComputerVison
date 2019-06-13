from numpy import *

def normalize(points):
    y = []
    for row in points:
        row /= points[-1]
        #y.append(row)
    return points

def make_homog(points):
    """ 将点集（dim× n 的数组）转换为齐次坐标表示 """
    return vstack((points,ones((1,points.shape[1]))))

x = array([[4,5,6]])
y = array([4,5,6])
print(x)
print(x.shape)
print(x.T.shape)
print(y)
print(y.shape)
print(y.T.shape)
'''z = normalize(x)
y = make_homog(x)
print(y)'''