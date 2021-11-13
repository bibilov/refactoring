from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0

while i < a : #Неверно работаю с граничными условиями, в результате чего справа и внизу остались необработанные полосы по 10 пикселей.
    j = 0
    while j < a1 : #Неверно работаю с граничными условиями, в результате чего справа и внизу остались необработанные полосы по 10 пикселей.
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                n0 = arr[n][n1][0] #В одном месте я запутался с именами переменных.
                n2 = arr[n][n1][1]
                n3 = arr[n][n1][2]
                M = n0 + n2 + n3 #В одном месте я запутался с именами переменных.
                s += M / 3 #Неверно считаю компоненты серого цвета (забываю поделить на 3).
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int(s // 50) * 50
                arr[n][n1][1] = int(s // 50) * 50
                arr[n][n1][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
