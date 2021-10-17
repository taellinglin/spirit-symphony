import sys
from stageflow.core import Stage
from random import randint, choice
from panda3d.core import TextNode
from panda3d.core import TextFont
from panda3d.core import NodePath
from bgm import BGM
from stageflow import Stage
from stageflow.panda3d import Cutscene

class Room00(Stage):
    def __init__(self, exit_stage = "main_menu"):
        self.exit_stage = exit_stage
        self.colors = [(1,0,0,1), (0,1,1,1), (1,1,0,1), (1,0,1,1)]

    def enter(self, data):
        base.cam.set_hpr(render, (0,0,0))
        base.cam.set_y(0.5)
        base.cam.set_z(3)
        base.cam.set_p(180)
        base.cam.look_at(render)
        self.load_room()
        base.camera.set_hpr(self.interior, 0,0,0)
        base.task_mgr.add(self.update)
        base.accept('escape', sys.exit)
        self.bgm = BGM()
        self.bgm.playMusic()
        
    def load_room(self):
        self.room = base.loader.loadModel("rooms/room00.bam")
        self.interior = self.room.reparent_to(render)
        
    def text_begin(self):
        self.caption = base.loader.loadModel("models/guess_the_letter.bam")
        #self.caption.set_p(180)
        self.caption.set_h(0)
        self.caption.set_r(0)
        self.caption.set_p(180)
        self.caption.set_z(0)
        self.caption.set_y(-0.1)
        self.caption.set_scale(0.1,0.1,0.1)
        self.text_caption = self.caption.reparent_to(render)
        #self.text_caption.set_scale(0.1,0.1,0.1)
    
   


    def update(self, task):
        dt = globalClock.get_dt()
        base.cam.look_at(render)
        base.camera.set_h(0.5)
       #base.cam.set_r(180)
        #self.next_letter()
        #self.letterbox.set_h(self.letterbox, 60)
        #for l, letter in enumerate(self.letterbox.get_children()):
        #    letter.set_color(choice(self.colors))
            #letter.set_h(self.letterbox, 60)
            #letter.set_r(self.letterbox, 60)
            #letter.set_z(l*0.2)
        
        
        #This part I need help with:
        #for c, char in enumerate(self.caption.get_children()):
            #char.set_y(render, 0.05)
        #    char.set_color(choice(self.colors))
        return task.cont