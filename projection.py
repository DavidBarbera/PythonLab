import FbxCommon
import math

f = open('proj.svg', 'w')

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

def rotate_x():
    rot = [[1, 0, 0],
          [0, math.cos(45), -math.sin(45)],
          [0, math.sin(45), math.cos(45)]]

    result = [[0 for x in range(3)] for x in range(3)] 

    for i in range(3):
        for j in range(3):
            result[i][j] = camera[i][0]*rot[0][j] + camera[i][1]*rot[1][j] + camera[i][2]*rot[2][j]

    for i in range(3):
        for j in range(3):
            camera[i][j] = result[i][j]

def get_projection(node):
    
    mesh = node.GetMesh()
    if not mesh:
        print("not mesh")
    else:
        for i in mesh.GetPolygonVertices():
            point = mesh.GetControlPointAt(i)
            new_point = [0 for x in range(3)]
            new_point[0] = point[0]*camera[0][0] + point[1]*camera[1][0] + point[2]*camera[2][0]
            new_point[1] = point[0]*camera[0][1] + point[1]*camera[1][1] + point[2]*camera[2][1]
            new_point[2] = point[0]*camera[0][2] + point[1]*camera[1][2] + point[2]*camera[2][2]
            #print('%d : %f, %f, %f' %(i, point[0], point[1], point[2]))
            f.write('%d,%d ' % (100+new_point[0]+50, 400-new_point[1]))

    for i in range(node.GetChildCount()):
        get_projection(node.GetChild(i))
    


sdk_manager, scene = FbxCommon.InitializeSdkObjects()

if not FbxCommon.LoadScene(sdk_manager, scene, "teapot.fbx"):
    print("error in LoadScene")

scale()
rotate_x()

f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="500" height="500"> ')
f.write('<polyline points="')
get_projection(scene.GetRootNode())
f.write('" stroke="red" stroke-width="0.1" fill="none" />')
f.write('</svg>')