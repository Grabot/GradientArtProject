
from pyglet import window
from pyglet import clock
from pyglet.gl import glColor4f, gl, GL_POLYGON, GL_QUADS, GL_LINES
from pyglet.graphics import draw


class MainWindow(window.Window):
    def __init__(self, width, height, red_array, green_array, blue_array, name):
        window.Window.__init__(self, width, height, name)
        self.height = height
        self.width = width
        self.red_array = red_array
        self.green_array = green_array
        self.blue_array = blue_array

        self.max_red = 0
        for r1 in red_array:
            for r2 in r1:
                red = self.pythagoras(0, r2[0], 0, r2[1])
                if red > self.max_red:
                    self.max_red = red

        self.max_green = 0
        for g1 in green_array:
            for g2 in g1:
                green = self.pythagoras(0, g2[0], 0, g2[1])
                if green > self.max_green:
                    self.max_green = green

        self.max_blue = 0
        for b1 in blue_array:
            for b2 in b1:
                blue = self.pythagoras(0, b2[0], 0, b2[1])
                if blue > self.max_blue:
                    self.max_blue = blue


    def main_loop(self):
        clock.set_fps_limit(30)

        step_x = self.height/len(self.red_array)
        step_y = self.height/len(self.red_array[0])

        timer = 0
        while not self.has_exit:
            self.dispatch_events()
            self.clear()

            # White, so reset the colour
            glColor4f(1, 1, 1, 1)
            gl.glEnable(gl.GL_BLEND)
            gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

            gl.glLineWidth(10)

            # all arrays are the same size
            for x in range(0, len(self.red_array)):
                for y in range(0, len(self.red_array[x])):

                    red = (self.pythagoras(0, self.red_array[x][y][0], 0, self.red_array[x][y][1])/self.max_red)
                    green = (self.pythagoras(0, self.green_array[x][y][0], 0, self.green_array[x][y][1])/self.max_green)
                    blue = (self.pythagoras(0, self.blue_array[x][y][0], 0, self.blue_array[x][y][1])/self.max_blue)

                    if red > green and red > blue:
                        red = red*(1/red)
                        green = green*(1/red)
                        blue = blue*(1/red)
                    elif green > red and green > blue:
                        red = red*(1/green)
                        green = green*(1/green)
                        blue = blue*(1/green)
                    elif blue > red and blue > green:
                        red = red*(1/blue)
                        green = green*(1/blue)
                        blue = blue*(1/blue)

                    glColor4f(red, green, blue, 1)
                    x_pos = (x*step_x + (step_x/2))
                    y_pos = (y*step_y + (step_y/2))

                    line_pos = self.red_array[x][y] + self.green_array[x][y] + self.blue_array[x][y]

                    x_begin = x_pos-(line_pos[0]/2)
                    y_begin = y_pos-(line_pos[1]/2)
                    x_end = x_pos+(line_pos[0]/2)
                    y_end = y_pos+(line_pos[1]/2)

                    draw(4, GL_LINES, ('v2f', (0, 0, 0, 0,
                                 x_begin, y_begin, x_end, y_end)))
            # glColor4f(0, 1, 0, 1)
            # draw(4, GL_LINES, (
            #     'v2f', (0, 0, 0, 0, 300, 100, 100, 300)))

            glColor4f(0, 0, 0, 1.0)
            clock.tick()


    def pythagoras(self, x_1, x_2, y_1, y_2):
        return pow((y_2-y_1), 2) + pow((x_2-x_1), 2)