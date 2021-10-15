import sys
import math
from direct import showbase

from direct.showbase.ShowBase import ShowBase
from letter_matching import LetterMatching


from stageflow import Flow
from stageflow.panda3d import Panda3DSplash
from stageflow.prefab import Quit

from panda3d.core import TransparencyAttrib
from panda3d.core import CardMaker

from bgm import BGM
from glyph_rings import GlyphRings
from motion_blur import MotionBlur
from direct.gui.OnscreenImage import OnscreenImage

from stageflow import Stage
from stageflow.panda3d import Cutscene


class TitleScreen(Stage):
    def __init__(self, exit_stage = 'main_menu'):
        self.exit_stage = exit_stage

    def enter(self, data):
        self.data = data
        base.accept("enter", base.flow.transition, [self.exit_stage])
        base.cam.set_z(256)
        base.cam.look_at(render)
        self.logo()
        self.press_start()
        self.glyph_rings = GlyphRings(font=base.loader.load_font('fonts/Daemon.otf'))
        self.bgm = BGM()
        self.motion_blur = MotionBlur()
        base.task_mgr.add(self.update)
        base.accept('escape', sys.exit)

    def logo(self):
        self.logo = CardMaker('logo')
        self.logo.set_frame(0 ,0 ,1,1)
        self.imageObject = OnscreenImage(image='graphics/SoulSymphonyLogo.png', pos=(-0.2, 1, 0.5), scale=(1,0.5,0.5))
        self.imageObject.setTransparency(TransparencyAttrib.MAlpha)
        self.bg2 = render.attach_new_node(self.logo.generate())

    def press_start(self):
        press_start = base.loader.loadModel("models/press_start.bam")
        press_start.set_p(90)
        press_start.set_x(-0.55)
        press_start.set_y(-3)
        press_start.set_z(-0.7)
        press_start.set_scale(0.15,0.15,0.75)
        press_start.reparent_to(base.cam2d)
        self.subtitle = press_start

    def torus(self):
        press_start = base.loader.loadModel("models/torus.bam")
        press_start.set_p(90)
        press_start.set_x(-0.55)
        press_start.set_y(-3)
        press_start.set_z(-0.7)
        press_start.set_scale(0.15,0.15,0.75)
        press_start.reparent_to(base.cam2d)

    def update(self, task):
        dt = globalClock.get_dt()
        if self.glyph_rings:
            self.glyph_rings.update(dt)
        base.camera.set_hpr(base.camera, (0.05, 0.05, 0.05))
        base.cam.look_at(render)
        return task.cont

    def exit(self, data):
        self.subtitle.detachNode()
        self.glyph_rings.center.detachNode()
        self.bg2.detachNode()
        self.imageObject.detachNode()
        return data

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
