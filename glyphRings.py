import math
from direct.showbase.ShowBase import ShowBase
from panda3d.core import NodePath
from panda3d.core import TextNode
from random import randint, choice
class GlyphRings(ShowBase):
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
                glyph_node.set_p(90) # Flip up
                glyph_node.set_two_sided(1)
                #glyph_node.set_r(90*randint(0,4))
                glyph_node.wrt_reparent_to(ring)
                glyph_node.flatten_strong()
            ring.set_scale(math.sin(r))
            self.rings.append(ring)
        center.reparent_to(render)