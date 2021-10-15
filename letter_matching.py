import sys
from stageflow.core import Stage
from random import randint, choice
from panda3d.core import TextNode
from panda3d.core import TextFont

class LetterMatching(Stage):
    def __init__(self, exit_stage = "main_menu"):
        self.exit_stage = exit_stage

    def enter(self, data):
        base.cam.set_z(10)
        base.cam.look_at(render)
        #self.logo()
        #self.press_start()
        self.text_begin()
        self.show_letter(str(choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')), base.loader.load_font('fonts/Daemon.otf'))
        #self.glyph_rings = GlyphRings(font=base.loader.load_font('fonts/Daemon.otf'))
        #self.bgm = BGM()
        #self.motion_blur = MotionBlur()
        base.task_mgr.add(self.update)
        base.accept('escape', sys.exit)
        #base.accept('enter', self.enter(data))

    def text_begin(self):
        text_begin = base.loader.loadModel("models/text_begin.bam")
        text_begin.set_p(90)
        #text_begin.set_x(-0.55)
        #text_begin.set_y(-3)
        #press_start.set_z(-0.7)
        #press_start.set_scale(0.15,0.15,0.75)
        text_begin.reparent_to(render)
    
    def show_letter(self, letter, font):
        self.letter = TextNode('glyph_'+letter)
        self.font = font
        self.letter.text = letter
        self.letter.font = font
        letterbox = render.attach_new_node(self.letter)
        letterbox.set_scale(5,5,5)

    def update(self, task):
        dt = globalClock.get_dt()
        #self.glyph_rings.update(dt)
        #base.camera.set_hpr(base.camera, (0.05, 0.05, 0.05))
        base.cam.look_at(render)
        return task.cont