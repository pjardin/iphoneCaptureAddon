print("body")
import bpy
from bpy.types import Panel, Operator,Property
import json

import bmesh
from bpy import context



def set_inverse(pbone):

    context_copy = bpy.context.copy()
    context_copy["constraint"] = pbone.constraints["Child Of"]
    bpy.context.active_object.data.bones.active = pbone.bone
    bpy.ops.constraint.childof_set_inverse(context_copy, constraint="Child Of", owner='BONE')

class ConnectMotionOperator(Operator):
    bl_idname = "connect.body_anchor"
    bl_label = "connect"

    def execute(self, context):

        scene = context.scene

        selected = bpy.context.selected_objects

        BMC = context.object # has to be first object selected!!!
        arm = context.object


        for obj in selected:
            
            if "tracked points" in obj.name:
                BMC = obj


        arm.parent = BMC
        arm.matrix_parent_inverse = BMC.matrix_world.inverted()


        #=======================================
        edit_bones = arm.data.edit_bones


        bpy.ops.object.editmode_toggle()

        where = arm.pose.bones["shoulder.R"].tail

        b = edit_bones.new('track1')
        b.head = where
        b.tail = (where.x, where.y, where.z + 0.1)


        where = arm.pose.bones["shoulder.L"].tail

        b = edit_bones.new('track2')
        b.head = where
        b.tail = (where.x, where.y, where.z + 0.1)

        where = arm.pose.bones["upper_arm.R"].tail

        b = edit_bones.new('track3')
        b.head = where
        b.tail = (where.x, where.y, where.z + 0.1)

        where = arm.pose.bones["upper_arm.L"].tail

        b = edit_bones.new('track4')
        b.head = where
        b.tail = (where.x, where.y, where.z + 0.1)

        where = arm.pose.bones["forearm.R"].tail

        b = edit_bones.new('track5')
        b.head = where
        b.tail = (where.x, where.y, where.z + 0.1)

        where = arm.pose.bones["forearm.L"].tail

        b = edit_bones.new('track6')
        b.head = where
        b.tail = (where.x, where.y, where.z + 0.1)

        where = arm.pose.bones["thigh.R"].tail

        b = edit_bones.new('track7')
        b.head = where
        b.tail = (where.x, where.y, where.z + 0.1)

        where = arm.pose.bones["thigh.L"].tail

        b = edit_bones.new('track8')
        b.head = where
        b.tail = (where.x, where.y, where.z + 0.1)

        where = arm.pose.bones["shin.R"].tail

        b = edit_bones.new('track9')
        b.head = where
        b.tail = (where.x, where.y, where.z + 0.1)

        where = arm.pose.bones["shin.L"].tail

        b = edit_bones.new('track10')
        b.head = where
        b.tail = (where.x, where.y, where.z + 0.1)

        where = arm.pose.bones["spine_lower"].tail

        b = edit_bones.new('track11')
        b.head = where
        b.tail = (where.x, where.y, where.z + 0.1)

        where = arm.pose.bones["spine_upper"].tail

        b = edit_bones.new('track12')
        b.head = where
        b.tail = (where.x, where.y, where.z + 0.1)

        where = arm.pose.bones["neck"].tail

        b = edit_bones.new('track13')
        b.head = where
        b.tail = (where.x, where.y, where.z + 0.1)

        bpy.ops.object.editmode_toggle()
        #=======================================


        #=======================================
        crc = arm.pose.bones['shoulder.R'].constraints.new('TRACK_TO')
        crc.target = arm
        crc.subtarget = "track1"
        crc.use_target_z = True

        crc = arm.pose.bones['track1'].constraints.new('CHILD_OF')
        crc.target = BMC
        crc.subtarget = "joint12"
        set_inverse(arm.pose.bones["track1"])


        crc = arm.pose.bones['shoulder.L'].constraints.new('TRACK_TO')
        crc.target = arm
        crc.subtarget = "track2"
        crc.use_target_z = True

        crc = arm.pose.bones['track2'].constraints.new('CHILD_OF')
        crc.target = BMC
        crc.subtarget = "joint6"
        set_inverse(arm.pose.bones["track2"])
        #=======================================
        crc = arm.pose.bones['upper_arm.R'].constraints.new('TRACK_TO')
        crc.target = arm
        crc.subtarget = "track3"
        crc.use_target_z = True

        crc = arm.pose.bones['track3'].constraints.new('CHILD_OF')
        crc.target = BMC
        crc.subtarget = "joint13"
        set_inverse(arm.pose.bones["track3"])

        crc = arm.pose.bones['upper_arm.L'].constraints.new('TRACK_TO')
        crc.target = arm
        crc.subtarget = "track4"
        crc.use_target_z = True

        crc = arm.pose.bones['track4'].constraints.new('CHILD_OF')
        crc.target = BMC
        crc.subtarget = "joint7"
        set_inverse(arm.pose.bones["track4"])
        #=======================================
        crc = arm.pose.bones['forearm.R'].constraints.new('TRACK_TO')
        crc.target = arm
        crc.subtarget = "track5"
        crc.use_target_z = True

        crc = arm.pose.bones['track5'].constraints.new('CHILD_OF')
        crc.target = BMC
        crc.subtarget = "joint14"
        set_inverse(arm.pose.bones["track5"])

        crc = arm.pose.bones['forearm.L'].constraints.new('TRACK_TO')
        crc.target = arm
        crc.subtarget = "track6"
        crc.use_target_z = True

        crc = arm.pose.bones['track6'].constraints.new('CHILD_OF')
        crc.target = BMC
        crc.subtarget = "joint8"
        set_inverse(arm.pose.bones["track6"])
        #=======================================
        crc = arm.pose.bones['thigh.R'].constraints.new('TRACK_TO')
        crc.target = arm
        crc.subtarget = "track7"
        crc.use_target_z = True

        crc = arm.pose.bones['track7'].constraints.new('CHILD_OF')
        crc.target = BMC
        crc.subtarget = "joint2"
        set_inverse(arm.pose.bones["track7"])

        crc = arm.pose.bones['thigh.L'].constraints.new('TRACK_TO')
        crc.target = arm
        crc.subtarget = "track8"
        crc.use_target_z = True

        crc = arm.pose.bones['track8'].constraints.new('CHILD_OF')
        crc.target = BMC
        crc.subtarget = "joint0"
        set_inverse(arm.pose.bones["track8"])
        #=======================================
        crc = arm.pose.bones['shin.R'].constraints.new('TRACK_TO')
        crc.target = arm
        crc.subtarget = "track9"
        crc.use_target_z = True

        crc = arm.pose.bones['track9'].constraints.new('CHILD_OF')
        crc.target = BMC
        crc.subtarget = "joint3"
        set_inverse(arm.pose.bones["track9"])

        crc = arm.pose.bones['shin.L'].constraints.new('TRACK_TO')
        crc.target = arm
        crc.subtarget = "track10"
        crc.use_target_z = True

        crc = arm.pose.bones['track10'].constraints.new('CHILD_OF')
        crc.target = BMC
        crc.subtarget = "joint1"
        set_inverse(arm.pose.bones["track10"])
        #=======================================
        crc = arm.pose.bones['spine_lower'].constraints.new('TRACK_TO')
        crc.target = arm
        crc.subtarget = "track11"
        crc.use_target_z = True

        crc = arm.pose.bones['track11'].constraints.new('CHILD_OF')
        crc.target = BMC
        crc.subtarget = "joint4"
        set_inverse(arm.pose.bones["track11"])

        crc = arm.pose.bones['spine_upper'].constraints.new('TRACK_TO')
        crc.target = arm
        crc.subtarget = "track12"
        crc.use_target_z = True

        crc = arm.pose.bones['track12'].constraints.new('CHILD_OF')
        crc.target = BMC
        crc.subtarget = "joint9"
        set_inverse(arm.pose.bones["track12"])

        crc = arm.pose.bones['neck'].constraints.new('TRACK_TO')
        crc.target = arm
        crc.subtarget = "track13"
        crc.use_target_z = True

        crc = arm.pose.bones['track13'].constraints.new('CHILD_OF')
        crc.target = BMC
        crc.subtarget = "joint10"
        set_inverse(arm.pose.bones["track13"])
        #=======================================






        return {'FINISHED'}


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
        frame = 0
        
        originaLocation = [ -move["moto"][0][15][0],move["moto"][0][15][2],move["moto"][0][15][1]]
        
        zOffset = -move["moto"][0][1][2]
        
        if zOffset > -move["moto"][0][3][2]:
            zOffset = -move["moto"][0][3][2]
        offset = [0,0, -zOffset * 10 + .2]
        
        #print(originaLocation)
        #return {'FINISHED'}
    
        for f in move["moto"]:
            
            joint = 0
            
            for b in f:
                
                if (joint < 15):
                    bone = obj.pose.bones['joint'+ str(joint)]
                      
                    bone.location = [-b[0] / 100000,b[1] / 100000,-b[2] / 100000]
                    bone.keyframe_insert('location', frame=move["frame"][frame][0][0] + scene.my_tool.startFrame)
                    
                    
                elif (joint == 15):
                    obj.location = [ (-b[0] - originaLocation[0] + offset[0]) / 100000,
                        (b[2]- originaLocation[1] + offset[1]) / 100000,
                        (b[1] - originaLocation[2] + offset[2]) / 100000]
                    obj.keyframe_insert('location', frame=move["frame"][frame][0][0] + scene.my_tool.startFrame)
                elif (joint == 16):
                    obj.rotation_euler = [b[2] / 100, -b[1] / 100, -b[0] / 100]
                    obj.keyframe_insert('rotation_euler', frame= move["frame"][frame][0][0] + scene.my_tool.startFrame)

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

        b = edit_bones.new('bone18')
        b.tail = (-0.179,0,0)
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

        crc = obj.pose.bones['bone3'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint4"
        crc.use_target_z = True



        crc = obj.pose.bones['bone4'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint4"

        crc = obj.pose.bones['bone4'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint11"
        crc.use_target_z = True

        crc = obj.pose.bones['bone5'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint5"

        crc = obj.pose.bones['bone5'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint6"
        crc.use_target_z = True

        crc = obj.pose.bones['bone6'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint11"

        crc = obj.pose.bones['bone6'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint12"
        crc.use_target_z = True

        crc = obj.pose.bones['bone7'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint4"

        crc = obj.pose.bones['bone7'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint5"
        crc.use_target_z = True




        crc = obj.pose.bones['bone8'].constraints.new('COPY_ROTATION')
        crc.target = obj
        crc.subtarget = "bone9"
        crc.target_space = 'POSE'
        crc.owner_space = 'POSE'

        crc = obj.pose.bones['bone8'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint9"

        crc = obj.pose.bones['bone8'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint10"
        crc.use_target_z = True




        crc = obj.pose.bones['bone9'].constraints.new('COPY_ROTATION')
        crc.target = obj
        crc.subtarget = "bone18"
        crc.use_x = False
        crc.use_y = False

        crc.target_space = 'POSE'
        crc.owner_space = 'POSE'



        crc = obj.pose.bones['bone9'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint4"

        crc = obj.pose.bones['bone9'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint9"
        crc.use_target_z = True







        crc = obj.pose.bones['bone10'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint6"

        crc = obj.pose.bones['bone10'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint7"
        crc.use_target_z = True

        crc = obj.pose.bones['bone11'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint7"

        crc = obj.pose.bones['bone11'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint8"
        crc.use_target_z = True

        crc = obj.pose.bones['bone12'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint12"

        crc = obj.pose.bones['bone12'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint13"
        crc.use_target_z = True

        crc = obj.pose.bones['bone13'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint13"

        crc = obj.pose.bones['bone13'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint14"
        crc.use_target_z = True

        crc = obj.pose.bones['bone14'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint17"

        crc = obj.pose.bones['bone14'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint0"
        crc.use_target_z = True

        crc = obj.pose.bones['bone15'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint16"

        crc = obj.pose.bones['bone15'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint2"
        crc.use_target_z = True

        crc = obj.pose.bones['bone16'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint0"

        crc = obj.pose.bones['bone16'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint1"
        crc.use_target_z = True

        crc = obj.pose.bones['bone17'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint2"

        crc = obj.pose.bones['bone17'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint3"
        crc.use_target_z = True



        crc = obj.pose.bones['bone18'].constraints.new('COPY_LOCATION')
        crc.target = obj
        crc.subtarget = "joint5"

        crc = obj.pose.bones['bone18'].constraints.new('TRACK_TO')
        crc.target = obj
        crc.subtarget = "joint11"
        crc.use_target_z = True



        obj.parent =  motoOffset
        customShape.parent = motoOffset


        joint = 0
        
        t_pose = [[12, -43, 11], [10, -88, 3], [-13, -44, 9], [-13, -88, -1], [0, 44, 0], [8, 55, 1], [23, 54, 2], [49, 56, -3], [74, 57, 8], [-1, 57, 1], [-1, 72, 5], [-10, 55, 0], [-24, 53, 1], [-50, 59, 1], [-74, 65, 12], [-34, -14, -313], [19, -3, -18]]
                   
        for b in t_pose:

            if (joint < 15):
                bone = obj.pose.bones['joint'+ str(joint)]

                bone.location = [-b[0] / 100,b[1] / 100,-b[2] / 100]

            joint +=1

    
        return {'FINISHED'}
