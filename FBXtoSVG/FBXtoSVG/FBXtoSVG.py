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
       # f.write('<path d="')
       # f.write('<polygon points="')
        for i in mesh.GetPolygonVertices():
            point = mesh.GetControlPointAt(i)
            new_point = [0 for x in range(3)]
            new_point[0] = point[0]*camera[0][0] + point[1]*camera[1][0] + point[2]*camera[2][0]
            new_point[1] = point[0]*camera[0][1] + point[1]*camera[1][1] + point[2]*camera[2][1]
            new_point[2] = point[0]*camera[0][2] + point[1]*camera[1][2] + point[2]*camera[2][2]
            #print('%d : %f, %f, %f' %(i, point[0], point[1], point[2]))
            if (i%3)==0:
                f.write('<path d="M%d %d ' % (100+new_point[0]+50, 400-new_point[1]))
            else:
             if (i%3)==1:
                f.write('L%d %d ' % (100+new_point[0]+50, 400-new_point[1]))
            #f.write('" />')
             else:
                if (i%3)==2:
                     f.write('L%d %d Z" /> ' % (100+new_point[0]+50, 400-new_point[1])) #stroke="darkred" stroke-width="0.2" fill="none" />')
                # f.write('<polygon points="')
        #f.write('Z" /> ') # stroke="darkred" stroke-width="0.2" fill="none" />')
    for i in range(node.GetChildCount()):
        
        get_projection(node.GetChild(i))
    
     

sdk_manager, scene = FbxCommon.InitializeSdkObjects()

if not FbxCommon.LoadScene(sdk_manager, scene, "TeaPot.fbx"):
    print("error in LoadScene")
#v=[]
#v=  FbxCommon.FbxCamera.Position.Get()
#v= FbxCommon.FbxMatrix.GetRow(FbxMatrix(0))
#print v
scale()
#rotateX(90)
rotateX(45)
#rotateY(35.264)
#rotateZ(45)

f.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="500" height="500"> ')
#f.write('<polygon points="')
get_projection(scene.GetRootNode())
f.write('" stroke="darkred" stroke-width="0.2" fill="none" />')
f.write('</svg>')