# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy


bl_info = {
    "name": "Swap objects",
    "description": "Swap the positions of two objects",
    "author": "Ray Mairlot",
    "version": (1, 0),
    "blender": (2, 76, 0),
    "location": "3D View> Search> Swap Objects",
    "category": "Object"}

 

def main(self, context):
    
        object1 = bpy.context.selected_objects[0]
        object2 = bpy.context.selected_objects[1]
        
        if self.location:
            object1.location, object2.location = object2.location.copy() , object1.location.copy()

        if self.rotation:    
            object1.rotation_euler, object2.rotation_euler = object2.rotation_euler.copy() , object1.rotation_euler.copy()
        
        if self.scale:        
            object1.scale, object2.scale = object2.scale.copy() , object1.scale.copy()    
       

        
class SwapObjects(bpy.types.Operator):
    """Swaps the positions of two objects"""
    bl_idname = "object.swap_objects"
    bl_label = "Swap Objects"
    bl_options = {"REGISTER", "UNDO"}
    
    rotation = bpy.props.BoolProperty(name ="Rotation", default=True)
    location = bpy.props.BoolProperty(name ="Location", default=True)
    scale = bpy.props.BoolProperty(name ="Scale", default=True)


    @classmethod
    def poll(cls, context):
        return context.mode == "OBJECT" and len(bpy.context.selected_objects) == 2


    def execute(self, context):
        main(self, context)
        return {'FINISHED'}



def register():
    bpy.utils.register_class(SwapObjects)



def unregister():
    bpy.utils.unregister_class(SwapObjects)    

    

if __name__ == "__main__":
    register()
         