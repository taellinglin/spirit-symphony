import sys
from typing import KeysView
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
        self.player_score = 0

    def enter(self, data):
        base.cam.set_hpr(render, (0,0,0))
        base.cam.set_y(0.5)
        base.cam.set_z(3)
        base.cam.set_p(180)
        base.cam.look_at(render)
        self.text_begin()
        self.show_letter()
        self.load_room()
        self.show_score()
        base.camera.set_hpr(self.caption, 0,0,0)
        base.task_mgr.add(self.update)
        base.accept('escape', sys.exit)
        base.accept('enter', self.next_letter)
        base.accept("a", lambda: self.check_letter("a"))
        base.accept("b", lambda: self.check_letter("b"))
        base.accept("c", lambda: self.check_letter("c"))
        base.accept("d", lambda: self.check_letter("d"))
        base.accept("e", lambda: self.check_letter("e"))
        base.accept("f", lambda: self.check_letter("f"))
        base.accept("g", lambda: self.check_letter("g"))
        base.accept("h", lambda: self.check_letter("h"))
        base.accept("i", lambda: self.check_letter("i"))
        base.accept("j", lambda: self.check_letter("j"))
        base.accept("k", lambda: self.check_letter("k"))
        base.accept("l", lambda: self.check_letter("l"))
        base.accept("m", lambda: self.check_letter("m"))
        base.accept("n", lambda: self.check_letter("n"))
        base.accept("o", lambda: self.check_letter("o"))
        base.accept("p", lambda: self.check_letter("p"))
        base.accept("q", lambda: self.check_letter("q"))
        base.accept("r", lambda: self.check_letter("r"))
        base.accept("s", lambda: self.check_letter("s"))
        base.accept("t", lambda: self.check_letter("t"))
        base.accept("u", lambda: self.check_letter("u"))
        base.accept("v", lambda: self.check_letter("v"))
        base.accept("w", lambda: self.check_letter("w"))
        base.accept("x", lambda: self.check_letter("x"))
        base.accept("y", lambda: self.check_letter("y"))
        base.accept("z", lambda: self.check_letter("z"))
        self.bgm = BGM()
        self.bgm.playMusic()
        

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
        self.letterbox.set_r(180)
        self.letterbox.set_y(0.2)
        self.letterbox.set_color(choice(self.colors))
        
    def show_score(self, score = None, font = None):
        if score == None:
            score = 0
        if font == None:
           font = base.loader.load_font('fonts/text/Festival.otf')
        self.score = TextNode('score_'+str(score))
        self.font = font
        self.score.text = str(score)
        self.score.font = font
        self.scorebox = render.attach_new_node(self.score)
        self.scorebox.set_two_sided(1)
        self.scorebox.flatten_strong()
        self.scorebox.set_scale(0.2,0.1,0.2)
        self.scorebox.set_p(90)
        self.scorebox.set_r(0)
        self.scorebox.set_y(-0.55)
        self.scorebox.set_x(-1)
        
        
    def load_room(self):
        self.room = base.loader.loadModel("rooms/room00.bam")
        self.interior = self.room.reparent_to(render)
        self.room.setTexture(base.loader.loadTexture("graphics/mandala00.png"), 1)
        
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
        self.letterbox.set_r(180)
        self.letterbox.set_y(0.2)
        self.letterbox.set_color(choice(self.colors))

    def check_letter(self, letter):
        if (letter == self.letter.text):
            self.player_score += 1
            print("You guessed right!")
            print(letter)
            print(self.letter)
            self.bgm.playSfx('correct_guess')
            self.next_letter()
            
        else:
            self.player_score -= 1
            print("You guessed wrong!")
            print(letter)
            print(self.letter)
            self.bgm.playSfx('incorrect_guess')
            self.next_letter()
            

    def update(self, task):
        self.score.text = str(self.player_score)
        self.scorebox.set_color(choice(self.colors))
        dt = globalClock.get_dt()
        base.cam.look_at(render)
        base.cam.set_r(180)
        #self.next_letter()
        #self.letterbox.set_h(self.letterbox, 60)
        for l, letter in enumerate(self.letterbox.get_children()):
            letter.set_color(choice(self.colors))
            #letter.set_h(self.letterbox, 60)
            #letter.set_r(self.letterbox, 60)
            #letter.set_z(l*0.2)
        
        
        #This part I need help with:
        for c, char in enumerate(self.caption.get_children()):
            #char.set_y(render, 0.05)
            char.set_color(choice(self.colors))
        return task.cont