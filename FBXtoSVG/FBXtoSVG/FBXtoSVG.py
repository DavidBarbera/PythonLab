import FbxCommon
import math

f = open('proj.svg', 'w')
if  f.errors:
    print "Problems opening the file"

width = 500
height = 500

camera = [[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]]

def scale(a):
    rot = [[a, 0, 0],
          [0, a, 0],
          [0, 0, a]]

    result = [[0 for x in range(3)] for x in range(3)]

    for i in range(3):
        for j in range(3):
            result[i][j] = camera[i][0]*rot[0][j] + camera[i][1]*rot[1][j] + camera[i][2]*rot[2][j]

    for i in range(3):
        for j in range(3):
            camera[i][j] = result[i][j]

def rotateX(a):
    rot = [[1, 0, 0],
           [0, math.cos(a), -math.sin(a)],
           [0, math.sin(a), math.cos(a)]]

    result = [[0 for x in range(3)] for x in range(3)] 

    for i in range(3):
        for j in range(3):
            result[i][j] = camera[i][0]*rot[0][j] + camera[i][1]*rot[1][j] + camera[i][2]*rot[2][j]

    for i in range(3):
        for j in range(3):
            camera[i][j] = result[i][j]

def rotateY(a):
    rot = [[ math.cos(a), 0, math.sin(a)],
           [0, 1, 0],
           [-math.sin(a), 0, math.cos(a)]]

    result = [[0 for x in range(3)] for x in range(3)] 

    for i in range(3):
        for j in range(3):
            result[i][j] = camera[i][0]*rot[0][j] + camera[i][1]*rot[1][j] + camera[i][2]*rot[2][j]

    for i in range(3):
        for j in range(3):
            camera[i][j] = result[i][j]

def rotateZ(a):
    rot = [[math.cos(a), -math.sin(a),0],
           [ math.sin(a), math.cos(a),0],
           [0,0,1]]

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
            vertex = [0 for x in range(3)]
            vertex[0] = point[0]*camera[0][0] + point[1]*camera[1][0] + point[2]*camera[2][0]
            vertex[1] = point[0]*camera[0][1] + point[1]*camera[1][1] + point[2]*camera[2][1]
            vertex[2] = point[0]*camera[0][2] + point[1]*camera[1][2] + point[2]*camera[2][2]
            f.write('%d,%d ' % (vertex[0] + width/2, height/2 - vertex[1]))    #Only 2 first components as .svg is 2D

    for i in range(node.GetChildCount()):
        
        get_projection(node.GetChild(i))

        
  
sdk_manager, scene = FbxCommon.InitializeSdkObjects()

if not FbxCommon.LoadScene(sdk_manager, scene, "TeaPot.fbx"):
    print("couldn't load the scene")

scale(4)
#rotateX(90)
rotateX(45)
rotateY(-45)
#rotateY(35.264)
#rotateZ(45)
#rotateX(45)

f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="%d" height="%d"> ' % (width,height))
f.write('<polygon points="')
get_projection(scene.GetRootNode())
f.write('" stroke="darkred" stroke-width="0.2" fill="none" />')
f.write('</svg>')

f.close()



