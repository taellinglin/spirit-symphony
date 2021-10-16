import sys
from stageflow.core import Stage
from random import randint, choice
from panda3d.core import TextNode
from panda3d.core import TextFont
from panda3d.core import NodePath
from bgm import BGM
from stageflow import Stage
from stageflow.panda3d import Cutscene

class LetterMatching(Stage):
    def __init__(self, exit_stage = "main_menu"):
        self.exit_stage = exit_stage
        self.colors = [(1,0,0,1), (0,1,1,1), (1,1,0,1), (1,0,1,1)]

    def enter(self, data):
        base.cam.set_y(0.5)
        base.cam.set_z(3)
        base.cam.look_at(render)
        self.text_begin()
        self.show_letter()
        base.task_mgr.add(self.update)
        base.accept('escape', sys.exit)
        base.accept('enter', self.next_letter)
        self.bgm = BGM()
        self.bgm.playMusic()

    def text_begin(self):
        self.caption = base.loader.loadModel("models/guess_the_letter.bam")
        self.caption.set_p(0)
        self.caption.set_z(0)
        self.caption.set_y(-0.1)
        self.caption.set_scale(0.1,0.1,0.1)
        self.text_caption = self.caption.reparent_to(render)
        #self.text_caption.set_scale(0.1,0.1,0.1)
    
    def show_letter(self, letter = None, font = None):
        if letter == None:
            letter = str(choice('abcdefghijklmnopqrstuvwxyz'))
        if font == None:
           font = base.loader.load_font('fonts/konnarian/Daemon.otf')

        self.letter = TextNode('glyph_'+letter)
        self.font = font
        self.letter.text = letter
        self.letter.font = font
        self.letterbox = render.attach_new_node(self.letter)
        self.letterbox.set_two_sided(1)
        self.letterbox.flatten_strong()
        self.letterbox.set_scale(0.5,0.1,0.5)
        self.letterbox.set_p(-90)
        self.letterbox.set_color(choice(self.colors))

    def next_letter(self, letter = None, font = None):
        if self.letterbox:
            self.letterbox.detachNode()
        if letter == None:
            letter = str(choice('abcdefghijklmnopqrstuvwxyz'))
        if font == None:
           font = base.loader.load_font('fonts/konnarian/Daemon.otf')
            
        self.letter = TextNode('glyph_'+letter)
        self.font = font
        self.letter.text = letter
        self.letter.font = font
        #self.letter.set_color(choice(self.colors))
        self.letterbox = render.attach_new_node(self.letter)
        self.letterbox.set_two_sided(1)
        self.letterbox.flatten_strong()
        self.letterbox.set_scale(0.5,0.1,0.5)
        self.letterbox.set_p(-90)
        self.letterbox.set_color(choice(self.colors))


    def update(self, task):
        dt = globalClock.get_dt()
        base.cam.look_at(self.caption)
        #self.next_letter()
        #self.letterbox.set_h(self.letterbox, 60)
        for l, letter in enumerate(self.letterbox.get_children()):
            letter.set_color(choice(self.colors))
            letter.set_h(self.letterbox, 60)
            #letter.set_r(self.letterbox, 60)
            letter.set_z(l*0.2)
        
        
        #This part I need help with:
        for c, char in enumerate(self.caption.get_children()):
            #char.set_y(render, 0.05)
            char.set_color(choice(self.colors))
        return task.cont