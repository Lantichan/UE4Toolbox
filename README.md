# UE4Toolbox
The UE4Toolbox is a collection of scripts for convenience when using Blender 2.8 to create assets for Unreal Engine 4.

## Getting Started

Simply download the repository as .zip archive and install it into Blender 2.8 using the Addon menu under Edit -> Preferences. You can then find the UE4Toolbox on the View3D menu (Default Hotkey "N").

## Philosophy

While this is mainly a small hobby project that I saw enough value in to share with the world, I do have some sort of Philosophy behind how I want to provide the functionality of this Addon.

I know there are already some plugins out there that deal with a better integration of Blender into the workflow with Unreal Engine 4. However I found some of them to have a very confusing UI and require some sort of special setup or naming convention to work. That is not my goal here.

The goal of this Toolbox is to provide functions that make the workflow more convenient and quick while not requiring any special setup or in-depth knowledge of some internal naming convention that is unique to the Addon. The only things I want you to know are Blender and Unreal Engine and how they work. That's it.

## Current Functions

### Convenience .fbx export

Usually Objects have to be moved to (0,0,0) before you can export them with the pivot being set correctly in Unreal Engine. Especially in scenes that contain many objects, like a prototype of how the scene is supposed to look like in Unreal Engine, this can be quite the chore. You would have to move every mesh to (0,0,0), export it and move it back to its original position by hand. This function will help you with that.

The "Export to UE4 (.fbx)" Button will open the same file-save dialog that you probably already know from Blender's "Export" menu.
The difference is that by using this button instead of the default .fbx exporter, your currently selected object will be moved into the origin (0,0,0). This happens as soon as you click the button, so you can then just save it as you are used to. 
Once you click the export button in the file-save dialog and saving is completed the mesh will automatically be returned to its original position. You will be returned to the scene-view with an .fbx file on your harddrive, ready to be imported into Unreal Engine with the correct pivot, while your prototype in Blender also remains intact.

It's not a big or groundbreaking feature, but I believe it will save a lot of time in the long run if you are prototyping scenes in Blender and need to get them into Unreal Engine.

## Planned Features

### Export multiple selected objects of a scene using the convenience .fbx exporter
No ETA on this one. I work on the addon as need arises and mainly as a small hobby project.


