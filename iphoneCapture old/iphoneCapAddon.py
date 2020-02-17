
bl_info = {
    "name": "Iphone Motion Capture",
    "author": "Pascal Jardin",
    "version": (0, 3),
    "blender": (2, 80, 0),
    "location": "View3D > Tool Shelf > Iphone Motion Capture",
    "description": "get data from iphone and import to blender!",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object",
}

import bpy
from bpy.types import Panel, Operator,Property
import json

import bmesh
from bpy import context



from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )

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


class G(PropertyGroup):
    folder_loc = "?"

    startFrame: IntProperty(
        name = "Start Frame",
        description="Start Frame",
        default = 0,
        min = 0
        )
        
    blendShapeType: EnumProperty(
        name="Type",
        description="Apply Data to attribute.",
        items=[ ('iOS', "iOS", ""),
                ('makeHuman', "makeHuman", ""),
                ('custom', "custom", ""),
               ]
        )
        
    folderPath: StringProperty(
        name = "Directory",
        description="Choose a directory:",
        default="",
        maxlen=1024,
        subtype='DIR_PATH'
        )


class blendShapesCheckOperator(Operator):
    bl_idname = "check.blendshapes"
    bl_label = "check/generate"
    
    def execute(self, context):

        print("check/generate blendshapes")
        obj = context.object
    
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
        shape_keys = obj.data.shape_keys.key_blocks
        scene = context.scene
        
        for blendShap in move:

            frame = scene.my_tool.startFrame;

            for v in move[blendShap]:
                shape_keys[blendShap].value = v
                shape_keys[blendShap].keyframe_insert("value", frame=frame)
                frame += 1
        
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
    
"""
        motcap = [
        "head"           : [],
        
        "leftFoot"       : [],
        "leftHand"       : [],
        "leftSholder"    : [],
        
        "rightFoot"      : [],
        "rightHand"      : [],
        "rightSholder"   : [],
        
        "root"           : []
        ]

"""
boneMotcap = [
"head"           ,

"leftFoot"       ,
"leftHand"       ,
"leftSholder"    ,

"rightFoot"      ,
"rightHand"      ,
"rightSholder"   ,

"root"
]


class BodyAnchorMotionOperator(Operator):
    bl_idname = "apply.body_anchor"
    bl_label = "apply"
    
    def execute(self, context):
        
        obj = context.object
        obj.rotation_mode = 'YZX'
        
        scene = context.scene

        # read file
        with open(bpy.path.abspath(scene.my_tool.folderPath)+ 'motcap.json', 'r') as myfile:
            data=myfile.read()
        
        # parse file
        move = json.loads(data)
        scene = context.scene
        frame = scene.my_tool.startFrame
        
        originaLocation = [ -move[0][15][0],move[0][15][2],move[0][15][1]]
        
        zOffset = -move[0][1][2]
        
        if zOffset > -move[0][3][2]:
            zOffset = -move[0][3][2]
        offset = [0,0, -zOffset * 10 + .2]
        
        #print(originaLocation)
        #return {'FINISHED'}
    
        for f in move:
            
            joint = 0
            
            for b in f:
                
                if (joint < 15):
                    bone = obj.pose.bones['joint'+ str(joint)]
                      
                    bone.location = [-b[0],b[1],-b[2]]
                    bone.keyframe_insert('location', frame=frame)
                    
                    
                elif (joint == 15):
                    obj.location = [ -b[0] - originaLocation[0] + offset[0],
                        b[2]- originaLocation[1] + offset[1],
                        b[1] - originaLocation[2] + offset[2]]
                    obj.keyframe_insert('location', frame=frame)
                elif (joint == 16):
                    obj.rotation_euler = [b[2], -b[1], -b[0]]
                    obj.keyframe_insert('rotation_euler', frame=frame)

                joint +=1

            frame += 1
            
        
        """
        if (obj.type == "ARMATURE"):
            print("ARMATURE")
            
            for b in boneMotcap:
                
                frame = 0;
                for m in move[b]:
                
                    bone = obj.pose.bones[b]
                    
                    bone.location = [m[0],m[1],m[2]]
                    bone.rotation_euler = [m[3], m[4], m[5]]
                    bone.keyframe_insert('rotation_euler', frame=frame)
                    bone.keyframe_insert('location', frame=frame)
                    frame += 1
        """
        return {'FINISHED'}


class createMotoSkelOperator(Operator):
    bl_idname = "apply.mot_skel"
    bl_label = "Create"
    
    def execute(self, context):
        print("skeleton")
        
        
        bpy.ops.object.empty_add(type='ARROWS', align='WORLD', radius=0.5, location=(0, 0, 0), rotation=(0, 0, 0))
        motoOffset = context.object
        motoOffset.name = "motoOffset"

        bpy.ops.object.armature_add(enter_editmode=True, location=(0, 0, 0))
        obj = context.object
        obj.name = "motoSkel"
        

        
        for bone in obj.data.edit_bones:
            obj.data.edit_bones.remove(bone)
        
        edit_bones = obj.data.edit_bones
        
        boneSize = 16
        
        for i in range(0,boneSize):
            b = edit_bones.new('joint'+ str(i))
            b.head = (0, 0, 0.0)
            b.tail = (0, 0, 0.1)
            
            
        b = edit_bones.new('joint16')
        b.head = (0.10054, -0.00119, -0.024963)
        b.tail = (0.10054, --0.00119, 0.075037)
        
        b = edit_bones.new('joint17')
        b.head = (-0.10054, -0.00119, -0.024963)
        b.tail = (-0.10054, -0.00119, 0.075037)
        
        # exit edit mode to save bones so they can be used in pose mode
        bpy.ops.object.mode_set(mode='OBJECT')
        
        # make the custom bone shape
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.05, enter_editmode=False, location=(0.0, 0.0, -1.0))
        bpy.ops.object.hide_view_set(unselected=False)

        customShape = context.object
        customShape.name = "jointCustomShape"

        for f in customShape.data.polygons:
            f.use_smooth = True

        for i in range(0, (boneSize + 2)):
            # use pose.bones for custom shape
            obj.pose.bones['joint'+ str(i)].custom_shape = customShape
            obj.pose.bones['joint'+ str(i)].use_custom_shape_bone_size = False

            # use data.bones for show_wire
            #obj.data.bones['bone2'].show_wire = True
        
        obj.parent =  motoOffset
        customShape.parent = motoOffset

    
        return {'FINISHED'}

class apply_sound(Operator):
    bl_idname = "apply.sound"
    bl_label = "apply sound"
    
    def execute(self, context):
        print("apply sound")
        
        scene = context.scene
        if not scene.sequence_editor:
            scene.sequence_editor_create()
        
        
        bpy.context.scene.sync_mode = 'AUDIO_SYNC'
        
        if scene.my_tool.folderPath != "":
            soundstrip = scene.sequence_editor.sequences.new_sound("audio", scene.my_tool.folderPath + 'audio.wav', 2, scene.my_tool.startFrame )
        
        
        return {'FINISHED'}



class IphoneMotionCapture(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Iphone Motion Capture"
    bl_idname = "OBJECT_PT_MotionCapture"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'


    def draw(self, context):
        layout = self.layout
        scene = context.scene
        obj = context.object
        
        mytool = scene.my_tool
        
        row = layout.row()
        layout.prop(mytool, "startFrame")

        row = layout.row()
        
        layout.prop(mytool, "folderPath")
        
        row = layout.row()
        
        try:
            row.label(text="Active object is: " + obj.name)
        except Exception:
            row.label(text="NO object is selected!!")
        
        row = layout.row()
        
        row.label(text="------------ FACE ---------------------")
        row = layout.row()
        row.operator("apply.sound")
        row = layout.row()
        
        #layout.prop(mytool, "blendShapeType")
        #row = layout.row()
        
        row.label(text= scene.my_tool.blendShapeType  + " BlendShapes:")
        row = layout.row()
        row.operator("check.blendshapes")
        row = layout.row()
        row.operator("apply.blendshapes")
        row = layout.row()
        
        row.label(text="Apply Euler Angles:")
        row = layout.row()
        row.operator("apply.head")
        row = layout.row()
        row.operator("apply.left_eye")
        row = layout.row()
        row.operator("apply.right_eye")
        
        
        
        row = layout.row()
        row.label(text="------------ BODY ---------------------")
        row = layout.row()
        row.operator("apply.body_anchor")
        row = layout.row()

        row.operator("apply.mot_skel")
        row = layout.row()


def register():
    bpy.utils.register_class(IphoneMotionCapture)
    bpy.utils.register_class(headOperator)
    bpy.utils.register_class(leftEyeOperator)
    bpy.utils.register_class(rightEyeOperator)
    bpy.utils.register_class(blendShapesCheckOperator)
    bpy.utils.register_class(blendShapesApplyOperator)
    
    
    bpy.utils.register_class(BodyAnchorMotionOperator)
    bpy.utils.register_class(createMotoSkelOperator)
    
    bpy.utils.register_class(apply_sound)
    
    bpy.utils.register_class(G)
    
    bpy.types.Scene.my_tool = PointerProperty(type=G)
    
def unregister():

    bpy.utils.unregister_class(headOperator)
    bpy.utils.unregister_class(leftEyeOperator)
    bpy.utils.unregister_class(rightEyeOperator)
    bpy.utils.unregister_class(blendShapesCheckOperator)
    bpy.utils.unregister_class(blendShapesApplyOperator)
    
    
    bpy.utils.unregister_class(BodyAnchorMotionOperator)
    bpy.utils.unregister_class(createMotoSkelOperator)

    bpy.utils.unregister_class(apply_sound)
    
    bpy.utils.unregister_class(G)
    
    del bpy.types.Scene.my_tool
    

if __name__ == "__main__":
    register()

