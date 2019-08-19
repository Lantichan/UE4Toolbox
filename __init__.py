# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "UE4 Toolbox",
    "author" : "Lanti",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (1, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from . export_to_ue4 import exportObj_OT_Operator
from . ue4toolbox_panel import UE4TB_PT_Panel

classes = (exportObj_OT_Operator, UE4TB_PT_Panel)

register, unregister = bpy.utils.register_classes_factory(classes)