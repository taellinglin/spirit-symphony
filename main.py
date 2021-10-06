import sys
import math
from random import randint, choice
from direct.showbase.ShowBase import ShowBase

from panda3d.core import CardMaker
from panda3d.core import TextNode
from panda3d.core import TextFont
from panda3d.core import NodePath
from panda3d.core import DirectionalLight
from panda3d.core import AmbientLight


class Base(ShowBase):
    colors = [(1,0,0,1), (0,1,1,1), (1,1,0,1), (1,0,1,1)]
    def __init__(self):
        ShowBase.__init__(self)
        self.win.set_clear_color((0,0,0,1))
        self.font = loader.load_font('fonts/Daemon_Full_Working.otf')
        self.font.set_render_mode(TextFont.RMSolid)
        base.cam.set_z(32)
        base.cam.look_at(render)

        self.make_glyph_rings()
        self.setup_light()
        self.setup_motion_blur()
        taskMgr.add(self.update)

        self.accept('escape', sys.exit)
        self.accept('f11', self.drop_to_pdb)

    def setup_motion_blur(self):
        base.win.set_clear_color_active(False)
        cardmaker = CardMaker('background')
        cardmaker.set_frame(-0.5,0.5,-0.5,0.5)
        bg = render.attach_new_node(cardmaker.generate())
        bg.set_p(-90)
        bg.set_transparency(True)
        bg.set_color((0,0,0,0.6))
        bg.set_scale(20000)
        bg.set_z(-512)

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

    def make_glyph_rings(self):
        self.rings = []
        center = NodePath('center')
        for r in range(16):
            ring = center.attach_new_node('ring_'+str(r))
            for c in range(16):
                ring.set_h(ring, 360/16)
                glyph_text = TextNode('glyph_'+str(c))
                glyph_text.font = self.font
                glyph_text.text = choice('abcdefghijklmnopqrstuvwxyz')
                glyph_node = render.attach_new_node(glyph_text)
                glyph_node.set_y(math.pi)
                glyph_node.set_sy(0.1)
                glyph_node.set_p(-90) # Flip up
                glyph_node.set_r(90*randint(0,4))
                glyph_node.wrt_reparent_to(ring)
                #glyph_node.flatten_strong()
            ring.set_scale(math.sin(r/math.pi))
            self.rings.append(ring)
        center.reparent_to(render)

    def update(self, task):
        dt = globalClock.get_dt()
        ring_speed = 5
        char_speed = 1000
        for r, ring in enumerate(self.rings):
            ring.set_h(ring, dt*ring_speed*r)
            ring.set_p(ring, dt*ring_speed*r)
            ring.set_scale(16 - r)
            for c, char in enumerate(ring.get_children()):
                #char.set_h(ring,dt*char_speed*c)
                char.set_r(ring, char_speed*r)
                char.set_color(choice((
                    (1,0,0,1),
                    (1,1,0,1),
                    (0,1,0,1),
                    (0,0,1,1),
                    (0,1,1,1),
                    (1,0,1,1),
                )))
        return task.cont

    def drop_to_pdb(self):
        import pdb; pdb.set_trace()


base = Base()
base.run()
