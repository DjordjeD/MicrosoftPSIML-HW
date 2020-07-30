import numpy as np
import os
from PIL import Image
#"C:\\Users\\Korisnik\\Desktop\\public (1)\public\\set\\map.png"
image_file_map = Image.open(input)
N = int(input())
p_no_of_rows, p_no_of_columnb = map(int, input().split())
mapa = np.array(image_file_map)
ispis = []


def saberi_2_pixela(list1, list2):
    pixel = [int(list1[0] + list2[0]), int(list1[1] + list2[1]),
             int(list1[2] + list2[2])]
    return pixel


def same_pixel(list1, list2):
    return list1[0] == list2[0] and list1[1] == list2[1] and list1[2] == list2[2]


def get_pixel(list):
    return[list[0], list[1], list[2]]


def uradi_4_pixela(list1, list2, list3, list4):
    pixel = [int(list1[0] + list2[0]+list3[0] - list4[0]), int(list1[1] +
                                                               list2[1]+list3[1] - list4[1]), int(list1[2] + list2[2]+list3[2] - list4[2])]
    return pixel


def uradi_4_pixela2(list1, list2, list3, list4):
    pixel = [int(list1[0] + list2[0] - list3[0] - list4[0]), int(list1[1] +
                                                                 list2[1]-list3[1] - list4[1]), int(list1[2] + list2[2]-list3[2] - list4[2])]
    return pixel


suma = [[[0 for k in range(3)] for j in range(len(mapa[0]))]
        for i in range(len(mapa))]

suma[0][0] = get_pixel(mapa[0][0])

for i in range(1, len(mapa[0])):
    suma[0][i] = saberi_2_pixela(mapa[0][i], suma[0][i-1])

for i in range(1, len(mapa)):
    suma[i][0] = saberi_2_pixela(mapa[i][0], suma[i-1][0])

for i in range(1, len(mapa)):
    for j in range(1, len(mapa[0])):
        suma[i][j] = uradi_4_pixela(
            mapa[i][j], suma[i-1][j], suma[i][j-1], suma[i-1][j-1])


for i in range(N):
    path = input()
    image_file = Image.open(path)
    patch = np.array(image_file)
    patch_suma = [0, 0, 0]
    # print(mapa)
    for i in range(len(patch)):
        for j in range(len(patch[0])):
            patch_suma = saberi_2_pixela(patch_suma, patch[i][j])

    moguci = []
    no_of_rows = len(mapa)
    no_of_column = len(mapa[0])
# suma [i-40][j-40] suma[i-40][j] suma[i][j-40]
    for i in range(p_no_of_rows, no_of_rows):
        for j in range(p_no_of_column, no_of_rows):
            if(same_pixel(patch_suma, uradi_4_pixela2(suma[i][j], suma[i-p_no_of_rows][j-p_no_of_column], suma[i-p_no_of_rows][j], suma[i][j-p_no_of_column]))):
                koordinata = [i, j]
                moguci.append(koordinata)

    for item in moguci:
        i = item[0]
        j = item[1]
        for pi in range(0, p_no_of_rows, 10):
            for pj in range(0, p_no_of_column, 10):
                if(same_pixel(patch[pi][pj], mapa[i+pi][j+pj])):
                    flag = True
                else:
                    not_same = True
                    flag = False
                    break
            if(not_same):
                break
        if(flag):
            string = str(j)+","+str(i)
            ispis.append(string)
            break


print(ispis)
