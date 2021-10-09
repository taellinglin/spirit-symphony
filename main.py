import sys
import math
from random import randint, choice
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenImage import OnscreenImage

from panda3d.core import TransparencyAttrib
from panda3d.core import CardMaker
from panda3d.core import DirectionalLight
from panda3d.core import AmbientLight


import bgm
from glyphRings import GlyphRings


class Base(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.win.set_clear_color((0,0,0,1))
        self.disable_mouse()
        base.cam.set_z(128)
        base.cam.look_at(render)

        self.glyph_rings = GlyphRings(font=loader.load_font('fonts/Daemon_Full_Working.otf'))

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

    def update(self, task):
        dt = globalClock.get_dt()
        self.glyph_rings.update(dt)
        self.camera.set_hpr(self.camera, (0.01, 1, 0.5))
        base.cam.look_at(render)
        return task.cont

    def drop_to_pdb(self):
        import pdb; pdb.set_trace()


base = Base()
music = [
    base.loader.loadSfx("music/Flag.ogg"),
    base.loader.loadSfx("music/Excellent.ogg"),
    base.loader.loadSfx("music/FlagTracker.ogg"),
    base.loader.loadSfx("music/HallofSunrise.ogg"),
    base.loader.loadSfx("music/NotaGoodbye.ogg"),
    base.loader.loadSfx("music/SpaceField.ogg"),
    base.loader.loadSfx("music/StarlightVocals.ogg"),
    base.loader.loadSfx("music/Trich.ogg"),
    base.loader.loadSfx("music/WalkThePath.ogg"),
    base.loader.loadSfx("music/Whisper.ogg"),
    base.loader.loadSfx("music/WishingWell.ogg"),
    base.loader.loadSfx("music/Womper.ogg"),
    base.loader.loadSfx("music/YouMightBeRight.ogg")
]
sfx = [
    base.loader.loadSfx("audio/soul-symphony.wav")
]

base.playSfx(sfx[0],0,1, None, 0)
base.playMusic(music[randint(0, 12)],1,1,None,0)
logo = CardMaker('logo')
logo.set_frame(0 ,0 ,1,1)
imageObject = OnscreenImage(image='graphics/SoulSymphonyLogo.png', pos=(-0.2, 1, 0.5), scale=(1,0.5,0.5))
imageObject.setTransparency(TransparencyAttrib.MAlpha)

bg2 = render.attach_new_node(logo.generate())



base.run()
