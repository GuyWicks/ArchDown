# from .drawx import RectangleRound
import pixie

from .drawx.defaults import DEFAULT_RADIUS
from .drawx.rectangle_round import RectangleRound

BACKGROUND = pixie.parse_color("#ffffff")

concept_labels = False


class Application:
    def __init__(
        self,
        image=None,
    ):
        if image:
            self._image = image
        else:
            self._image = pixie.Image(width=640, height=800)
            self._image.fill(BACKGROUND)

    def service(self, x: int = 0, y: int = 0, text: str = "Application Service"):
        return RectangleRound(
            image=self._image,
            x=x,
            y=y,
            radius=DEFAULT_RADIUS * 5,
            text=text + ("\n[Application Service]" if concept_labels else ""),
        ).draw()

    def component(self, x: int = 0, y: int = 0, text: str = "Application Component"):
        return RectangleRound(
            image=self._image,
            x=x,
            y=y,
            radius=0,
            glyph="=[]",
            text=text + ("\n[Application Component]" if concept_labels else ""),
        ).draw()

    def interface(self, x: int = 0, y: int = 0, text: str = "Application Interface"):
        return RectangleRound(
            image=self._image,
            x=x,
            y=y,
            radius=0,
            glyph="-O",
            text=text + ("\n[Application Interface]" if concept_labels else ""),
        ).draw()

    def process(self, x: int = 0, y: int = 0, text: str = "Application Process"):
        return RectangleRound(
            image=self._image,
            x=x,
            y=y,
            radius=DEFAULT_RADIUS,
            glyph="=>",
            text=text + ("\n[Application Process]" if concept_labels else ""),
        ).draw()

    def event(self, x: int = 0, y: int = 0, text: str = "Application Event"):
        return RectangleRound(
            image=self._image,
            x=x,
            y=y,
            radius=DEFAULT_RADIUS,
            glyph="^",
            text=text + ("\n[Application Event]" if concept_labels else ""),
        ).draw()

    def dataobject(self, x: int = 0, y: int = 0, text: str = "Data Object"):
        return RectangleRound(
            image=self._image,
            x=x,
            y=y,
            radius=0,
            glyph="",
            text=text + ("\n[Data Object]" if concept_labels else ""),
        ).draw()
