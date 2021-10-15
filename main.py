import sys
import math
from direct import showbase
from letterMatching import LetterMatching
from titleScreen import TitleScreen
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
base.flow = Flow(
    stages=dict(
        splash=Panda3DSplash(exit_stage='title_screen'),
        title_screen=TitleScreen(exit_stage='letter_matching'),
        letter_matching=LetterMatching(exit_stage='quit'),
        quit=Quit()
    ),
    initial_stage = 'splash',
)
base.run()
