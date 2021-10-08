class MotionBlur(ShowBase):
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