# -*- coding: utf-8 -*-
import pyglet


class Lines():
    """
        Line between (x1, y1) and (x2, y2)
    """

    def __init__(self, x1, y1, x2, y2, origin=[0, 0]):
        """
            Constructor
        """
        self.lines = pyglet.graphics.vertex_list(2,
            ('v2i', (origin[0] + x1, origin[1] + y1,
            origin[0] + x2, origin[1] + y2))
        )

    def draw(self):
        """
            Draw the object
        """
        self.lines.draw(pyglet.gl.GL_LINES)
