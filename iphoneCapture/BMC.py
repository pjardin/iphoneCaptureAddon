print("BMC")
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


# ------------------------------------------------------------------------
#    Scene Properties
# ------------------------------------------------------------------------
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

# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------

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
