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

    
    
class createPoslibMotoFaceRig(Operator):
    bl_idname = "create.poslib_moto_face_rig"
    bl_label = "Create Poslib MotoFaceRig"

    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        print("create Poslib MotoFaceRig")
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
            
        #selected_objects = bpy.context.selected_objects
        
        
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


class poslibCreateOperator(Operator):
    bl_idname = "create.poslib_moto"
    bl_label = "generate poslib"
    
    def execute(self, context):
        #https://docs.blender.org/api/current/bpy.ops.poselib.html?highlight=pose#module-bpy.ops.poselib
        #https://blender.stackexchange.com/questions/100152/saving-multiple-poses-to-pose-library-via-python#100160

        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.select_all(action='SELECT')
        bpy.ops.pose.rot_clear()
        bpy.ops.pose.loc_clear()
        bpy.ops.pose.scale_clear()
        bpy.ops.pose.select_all(action='DESELECT')


        #----------to set up pose action
        bpy.ops.poselib.new()

        findPosLib = []

        for a in bpy.data.actions:
            if "PoseLib." in a.name:
                findPosLib.append(a.name)

        if len(findPosLib) == 0:
            bpy.data.actions["PoseLib"].name = "BMC_PoseLib"
        else:
            bpy.data.actions[findPosLib[-1]].name = "BMC_PoseLib"

        #----------to set up pose action


        bpy.ops.poselib.pose_add(frame = 0, name="Basis")

        for f, shape in enumerate(applyMotoDrivers):
            bpy.ops.pose.select_all(action="DESELECT")
            bpy.ops.poselib.pose_add(frame = f+1, name=shape[0])


        bpy.ops.object.mode_set(mode='OBJECT')


        armature = bpy.context.scene.objects['Armature']
        action = bpy.data.actions['BMC_PoseLib']

        
        return {'FINISHED'}
