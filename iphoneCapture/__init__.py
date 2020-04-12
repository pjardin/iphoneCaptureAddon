#https://blender.stackexchange.com/questions/57306/how-to-create-a-custom-ui
#!/usr/bin/python
# -*- coding: utf-8 -*-
bl_info = {
    "name": "BMC: Blender Motion Capture",
    "description": "Blender Motion Capture that uses data from iphon X and above",
    "author": "Pascal Jardin",
    "version": (0, 0, 3),
    "blender": (2, 80, 0),
    "location": "3D View > BMC",
    "warning": "still a work in progress", # used for warning icon and text in addons panel
    "wiki_url": "",
    "tracker_url": "",
    "category": "Development"
}
import pathlib
path = pathlib.Path(__file__).parent.absolute()

import bpy

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

from . import face_Bone_Motion_Capture
from . import face_Motion_Capture
from . import body_Motion_Capture
from . import BMC

# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------
class Blender_Motion_Capture_Panel(Panel):
    bl_label = "Blender Motion Capture"
    bl_idname = "OBJECT_PT_blender_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BMC"
    bl_context = "objectmode"

    """
    @classmethod
    def poll(self,context):
        return context.object is not None
    """
    
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
        
        row.operator("apply.sound")
        row = layout.row()
  
class Face_Motion_Capture_Pose_Library_Panel(Panel):
  bl_label = "Face Pose Library"
  bl_idname = "OBJECT_PT_Pose_Library_panel"
  bl_space_type = "VIEW_3D"
  bl_region_type = "UI"
  bl_category = "BMC"
  bl_context = "objectmode"

  """
  @classmethod
  def poll(self,context):
      return context.object is not None
  """

  def draw(self, context):
      layout = self.layout
      scene = context.scene
      mytool = scene.my_tool


      row = layout.row()
      row.label(text="generate poses:")
      row = layout.row()
      row.operator("create.poslib_moto")
      row = layout.row()
      row.label(text="assign face rig to rig")
      row = layout.row()
      row.operator("create.poslib_moto_face_rig")
          
class Face_Motion_Capture_Shape_Keys_Panel(Panel):
    bl_label = "Face Shape Keys"
    bl_idname = "OBJECT_PT_Shape_Keys_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BMC"
    bl_context = "objectmode"

    """
    @classmethod
    def poll(self,context):
        return context.object is not None
    """

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool


        row = layout.row()
        row.label(text="Shape Keys:")
        row = layout.row()
        row.operator("check.blendshapes")
        row = layout.row()
        row.label(text="assign rig to mesh")
        row = layout.row()
        row.operator("create.moto_face_rig")

  
class Face_Motion_Capture_Panel(Panel):
    bl_label = "Face Motion Capture"
    bl_idname = "OBJECT_PT_custom_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BMC"
    bl_context = "objectmode"

    """
    @classmethod
    def poll(self,context):
        return context.object is not None
    """
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool


        row = layout.row()
        row.label(text="apply moto to rig")
        row = layout.row()
        row.operator("apply.blendshapes")
        row = layout.row()
        
        row.label(text="Euler Angles:")
        row = layout.row()
        row.operator("apply.head")
        row = layout.row()
        row.operator("apply.left_eye")
        row = layout.row()
        row.operator("apply.right_eye")


class Body_Motion_Capture_Panel(Panel):
    bl_label = "Body Motion Capture"
    bl_idname = "OBJECT_PT_body_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BMC"
    bl_context = "objectmode"

    """
    @classmethod
    def poll(self,context):
        return context.object is not None
    """
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        layout.operator("apply.body_anchor")
        layout.operator("create.mot_skel")
        
# ------------------------------------------------------------------------
#    Registration
# ------------------------------------------------------------------------

classes = (
    Face_Motion_Capture_Pose_Library_Panel,
    Face_Motion_Capture_Shape_Keys_Panel,
    Face_Motion_Capture_Panel,
    Body_Motion_Capture_Panel,
    body_Motion_Capture.BodyAnchorMotionOperator,
    body_Motion_Capture.createMotoSkelOperator,
    
    face_Motion_Capture.blendShapesCheckOperator,
    face_Motion_Capture.blendShapesApplyOperator,
    face_Motion_Capture.headOperator,
    face_Motion_Capture.leftEyeOperator,
    face_Motion_Capture.rightEyeOperator,
    
    face_Bone_Motion_Capture.createPoslibMotoFaceRig,
    face_Bone_Motion_Capture.poslibCreateOperator,
    
    Blender_Motion_Capture_Panel,
    BMC.G,
    BMC.apply_sound,

    face_Motion_Capture.createMotoFaceRig


)

def register():
    print("register")
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.my_tool = PointerProperty(type=BMC.G)

def unregister():
    print("unregister")

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()


