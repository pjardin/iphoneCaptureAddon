print("body")
import bpy
from bpy.types import Panel, Operator,Property
import json

import bmesh
from bpy import context


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

        return {'FINISHED'}


class createMotoSkelOperator(Operator):
    bl_idname = "create.mot_skel"
    bl_label = "Create"
    
    def execute(self, context):
        
        print("skeleton")
        print("create.mot_skel")


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




        b = edit_bones.new('bone1')
        b.tail = (0.10054, -0.00119, -0.024963)
        b.head = (0,0,0)

        b = edit_bones.new('bone2')
        b.tail = (-0.10054, -0.00119, -0.024963)
        b.head = (0,0,0)




        b = edit_bones.new('bone3')
        b.tail = (-0.44,0,0)
        b.head = (0,0,0)



        b = edit_bones.new('bone4')
        b.tail = (-0.15,0,0)
        b.head = (0,0,0)

        b = edit_bones.new('bone5')
        b.tail = (-0.15,0,0)
        b.head = (0,0,0)

        b = edit_bones.new('bone6')
        b.tail = (-0.15,0,0)
        b.head = (0,0,0)

        b = edit_bones.new('bone7')
        b.tail = (-0.15,0,0)
        b.head = (0,0,0)

        b = edit_bones.new('bone8')
        b.tail = (-0.15,0,0)
        b.head = (0,0,0)

        b = edit_bones.new('bone9')
        b.tail = (-0.15,0,0)
        b.head = (0,0,0)


        b = edit_bones.new('bone10')
        b.tail = (-0.28,0,0)
        b.head = (0,0,0)

        b = edit_bones.new('bone11')
        b.tail = (-0.28,0,0)
        b.head = (0,0,0)

        b = edit_bones.new('bone12')
        b.tail = (-0.28,0,0)
        b.head = (0,0,0)

        b = edit_bones.new('bone13')
        b.tail = (-0.28,0,0)
        b.head = (0,0,0)

        b = edit_bones.new('bone14')
        b.tail = (-0.42,0,0)
        b.head = (0,0,0)

        b = edit_bones.new('bone15')
        b.tail = (-0.42,0,0)
        b.head = (0,0,0)

        b = edit_bones.new('bone16')
        b.tail = (-0.455,0,0)
        b.head = (0,0,0)

        b = edit_bones.new('bone17')
        b.tail = (-0.455,0,0)
        b.head = (0,0,0)

        # exit edit mode to save bones so they can be used in pose mode
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.posemode_toggle()
        bpy.ops.pose.group_add()
        bpy.context.object.name = "tracked points"

        bone_groups = obj.pose.bone_groups


        bone_groups["Group"].color_set = 'THEME12'
        bone_groups["Group"].name = "tracked points"


        # make the custom bone shape
        #bpy.ops.mesh.primitive_uv_sphere_add(radius=0.04, enter_editmode=False, location=(0.0, 0.0, -1.0),  rotation=(1.5708, 0, 0))
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=4, radius=0.04, enter_editmode=False, location=(0.0, 0.0, -1.0))

        bpy.ops.object.hide_view_set(unselected=False)

        customShape = context.object
        customShape.name = "jointCustomShape"

        for f in customShape.data.polygons:
            f.use_smooth = True

        for i in range(0, (boneSize + 2)):
            # use pose.bones for custom shape
            obj.pose.bones['joint'+ str(i)].custom_shape = customShape
            obj.pose.bones['joint'+ str(i)].use_custom_shape_bone_size = False
            obj.pose.bones['joint'+ str(i)].bone_group = bone_groups["tracked points"]

            # use data.bones for show_wire
            #obj.data.bones['bone2'].show_wire = True


        crc = obj.pose.bones['bone3'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint15"

        crc = obj.pose.bones['bone3'].constraints.new('DAMPED_TRACK')
        crc.target = obj
        crc.subtarget = "joint4"



        crc = obj.pose.bones['bone4'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint4"

        crc = obj.pose.bones['bone4'].constraints.new('DAMPED_TRACK')
        crc.target = obj
        crc.subtarget = "joint11"


        crc = obj.pose.bones['bone5'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint5"

        crc = obj.pose.bones['bone5'].constraints.new('DAMPED_TRACK')
        crc.target = obj
        crc.subtarget = "joint6"


        crc = obj.pose.bones['bone6'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint11"

        crc = obj.pose.bones['bone6'].constraints.new('DAMPED_TRACK')
        crc.target = obj
        crc.subtarget = "joint12"


        crc = obj.pose.bones['bone7'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint4"

        crc = obj.pose.bones['bone7'].constraints.new('DAMPED_TRACK')
        crc.target = obj
        crc.subtarget = "joint5"


        crc = obj.pose.bones['bone8'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint9"

        crc = obj.pose.bones['bone8'].constraints.new('DAMPED_TRACK')
        crc.target = obj
        crc.subtarget = "joint10"


        crc = obj.pose.bones['bone9'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint4"

        crc = obj.pose.bones['bone9'].constraints.new('DAMPED_TRACK')
        crc.target = obj
        crc.subtarget = "joint9"



        crc = obj.pose.bones['bone10'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint6"

        crc = obj.pose.bones['bone10'].constraints.new('DAMPED_TRACK')
        crc.target = obj
        crc.subtarget = "joint7"


        crc = obj.pose.bones['bone11'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint7"

        crc = obj.pose.bones['bone11'].constraints.new('DAMPED_TRACK')
        crc.target = obj
        crc.subtarget = "joint8"


        crc = obj.pose.bones['bone12'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint12"

        crc = obj.pose.bones['bone12'].constraints.new('DAMPED_TRACK')
        crc.target = obj
        crc.subtarget = "joint13"


        crc = obj.pose.bones['bone13'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint13"

        crc = obj.pose.bones['bone13'].constraints.new('DAMPED_TRACK')
        crc.target = obj
        crc.subtarget = "joint14"


        crc = obj.pose.bones['bone14'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint17"

        crc = obj.pose.bones['bone14'].constraints.new('DAMPED_TRACK')
        crc.target = obj
        crc.subtarget = "joint0"


        crc = obj.pose.bones['bone15'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint16"

        crc = obj.pose.bones['bone15'].constraints.new('DAMPED_TRACK')
        crc.target = obj
        crc.subtarget = "joint2"


        crc = obj.pose.bones['bone16'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint0"

        crc = obj.pose.bones['bone16'].constraints.new('DAMPED_TRACK')
        crc.target = obj
        crc.subtarget = "joint1"

        crc = obj.pose.bones['bone17'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint2"

        crc = obj.pose.bones['bone17'].constraints.new('DAMPED_TRACK')
        crc.target = obj
        crc.subtarget = "joint3"


        obj.parent =  motoOffset
        customShape.parent = motoOffset

    
        return {'FINISHED'}
