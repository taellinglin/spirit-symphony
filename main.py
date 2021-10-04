from random import randint
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Material
import simplepbr
from panda3d.core import loadPrcFileData


class Base(ShowBase):
    colors = [(1,0,0,1), (0,1,1,1), (1,1,0,1), (1,0,1,1)]
    def __init__(self):
        ShowBase.__init__(self)
        loadPrcFileData('', 'framebuffer-srgb false')
        self.win.set_clear_color((0,0,0,1))
        self.model = loader.load_model("models/glyphs.bam")
        self.model.reparent_to(render)

        taskMgr.add(self.update, "myTask")

    def update(self, task):

      dt = globalClock.get_dt()
      clock = 0.0001
      for r, ring in enumerate(self.model.getChildren()):
            
            ring.setColor(self.colors[randint(0,3)], 1)
            #ring.set_h(ring, dt*r)
            ring.set_h(ring, clock*r)

            #ring.set_p(ring, dt*r)
            ring.set_p(ring, clock*r)

      return task.cont   

base = Base()

base.run()