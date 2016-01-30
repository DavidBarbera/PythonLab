

#print([[2 for x in range(3)] for x in range(3)])

camera = [[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]]

def scale():
    rot = [[3, 0, 0],
          [0, 3, 0],
          [0, 0, 3]]

    result = [[0 for x in range(3)] for x in range(3)]

    for i in range(3):
        for j in range(3):
            result[i][j] = camera[i][0]*rot[0][j] + camera[i][1]*rot[1][j] + camera[i][2]*rot[2][j]


    for i in range(3):
        for j in range(3):
            camera[i][j] = result[i][j]

scale()
print(camera)