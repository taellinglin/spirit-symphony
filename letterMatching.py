import sys
from stageflow.core import Stage
from random import randint, choice
from panda3d.core import TextNode
from panda3d.core import TextFont

from stageflow import Stage
from stageflow.panda3d import Cutscene

class LetterMatching(Stage):
    def __init__(self, exit_stage = "main_menu"):
        self.exit_stage = exit_stage

    def enter(self, data):
        base.cam.set_z(10)
        base.cam.look_at(render)
        self.text_begin()
        self.show_letter()
        base.task_mgr.add(self.update)
        base.accept('escape', sys.exit)
        base.accept('enter', self.next_letter())

    def text_begin(self):
        text_begin = base.loader.loadModel("models/text_begin.bam")
        text_begin.set_p(90)
        text_begin.reparent_to(render)
    
    def show_letter(self, letter = str(choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')), font = base.loader.load_font('fonts/Daemon.otf')):
        self.letter = TextNode('glyph_'+letter)
        self.font = font
        self.letter.text = letter
        self.letter.font = font
        self.letterbox = render.attach_new_node(self.letter)
        self.letterbox.set_scale(5,5,5)

    def next_letter(self, letter = str(choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')), font = base.loader.load_font('fonts/Daemon.otf')):
        if self.letterbox:
            self.letterbox.detachNode()
        self.letter = TextNode('glyph_'+letter)
        self.font = font
        self.letter.text = letter
        self.letter.font = font
        self.letterbox = render.attach_new_node(self.letter)
        self.letterbox.set_scale(5,5,5)


    def update(self, task):
        dt = globalClock.get_dt()
        base.cam.look_at(render)
        return task.cont