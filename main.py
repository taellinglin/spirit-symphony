import sys
import math
from random import randint, choice
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenImage import OnscreenImage

from panda3d.core import TransparencyAttrib
from panda3d.core import CardMaker
from panda3d.core import TextFont
from panda3d.core import DirectionalLight
from panda3d.core import AmbientLight



import bgm
from glyphRings import GlyphRings
class Base(ShowBase):
    colors = [(1,0,0,1), (0,1,1,1), (1,1,0,1), (1,0,1,1)]
    clock = 0
    def __init__(self):
        ShowBase.__init__(self)
        self.win.set_clear_color((0,0,0,1))
        self.font = loader.load_font('fonts/Daemon_Full_Working.otf')
        self.font.set_render_mode(TextFont.RMSolid)
        base.cam.set_z(128)
        base.cam.look_at(render)
        self.logo()
        self.press_start()

        GlyphRings.make_glyph_rings(self)
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
        ring_speed = 0.01
        self.clock += 1
        char_speed = 1
        base.cam.look_at(render)
        for r, ring in enumerate(self.rings):
            ring.set_h(ring, ring_speed*r)
            ring.set_p(ring, ring_speed*r)
            ring.set_scale(2 - r)
            for c, char in enumerate(ring.get_children()):
                #char.set_h(ring,dt*char_speed*c)
                char.set_r(ring, char_speed*r)
                char.set_color(choice((
                   # (1,0,0,1),
                    (1,1,0,1),
                   # (0,1,0,1),
                   # (0,0,1,1),
                    (0,1,1,1),
                    (1,0,1,1),
                    (1,0,0,1)
                )))
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


base.run()
