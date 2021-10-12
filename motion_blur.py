from panda3d.core import CardMaker


class MotionBlur():
    def __init__(self):
        base.win.set_clear_color_active(False)
        self.cardmaker = CardMaker('background')
        self.cardmaker.set_frame(-0.5,0.5,-0.5,0.5)
        self.bg = base.cam.attach_new_node(self.cardmaker.generate())
        self.bg.set_y(512)
        self.bg.set_transparency(True)
        self.bg.set_color((0,0,0,0.1))
        self.bg.set_scale(20000)
