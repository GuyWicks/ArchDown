# from .drawx import RectangleRound
import pixie

from .drawx.defaults import DEFAULT_RADIUS
from .drawx.rectangle_round import RectangleRound

BACKGROUND = pixie.parse_color("#ffffff")
BUSINESS_FILL = pixie.parse_color("#ffffb5")


concept_labels = False


class Business:
    def __init__(self, image=None):
        if image:
            self._image = image
        else:
            self._image = pixie.Image(width=640, height=800)
            self._image.fill(BACKGROUND)

    def service(self, x: int = 0, y: int = 0, text: str = "Business Service"):
        return RectangleRound(
            image=self._image,
            x=x,
            y=y,
            fill_colour=BUSINESS_FILL,
            radius=DEFAULT_RADIUS * 5,
            text=text + ("\n[Business Service]" if concept_labels else ""),
        ).draw()

    def process(self, x: int = 0, y: int = 0, text: str = "Business Process"):
        return RectangleRound(
            image=self._image,
            x=x,
            y=y,
            fill_colour=BUSINESS_FILL,
            radius=DEFAULT_RADIUS,
            glyph="=>",
            text=text + ("\n[Business Process]" if concept_labels else ""),
        ).draw()

    def event(self, x: int = 0, y: int = 0, text: str = "Business Event"):
        return RectangleRound(
            image=self._image,
            x=x,
            y=y,
            fill_colour=BUSINESS_FILL,
            radius=DEFAULT_RADIUS,
            glyph="^",
            text=text + ("\n[Business Event]" if concept_labels else ""),
        ).draw()

    def businessobject(self, x: int = 0, y: int = 0, text: str = "Business Object"):
        return RectangleRound(
            image=self._image,
            x=x,
            y=y,
            fill_colour=BUSINESS_FILL,
            radius=0,
            glyph="",
            text=text + ("\n[Business Object]" if concept_labels else ""),
        ).draw()
