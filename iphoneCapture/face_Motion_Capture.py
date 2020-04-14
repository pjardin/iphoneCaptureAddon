print("face")

import bpy
from bpy.types import Panel, Operator,Property
import json

import bmesh
from bpy import context

import pathlib
path = pathlib.Path(__file__).parent.absolute()


blendShapesName = [
             #Left Eye
             "eyeBlink_L"       ,
             "eyeLookDown_L"    ,
             "eyeLookIn_L"      ,
             "eyeLookOut_L"     ,
             "eyeLookUp_L"      ,
             "eyeSquint_L"      ,
             "eyeWide_L"        ,
             #Right Eye
             "eyeBlink_R"       ,
             "eyeLookDown_R"    ,
             "eyeLookIn_R"      ,
             "eyeLookOut_R"     ,
             "eyeLookUp_R"      ,
             "eyeSquint_R"      ,
             "eyeWide_R"        ,
             #jaw
             "jawForward"       ,
             "jawLeft"          ,
             "jawRight"         ,
             "jawOpen"          ,
             #mouth
             "mouthClose"       ,
             "mouthFunnel"      ,
             "mouthPucker"      ,
             "mouthLeft"        ,
             "mouthRight"       ,
             "mouthSmile_L"     ,
             "mouthSmile_R"     ,
             "mouthFrown_L"     ,
             "mouthFrown_R"     ,
             "mouthDimple_L"    ,
             "mouthDimple_R"    ,
             "mouthStretch_L"   ,
             "mouthStretch_R"   ,
             "mouthRollLower"   ,
             "mouthRollUpper"   ,
             "mouthShrugLower"  ,
             "mouthShrugUpper"  ,
             "mouthPress_L"     ,
             "mouthPress_R"     ,
             "mouthLowerDown_L" ,
             "mouthLowerDown_R" ,
             "mouthUpperUp_L"   ,
             "mouthUpperUp_R"   ,
             #brow
             "browDown_L"       ,
             "browDown_R"       ,
             "browInnerUp"      ,
             "browOuterUp_L"    ,
             "browOuterUp_R"    ,
             #cheek
             "cheekPuff"        ,
             "cheekSquint_L"    ,
             "cheekSquint_R"    ,
             #nose
             "noseSneer_L"      ,
             "noseSneer_R"      ,
             #tongue
             "tongueOut" ]


applyMotoDrivers = [
             #Left Eye
             ["eyeBlink_L"       , "LOC_Z", "-10*", "Bone.002"],
             ["eyeLookDown_L"    , "LOC_Z", "-10*", "Bone.009"],
             ["eyeLookIn_L"      , "LOC_X", "10*", "Bone.009"],
             ["eyeLookOut_L"     , "LOC_X", "-10*", "Bone.009"],
             ["eyeLookUp_L"      , "LOC_Z", "10*", "Bone.009"],
             ["eyeSquint_L"      , "LOC_Z", "10*", "Bone.012"],
             ["eyeWide_L"        , "LOC_Z", "10*", "Bone.002"],
             #Right Eye
             ["eyeBlink_R"       , "LOC_Z", "-10*", "Bone.003"],
             ["eyeLookDown_R"    , "LOC_Z", "-10*", "Bone.010"],
             ["eyeLookIn_R"      , "LOC_X", "-10*", "Bone.010"],
             ["eyeLookOut_R"     , "LOC_X", "10*", "Bone.010"],
             ["eyeLookUp_R"      , "LOC_Z", "10*", "Bone.010"],
             ["eyeSquint_R"      , "LOC_Z", "10*", "Bone.011"],
             ["eyeWide_R"        , "LOC_Z", "10*", "Bone.003"],
             #jaw
             ["jawForward"       , "LOC_Z", "10*", "Bone.024"],
             ["jawLeft"          , "LOC_X", "-10*", "Bone.024"],
             ["jawRight"         , "LOC_X", "10*", "Bone.024"],
             ["jawOpen"          , "LOC_Z", "-10*", "Bone.024"],
             #mouth
             ["mouthClose"       , "LOC_X", "-10*", "Bone.033"],
             ["mouthFunnel"      , "LOC_X", "-10*", "Bone.032"],
             ["mouthPucker"      , "LOC_X", "-10*", "Bone.031"],
             ["mouthLeft"        , "LOC_X", "-10*", "Bone.020"],
             ["mouthRight"       , "LOC_X", "10*", "Bone.020"],
             ["mouthSmile_L"     , "LOC_X", "-10*", "Bone.067"],
             ["mouthSmile_R"     , "LOC_X", "10*", "Bone.071"],
             ["mouthFrown_L"     , "LOC_X", "-10*", "Bone.069"],
             ["mouthFrown_R"     , "LOC_X", "10*", "Bone.073"],
             ["mouthDimple_L"    , "LOC_X", "-10*", "Bone.027"],
             ["mouthDimple_R"    , "LOC_X", "10*", "Bone.025"],
             ["mouthStretch_L"   , "LOC_Z", "-10*", "Bone.028"],
             ["mouthStretch_R"   , "LOC_Z", "-10*", "Bone.026"],
             ["mouthRollLower"   , "LOC_Z", "-10*", "Bone.021"],
             ["mouthRollUpper"   , "LOC_Z", "10*", "Bone.021"],
             ["mouthShrugLower"  , "LOC_Z", "-10*", "Bone.019"],
             ["mouthShrugUpper"  , "LOC_Z", "10*", "Bone.019"],
             ["mouthPress_L"     , "LOC_Z", "10*", "Bone.028"],
             ["mouthPress_R"     , "LOC_Z", "10*", "Bone.026"],
             ["mouthLowerDown_L" , "LOC_Z", "-10*", "Bone.023"],
             ["mouthLowerDown_R" , "LOC_Z", "-10*", "Bone.022"],
             ["mouthUpperUp_L"   , "LOC_Z", "10*", "Bone.018"],
             ["mouthUpperUp_R"   , "LOC_Z", "10*", "Bone.017"],
             #brow
             ["browDown_L"       , "LOC_Z", "-10*", "Bone.004"],
             ["browDown_R"       , "LOC_Z", "-10*", "Bone.005"],
             ["browInnerUp"      , "LOC_Z", "10*", "Bone.006"],
             ["browOuterUp_L"    , "LOC_Z", "10*", "Bone.008"],
             ["browOuterUp_R"    , "LOC_Z", "10*", "Bone.007"],
             #cheek
             ["cheekPuff"        , "LOC_X", "-10*", "Bone.029"],
             ["cheekSquint_L"    , "LOC_Z", "10*", "Bone.016"],
             ["cheekSquint_R"    , "LOC_Z", "10*", "Bone.013"],
             #nose
             ["noseSneer_L"      , "LOC_Z", "10*", "Bone.015"],
             ["noseSneer_R"      , "LOC_Z", "10*", "Bone.014"],
             #tongue
             ["tongueOut"        , "LOC_X", "-10*", "Bone.030"]
             ]


#https://blender.stackexchange.com/questions/39127/how-to-put-together-a-driver-with-python
def add_driver(
        source, target, prop, negative = False, func = '', boneName = "", transform_type= "", name = ""
    ):
    ''' Add driver to source prop (at index), driven by target dataPath '''

    d = source.driver_add( prop ).driver

    #https://docs.blender.org/api/current/bpy.types.DriverVariable.html?highlight=drivervariable
    v = d.variables.new()
    v.name                          = name
    v.type                          = "TRANSFORMS"
    
    v.targets[0].id                 = target
    v.targets[0].bone_target        = boneName
    
    v.targets[0].transform_type     = transform_type
    v.targets[0].transform_space    = 'LOCAL_SPACE'
 

    d.expression = func + "(" + v.name + ")" if func else v.name
    d.expression = d.expression if not negative else "-1 * " + d.expression

    
    
class createMotoFaceRig(Operator):
    bl_idname = "create.moto_face_rig"
    bl_label = "Create MotoFaceRig"

    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        print("createMotoFaceRig")
        objMesh = context.object

        
        #https://blender.stackexchange.com/questions/38060/how-to-link-append-with-a-python-script
        blendfile = str(path) + "/data/face.blend"
        section   = "\\Object\\"
        object    = "motoFaceRig"

        filepath  = blendfile + section + object
        directory = blendfile + section
        filename  = object

        bpy.ops.wm.append(
            filepath=filepath,
            filename=filename,
            directory=directory)
            
        #selected_objects = [ o for o in bpy.context.scene.objects if o.select ]
        
        
        arm = bpy.context.scene.objects['motoFaceRig']
        """
        for s in selected_objects:
            if "motoFaceRig" not in s.name:
                s.hide = True
            else:
                arm = s
        """
        for d in applyMotoDrivers:

            meshShapeKey = objMesh.data.shape_keys.key_blocks[d[0]]
            
            add_driver( meshShapeKey, arm, 'value', False, d[2], d[3], d[1], "motoCap")
         

        return {'FINISHED'}


class blendShapesCheckOperator(Operator):
    bl_idname = "check.blendshapes"
    bl_label = "check/generate"
    
    def execute(self, context):

        print("check/generate blendshapes")
        obj = context.object
    
        shape_keys = []

        try:
            shape_keys = obj.data.shape_keys.key_blocks
        except Exception:
            bpy.ops.object.shape_key_add(from_mix=False)
    
        shape_keys = obj.data.shape_keys.key_blocks

        missingShapes = []
   
        for bn in blendShapesName:
            try:
                sk1_data = shape_keys[bn].data
                
            except Exception:
                missingShapes.append(bn)
                pass
        
        print("missing:" + str(missingShapes))
        
        try:
            sk1_data = shape_keys["Basis"].data
                
        except Exception:
            bpy.ops.object.shape_key_add(from_mix=False)

        
        #creates missing shape keys
        for ms in missingShapes:
            print(ms)
            #sk = obj.shape_key_add('Basis')
            #sk.interpolation =  ms
            key = obj.shape_key_add(from_mix=False)
            key.name = ms
        
        
        return {'FINISHED'}



motoBone =[['Bone.059', ['LOC_Z']],
 ['Bone.057', ['LOC_X', 'LOC_Z']],
 ['Bone.055', ['LOC_Z']],
 ['Bone.060', ['LOC_Z']],
 ['Bone.058', ['LOC_X', 'LOC_Z']],
 ['Bone.056', ['LOC_Z']],
 ['Bone.034', ['LOC_X', 'LOC_Z']],
 ['Bone.054', ['LOC_X']],
 ['Bone.053', ['LOC_X']],
 ['Bone.052', ['LOC_X']],
 ['Bone.040', ['LOC_X']],
 ['Bone.039', ['LOC_X']], #
 ['Bone.041', ['LOC_X']], #
 ['Bone.038', ['LOC_Z']],
 ['Bone.042', ['LOC_Z']],
 ['Bone.035', ['LOC_Z']],
 ['Bone.043', ['LOC_Z']],
 ['Bone.037', ['LOC_Z']],
 ['Bone.036', ['LOC_Z']],
 ['Bone.044', ['LOC_Z']],
 ['Bone.045', ['LOC_Z']],
 ['Bone.062', ['LOC_Z']],
 ['Bone.064', ['LOC_Z']],
 ['Bone.063', ['LOC_Z']],
 ['Bone.061', ['LOC_Z']],
 ['Bone.065', ['LOC_Z']],
 ['Bone.050', ['LOC_X']],
 ['Bone.046', ['LOC_Z']],
 ['Bone.049', ['LOC_Z']],
 ['Bone.047', ['LOC_Z']],
 ['Bone.048', ['LOC_Z']],
 ['Bone.051', ['LOC_X']],#
 ['Bone.072', ['LOC_X']],
 ['Bone.074', ['LOC_X']],
 ['Bone.068', ['LOC_X']],
 ['Bone.070', ['LOC_X']] ]

class blendShapesApplyOperator(Operator):
    bl_idname = "apply.blendshapes"
    bl_label = "Apply"
    
    
    def execute(self, context):
        print("apply blendshapes")
        
        scene = context.scene
        # read file
        with open(bpy.path.abspath(scene.my_tool.folderPath)+ 'blendShapes.json', 'r') as myfile:
            data=myfile.read()

        # parse file
        move = json.loads(data)


        obj = context.object
        scene = context.scene
        

        for mb in motoBone:
            frame = scene.my_tool.startFrame;
            print( mb[0] + " " + str(mb[1]) +str(len(move[mb[0]])) )

            for m in move[mb[0]]:
                print(m)
                
                location = [0,0,0]
                if ( len(mb[1]) == 1):
                    if mb[1][0] == "LOC_Z" :
                        location = [0,0,m[0] / 10 /100]
                    else:
                        location = [m[0] / 10 /100,0,0]
                else:
                    location = [m[0] / 10 /100, 0, m[1] / 10 /100]
                    
                print(location)
                
                bone = obj.pose.bones[mb[0]]

                bone.location = location
                    
                bone.keyframe_insert('location', frame=frame)
                
                
                frame += 1
        
        """
        shape_keys = obj.data.shape_keys.key_blocks

        for blendShap in move:

            frame = scene.my_tool.startFrame;

            for v in move[blendShap]:
                shape_keys[blendShap].value = v
                shape_keys[blendShap].keyframe_insert("value", frame=frame)
                frame += 1
        """
        return {'FINISHED'}

class headOperator(Operator):
    bl_idname = "apply.head"
    bl_label = "Head"
    
    def execute(self, context):
        print("head")
        
        
        
        scene = context.scene

        print (bpy.path.abspath(scene.my_tool.folderPath) )
        
        # read file
        with open(bpy.path.abspath(scene.my_tool.folderPath)+ 'head.json', 'r') as myfile:
            data=myfile.read()
        
        # parse file
        move = json.loads(data)
        obj = context.object
        scene = context.scene
        
        frame = scene.my_tool.startFrame
                    

        for m in move:
            obj.rotation_euler = [-m[2], -m[1], m[0]]
            obj.keyframe_insert('rotation_euler', frame=frame)
            frame += 1
        
        return {'FINISHED'}
    
class leftEyeOperator(Operator):
    bl_idname = "apply.left_eye"
    bl_label = "LeftEye"
    
    def execute(self, context):
        print("leftEye")
        
        scene = context.scene
        # read file
        with open(bpy.path.abspath(scene.my_tool.folderPath)+ 'leftEye.json', 'r') as myfile:
            data=myfile.read()
        
        # parse file
        move = json.loads(data)
        obj = context.object
        scene = context.scene
        
        frame = scene.my_tool.startFrame
    
            
        for m in move:
            obj.rotation_euler = [m[2], m[1], m[0]]
            obj.keyframe_insert('rotation_euler', frame=frame)
            frame += 1
        
        return {'FINISHED'}
    
class rightEyeOperator(Operator):
    bl_idname = "apply.right_eye"
    bl_label = "RightEye"
    
    def execute(self, context):
        print("rightEye")
        
        scene = context.scene
        # read file
        with open(bpy.path.abspath(scene.my_tool.folderPath) + 'rightEye.json', 'r') as myfile:
            data=myfile.read()
        
        # parse file
        move = json.loads(data)
        obj = context.object
        scene = context.scene
        
        frame = scene.my_tool.startFrame
    
     
        for m in move:
            obj.rotation_euler = [m[2], m[1], m[0]]
            obj.keyframe_insert('rotation_euler', frame=frame)
            frame += 1
        
        return {'FINISHED'}
