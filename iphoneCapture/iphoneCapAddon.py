
bl_info = {
    "name": "Iphone Motion Capture",
    "author": "Pascal Jardin",
    "version": (0, 1),
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


class G:
    folder_loc = "?"

class getFolderOperator(Operator):

    bl_idname = "get.folder"
    bl_label = "get cap folder"
    
    #https://blender.stackexchange.com/questions/14738/use-filemanager-to-select-directory-instead-of-file
    bl_options = {'REGISTER'}

    # Define this to tell 'fileselect_add' that we want a directoy
    directory = bpy.props.StringProperty(
        name="Outdir Path",
        description="Where I will save my stuff"
        # subtype='DIR_PATH' is not needed to specify the selection mode.
        # But this will be anyway a directory path.
        )

    def execute(self, context):

        print("Selected dir: '" + self.directory + "'")
        G.folder_loc = self.directory
        return {'FINISHED'}

    def invoke(self, context, event):
        # Open browser, take reference to 'self' read the path to selected
        # file, put path in predetermined self fields.
        # See: https://docs.blender.org/api/current/bpy.types.WindowManager.html#bpy.types.WindowManager.fileselect_add
        context.window_manager.fileselect_add(self)
        # Tells Blender to hang on for the slow user input
        return {'RUNNING_MODAL'}



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
        
        # read file
        with open(G.folder_loc + 'blendShapes.json', 'r') as myfile:
            data=myfile.read()

        # parse file
        move = json.loads(data)


        obj = context.object
        shape_keys = obj.data.shape_keys.key_blocks

        for blendShap in move:

            frame = 0;

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
        
        # read file
        with open(G.folder_loc + 'head.json', 'r') as myfile:
            data=myfile.read()
        
        # parse file
        move = json.loads(data) 
        obj = context.object  
        
        frame = 0;
                    

        for m in move:
            obj.rotation_euler = [m[2], m[1], m[0]]
            obj.keyframe_insert('rotation_euler', frame=frame)
            frame += 1
                
        return {'FINISHED'}
    
class leftEyeOperator(Operator):
    bl_idname = "apply.left_eye"
    bl_label = "LeftEye"
    
    def execute(self, context): 
        print("leftEye")
        
        # read file
        with open(G.folder_loc + 'leftEye.json', 'r') as myfile:
            data=myfile.read()
        
        # parse file
        move = json.loads(data)   
        obj = context.object
        
        frame = 0;
    
            
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
        
        # read file
        with open(G.folder_loc + 'rightEye.json', 'r') as myfile:
            data=myfile.read()
        
        # parse file
        move = json.loads(data) 
        obj = context.object  
        
        frame = 0;
     
        for m in move:
            obj.rotation_euler = [m[2], m[1], m[0]]
            obj.keyframe_insert('rotation_euler', frame=frame)
            frame += 1
        
        return {'FINISHED'}       
    

class IphoneMotionCapture(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Iphone Motion Capture"
    bl_idname = "OBJECT_Motion_Capture"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'


    def draw(self, context):
        layout = self.layout

        obj = context.object
        row = layout.row()

        row.operator("get.folder")
        row = layout.row()
        
        row.label(text="folder: " + G.folder_loc)
        
        row = layout.row()
        
        row.label(text="Active object is: " + obj.name)
        
        row = layout.row()
        
        row.label(text="BlendShapes:")
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


def register():
    bpy.utils.register_class(IphoneMotionCapture)
    bpy.utils.register_class(headOperator)
    bpy.utils.register_class(leftEyeOperator)
    bpy.utils.register_class(rightEyeOperator)
    bpy.utils.register_class(blendShapesCheckOperator)
    bpy.utils.register_class(blendShapesApplyOperator)
    
    bpy.utils.register_class(getFolderOperator)
    
    
def unregister():
    bpy.utils.unregister_class(IphoneMotionCapture)
    bpy.utils.unregister_class(headOperator)
    bpy.utils.unregister_class(leftEyeOperator)
    bpy.utils.unregister_class(rightEyeOperator)
    bpy.utils.unregister_class(blendShapesCheckOperator)
    bpy.utils.unregister_class(blendShapesApplyOperator)
    
    bpy.utils.unregister_class(getFolderOperator)
    

if __name__ == "__main__":
    register()
