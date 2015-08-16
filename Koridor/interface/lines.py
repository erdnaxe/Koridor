# -*- coding: utf-8 -*-
import pyglet


class Lines():
    """
        Line between (x1, y1) and (x2, y2)
    """

    def __init__(self, x1, y1, x2, y2, origin, color=[255, 255, 255], width=1):
        """
            Constructor
        """
        self.lines = pyglet.graphics.vertex_list(
                    2,
                    ('v2i', (origin[0] + x1, origin[1] + y1,
                            origin[0] + x2, origin[1] + y2)),
                    ('c3B', (color[0], color[1], color[2],
                            color[0], color[1], color[2]))
        )
        self.width = width

    def draw(self):
        """
            Draw the object
        """
        pyglet.graphics.glLineWidth(self.width)
        self.lines.draw(pyglet.gl.GL_LINES)
