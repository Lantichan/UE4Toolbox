import bpy

class UE4TB_PT_Panel(bpy.types.Panel):
    bl_idname = "UE4TB_PT_Panel"
    bl_label = "UE4 Toolbox"
    bl_category = "UE4 Toolbox"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator('view3d.export_to_ue4', text="Export to UE4 (.fbx)")

