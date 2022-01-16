from typing import Pattern
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import texture
import sys
app = Ursina()
# grass = load_texture('grass_block.png')
stone = load_texture('stone.png')
brick = load_texture('brick.png')
#dirt = load_texture('dirt_block.png')
swimming = load_texture('skyblue.png')
grass2 = load_texture('grasstexture.png')
Sky1 = load_texture('skyji.png') 
current_texture = grass2
def update():
    global current_texture
    if held_keys['1']: current_texture = grass2
    if held_keys['2']: current_texture = stone
    if held_keys['3']: current_texture = brick
    if held_keys['4']: current_texture = swimming
    if held_keys['q']: sys.exit()
   
        
class sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = Sky1,
            scale = 300,
            double_sided = True
            
        )
class hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'cube',
            scale = (0.2,0.3),
            color = color.gray,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4,-0.4)
        )
  


class voxel(Button):
    def __init__(self,position = (0,0,0),texture = grass2):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1
            )),
            highlight_color = color.cyan
            )
    def input(self,key):
        if self.hovered:
            if key == "left mouse down":
                VOXEL = voxel(position=self.position+mouse.normal,texture = current_texture)
            if key == "right mouse down":
                destroy(self)


        
    








for z in range(20):
    for x in range(20):
        VOXEL = voxel(position=(x,0,z))
player = FirstPersonController()
background = sky()
Hand = hand()
app.run()