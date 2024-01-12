import numpy as np
import matplotlib.pyplot as plt

def placeShips(arr,ship):
    for i in range(10):
        for j in range(11-ship):
            if(checkMissHorizontal(arr,i,j,ship)):
                for k in range(ship):
                    arr[i][j + k] += 1
        for j in range(11-ship):
            if(checkMissVertical(arr,i,j,ship)):
                for k in range(ship):
                    arr[j + k][i] += 1

def checkMissHorizontal(arr,i,j,ship):
    for num in range(ship):
        if arr[i][j+num] == -1:
            return False
    return True

def checkMissVertical(arr,i,j,ship):
    for num in range(ship):
        if arr[j+num][i] == -1:
            return False
    return True
shipArr = [5,4,3,3,2]

def update(arr):
    for i in range(10):
        for j in range(10):
            if(arr[i][j] != -1):
                arr[i][j] = 0

    for ship in shipArr:
        placeShips(arr, ship)

def showMap(arr,blk):
    plt.imshow(arr, cmap='plasma', interpolation='nearest')
    plt.colorbar()
    plt.title('Matrix Heatmap')
    plt.show(block=blk)
    plt.pause(1)
    plt.close()
def findLargestIndex(arr):
    flat_index = np.argmax(arr)
    index = np.unravel_index(flat_index, arr.shape)
    return index

arr = np.empty([10, 10], dtype=int)
update(arr)
showMap(arr,False)

for i in range(10):
    print(findLargestIndex(arr))
    arr[findLargestIndex(arr)] = -1
    update(arr)
    showMap(arr,False)

showMap(arr,True)
plt.close()