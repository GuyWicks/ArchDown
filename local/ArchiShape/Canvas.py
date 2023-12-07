import pixie

BACKGROUND = pixie.parse_color("#ffffff")


class Canvas:
    def __init__(
        self,
        height: int = 1024,
        width: int = 780,
    ):
        self._width = width
        self._height = height
        # TODO: Move to super init
        self._image = pixie.Image(width=width, height=height)
        self._image.fill(BACKGROUND)

    def image(self):
        return self._image

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        return None
