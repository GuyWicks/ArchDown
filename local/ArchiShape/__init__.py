import pixie

from .Application import Application

# from .Canvas import Canvas
BACKGROUND = pixie.parse_color("#ffffff")


#
# Superclass that joins up all the lower sub-classes... ?
#
class ArchiShape:
    def __init__(self, width: int = 640, height: int = 800):
        # self._application = Application()
        self._image = pixie.Image(width=width, height=height)
        self._image.fill(BACKGROUND)
        pass

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        return None

    # def canvas(self, width, height):
    #     self._width = width
    #     self._height = height
    #     self._image = Canvas(self._width, self._height)
    #     return self

    def application(self):
        # self._application.image = self.canvas
        return Application(self._image)

    def write_image(self, filename: str):
        self._image.write_file(filename)
