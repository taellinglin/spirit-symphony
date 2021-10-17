import sys
import math
from direct import showbase
from letterMatching import LetterMatching
from titleScreen import TitleScreen
from room00 import Room00
from intro import Intro
from direct.showbase.ShowBase import ShowBase
from stageflow import Flow
from stageflow.panda3d import Panda3DSplash

from stageflow.prefab import Quit

class Base(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        base.accept('f11', self.drop_to_pdb)

    def drop_to_pdb(self):
        import pdb; pdb.set_trace()


base = Base()
base.disable_mouse()
base.flow = Flow(
    stages=dict(
        splash=Panda3DSplash(exit_stage='title_screen'),
        title_screen=TitleScreen(exit_stage='letter_matching'),
        letter_matching=LetterMatching(exit_stage='intro'),
        intro=Intro(exit_stage='room00'),
        room00=Room00(exit_stage='quit'),
        quit=Quit()
    ),
    initial_stage = 'title_screen',
)
base.run()
