import sys
from stageflow.core import Stage
from random import randint, choice
from panda3d.core import TextNode
from panda3d.core import TextFont
from panda3d.core import NodePath
from bgm import BGM
from stageflow import Stage
from stageflow.panda3d import Cutscene

class Intro(Stage):
    def __init__(self, exit_stage = "main_menu"):
        self.exit_stage = exit_stage
        self.colors = [(1,0,0,1), (0,1,1,1), (1,1,0,1), (1,0,1,1)]
        self.clock = 0
        self.frame_count = 6

    def enter(self, data):
        base.cam.set_hpr(render, (0,0,0))
        base.cam.set_y(0.5)
        base.cam.set_z(3)
        base.cam.set_p(180)
        base.cam.look_at(render)
        self.load_room()
        self.text_begin()
        base.camera.set_hpr(0,0,0)
        base.task_mgr.add(self.update)
        base.accept('escape', sys.exit)
        self.bgm = BGM()
        self.bgm.playMusic()
        
    def load_room(self):
        self.room = base.loader.loadModel("rooms/room00.bam")
        self.room.set_p(90)
        self.room_texture = base.loader.loadTexture("graphics/mandala00.png")
        self.room.setTexture(self.room_texture, 1)
        self.room.reparent_to(render)
        
    def text_begin(self):
        self.caption = base.loader.loadModel("text_chapters/chapter00/frame00.bam")
        self.caption1 = base.loader.loadModel("text_chapters/chapter00/frame01.bam")
        self.caption2 = base.loader.loadModel("text_chapters/chapter00/frame02.bam")
        self.caption3 = base.loader.loadModel("text_chapters/chapter00/frame03.bam")
        self.caption4 = base.loader.loadModel("text_chapters/chapter00/frame04.bam")
        self.caption5 = base.loader.loadModel("text_chapters/chapter00/frame05.bam")
        self.caption6 = base.loader.loadModel("text_chapters/chapter00/frame06.bam")
        
        self.caption.set_h(180)
        self.caption1.set_h(180)
        self.caption2.set_h(180)
        self.caption3.set_h(180)
        self.caption4.set_h(180)
        self.caption5.set_h(180)
        self.caption6.set_h(180)
        
        self.caption.set_r(0)
        self.caption1.set_r(0)
        self.caption2.set_r(0)
        self.caption3.set_r(0)
        self.caption4.set_r(0)
        self.caption5.set_r(0)
        self.caption6.set_r(0)
        
        self.caption.set_p(0)
        self.caption1.set_p(0)
        self.caption2.set_p(0)
        self.caption3.set_p(0)
        self.caption4.set_p(0)
        self.caption5.set_p(0)
        self.caption6.set_p(0)
        
        self.caption.set_z(0)
        self.caption1.set_z(0)
        self.caption2.set_z(0)
        self.caption3.set_z(0)
        self.caption4.set_z(0)
        self.caption5.set_z(0)
        self.caption6.set_z(0)
        
        self.caption.set_y(-0.1)
        self.caption1.set_y(-0.1)
        self.caption2.set_y(-0.1)
        self.caption3.set_y(-0.1)
        self.caption4.set_y(-0.1)
        self.caption5.set_y(-0.1)
        self.caption6.set_y(-0.1)
                           
        self.caption.set_scale(0.18,0.18,0.18)
        self.caption1.set_scale(0.18,0.18,0.18)
        self.caption2.set_scale(0.18,0.18,0.18)
        self.caption3.set_scale(0.18,0.18,0.18)
        self.caption4.set_scale(0.18,0.18,0.18)
        self.caption5.set_scale(0.18,0.18,0.18)
        self.caption6.set_scale(0.18,0.18,0.18)
        
        self.caption.reparent_to(render)
        self.caption1.reparent_to(render)
        self.caption2.reparent_to(render)
        self.caption3.reparent_to(render)
        self.caption4.reparent_to(render)
        self.caption5.reparent_to(render)
        self.caption6.reparent_to(render)
        
        self.frames = [self.caption,self.caption1,self.caption2,self.caption3,self.caption4,self.caption5,self.caption6]
        
    def update(self, task):
        for f, frame in enumerate(self.frames):
            frame.hide()
        if(self.clock >= self.frame_count):
            self.clock = 0
        else:
            self.clock += 0.001
        self.frames[round(self.clock)].show()
        
        dt = globalClock.get_dt()
        base.cam.look_at(render)
        base.camera.set_r(base.camera, 1)
        for l, line in enumerate(self.caption.get_children()):
            line.set_color(choice(self.colors))
        return task.cont