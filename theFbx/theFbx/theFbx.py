import FbxCommon

def polycount(node)
    mesh = node.GetMesh()
  
    if not mesh:
        print("not mesh")
    else:
        mesh.GetPolycount()


sdk_manager, scene = FbxCommon.InitializeSdkObjects()

if not FbxCommon.LoadScene(sdk_manager, scene, "TeaPot.fbx"):
    print("error in LoadScene")

polycount(scene.GetRootNode())



            



