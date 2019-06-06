
from pyglet import window
from pyglet import clock
from pyglet.gl import glColor4f, gl, GL_POLYGON, GL_QUADS, GL_LINES


class MainWindow(window.Window):
    def __init__(self, width, height, name):
        window.Window.__init__(self, width, height, name)


    def main_loop(self):
        clock.set_fps_limit(30)
        nodeSize = 5

        timer = 0
        while not self.has_exit:
            self.dispatch_events()
            self.clear()

            # White, so reset the colour
            glColor4f(1, 1, 1, 1)
            gl.glLineWidth(1)

            gl.glEnable(gl.GL_BLEND)
            gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

            glColor4f(0, 0, 0, 1.0)
            clock.tick()
