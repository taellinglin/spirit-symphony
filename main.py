import sys
import math
from direct import showbase

from direct.showbase.ShowBase import ShowBase


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



class Base(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.cam.set_z(128)
        self.cam.look_at(render)
        self.logo()
        self.press_start()

        self.glyph_rings = GlyphRings(font=loader.load_font('fonts/Daemon.otf'))
        self.bgm = BGM()
        self.motion_blur = MotionBlur()

        taskMgr.add(self.update)
        self.accept('escape', sys.exit)
        self.accept('f11', self.drop_to_pdb)


    def logo(self):
        logo = CardMaker('logo')
        logo.set_frame(0 ,0 ,1,1)
        imageObject = OnscreenImage(image='graphics/SoulSymphonyLogo.png', pos=(-0.2, 1, 0.5), scale=(1,0.5,0.5))
        imageObject.setTransparency(TransparencyAttrib.MAlpha)
        bg2 = render.attach_new_node(logo.generate())

    def press_start(self):
        press_start = self.loader.loadModel("models/press_start.bam")
        press_start.set_p(90)
        press_start.set_x(-0.55)
        press_start.set_y(-3)
        press_start.set_z(-0.7)
        press_start.set_scale(0.15,0.15,0.75)
        press_start.reparent_to(base.cam2d)

    def torus(self):
        press_start = self.loader.loadModel("models/torus.bam")
        press_start.set_p(90)
        press_start.set_x(-0.55)
        press_start.set_y(-3)
        press_start.set_z(-0.7)
        press_start.set_scale(0.15,0.15,0.75)
        press_start.reparent_to(base.cam2d)

    def update(self, task):
        dt = globalClock.get_dt()
        self.glyph_rings.update(dt)
        self.camera.set_hpr(self.camera, (0.05, 0.05, 0.05))
        self.cam.look_at(render)
        return task.cont

    def drop_to_pdb(self):
        import pdb; pdb.set_trace()
base = Base()
#base.flow = Flow(
#    stages=dict(
#        splash=Panda3DSplash(exit_stage='title_screen'),
#        title_screen=base,
#        quit=Quit()
#    ),
#    initial_stage = 'splash',
#)
base.run()