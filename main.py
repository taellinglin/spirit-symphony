import sys
import math
from random import randint, choice
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenImage import OnscreenImage

from panda3d.core import TransparencyAttrib
from panda3d.core import CardMaker
from panda3d.core import DirectionalLight
from panda3d.core import AmbientLight


from bgm import BGM
from glyphRings import GlyphRings


class Base(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.win.set_clear_color((0,0,0,1))
        self.disable_mouse()
        base.cam.set_z(128)
        base.cam.look_at(render)
        self.logo()
        self.press_start()

        self.glyph_rings = GlyphRings(font=loader.load_font('fonts/Daemon_Full_Working.otf'))
        self.bgm = BGM()

        self.setup_light()
        self.setup_motion_blur()
        taskMgr.add(self.update)

        self.accept('escape', sys.exit)
        self.accept('f11', self.drop_to_pdb)

    def setup_motion_blur(self):
        base.win.set_clear_color_active(False)
        cardmaker = CardMaker('background')
        cardmaker.set_frame(-0.5,0.5,-0.5,0.5)
        bg = base.cam.attach_new_node(cardmaker.generate())
        bg.set_y(512)
        bg.set_transparency(True)
        bg.set_color((0,0,0,0.05))
        bg.set_scale(20000)
       #bg.set_z(-512)

    def setup_light(self):
        sun = DirectionalLight('sun')
        sun.set_color((1,1,1,1))
        sun_node = render.attach_new_node(sun)
        sun_node.look_at((1,0,-1))

        moon = AmbientLight('moon')
        moon.set_color((0.6,0.6,0.6,1))
        moon_node = render.attach_new_node(moon)

        render.set_light(sun_node)
        render.set_light(moon_node)

    def logo(self):
        logo = CardMaker('logo')
        logo.set_frame(0 ,0 ,1,1)
        imageObject = OnscreenImage(image='graphics/SoulSymphonyLogo.png', pos=(-0.2, 1, 0.5), scale=(1,0.5,0.5))
        imageObject.setTransparency(TransparencyAttrib.MAlpha)
        bg2 = render.attach_new_node(logo.generate())

    def press_start(self):
        press_start = loader.loadModel("models/press_start.bam")
        press_start.set_p(90)
        press_start.set_x(-0.5)
        press_start.set_y(-3)
        press_start.set_z(-0.5)
        press_start.set_scale(0.2,0.2,1)
        press_start.reparent_to(base.cam2d)

    def update(self, task):
        dt = globalClock.get_dt()
        self.glyph_rings.update(dt)
        self.camera.set_hpr(self.camera, (0.01, 1, 0.5))
        base.cam.look_at(render)
        return task.cont

    def drop_to_pdb(self):
        import pdb; pdb.set_trace()


base = Base()
base.run()
