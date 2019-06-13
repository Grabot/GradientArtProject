
from pyglet import window
from pyglet import clock
from pyglet.gl import glColor4f, gl, GL_POLYGON, GL_QUADS, GL_LINES
from pyglet.graphics import draw


class MainWindow(window.Window):
    def __init__(self, width, height, draw_array, name):
        window.Window.__init__(self, width, height, name)
        self.height = height
        self.width = width
        self.draw_array = draw_array


    def main_loop(self):
        clock.set_fps_limit(30)

        step_x = self.height/len(self.draw_array)
        step_y = self.height/len(self.draw_array[0])

        timer = 0
        while not self.has_exit:
            self.dispatch_events()
            self.clear()

            # White, so reset the colour
            glColor4f(1, 1, 1, 1)
            gl.glEnable(gl.GL_BLEND)
            gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

            gl.glLineWidth(30)

            for x in range(0, len(self.draw_array)):
                for y in range(0, len(self.draw_array[x])):
                    glColor4f(1, 0, 0, 1)
                    x_pos = (x*step_x + (step_x/2))
                    y_pos = (y*step_y + (step_y/2))

                    x_begin = x_pos-(self.draw_array[x][y][0]/2)
                    y_begin = y_pos-(self.draw_array[x][y][1]/2)
                    x_end = x_pos+(self.draw_array[x][y][0]/2)
                    y_end = y_pos+(self.draw_array[x][y][1]/2)

                    draw(4, GL_LINES, ('v2f', (0, 0, 0, 0,
                                 x_begin, y_begin, x_end, y_end)))
            # glColor4f(0, 1, 0, 1)
            # draw(4, GL_LINES, (
            #     'v2f', (0, 0, 0, 0, 300, 100, 100, 300)))

            glColor4f(0, 0, 0, 1.0)
            clock.tick()
