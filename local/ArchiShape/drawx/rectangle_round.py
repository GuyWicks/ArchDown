import os
import pathlib

import pixie

DEFAULT_GRID = 15
DEFAULT_WIDTH = 12
DEFAULT_HEIGHT = 6
DEFAULT_BORDER = 0.75
DEFAULT_RADIUS = 10


BACKGROUND = pixie.parse_color("#ffffff")
CONCEPT_BORDER = pixie.parse_color("#333333")

APPLICATION_FILL = pixie.parse_color("#b5ffff")
TECHNOLOGY_FILL = pixie.parse_color("#c9e7b7")
BUSINESS_FILL = pixie.parse_color("#ffffb5")


class RectangleRound:
    default_typeface = pixie.read_typeface(
        str(
            pathlib.Path(__file__).parent.resolve().joinpath("fonts/Ubuntu-Regular.ttf")
        )
    )

    def __init__(
        self,
        image=None,
        x: int = 0,
        y: int = 0,
        height: int = DEFAULT_HEIGHT,
        width: int = DEFAULT_WIDTH,
        fill_colour=APPLICATION_FILL,
        radius: int = DEFAULT_RADIUS,
        border: int = DEFAULT_BORDER,
        text: str = "",
        glyph: str = "",
    ):
        # TODO: Move to super init
        if image:
            self._image = image
        else:
            self._image = pixie.Image(width=640, height=800)
            self._image.fill(BACKGROUND)

        # Position from origin
        self._x: int = x
        self._y: int = y

        self._width: int = width
        self._height: int = height
        self._radius: int = radius

        self._border_width: int = border
        self._border_colour = CONCEPT_BORDER
        self._fill_colour = fill_colour
        self._text = text
        self._glyph = glyph

    def draw_outer(self):
        ctx = self._image.new_context()

        paint = pixie.Paint(pixie.SOLID_PAINT)
        paint.color = CONCEPT_BORDER
        ctx.fill_style = paint

        ctx.rounded_rect(
            self._x * DEFAULT_GRID,
            self._y * DEFAULT_GRID,
            self._width * DEFAULT_GRID,
            self._height * DEFAULT_GRID,
            self._radius,
            self._radius,
            self._radius,
            self._radius,
        )
        ctx.fill()

        return self

    def draw_inner(self):
        ctx = self._image.new_context()

        paint = pixie.Paint(pixie.SOLID_PAINT)
        paint.color = self._fill_colour
        ctx.fill_style = paint

        ctx.rounded_rect(
            self._x * DEFAULT_GRID + self._border_width,
            self._y * DEFAULT_GRID + self._border_width,
            self._width * DEFAULT_GRID - self._border_width - self._border_width,
            self._height * DEFAULT_GRID - self._border_width - self._border_width,
            self._radius,
            self._radius,
            self._radius,
            self._radius,
        )
        ctx.fill()

        return self

    @staticmethod
    def make_font(typeface, size, color):
        font = typeface.new_font()
        font.size = size
        font.paint.color = color
        return font

    def draw_text(self):
        spans = pixie.SeqSpan()
        spans.append(
            pixie.Span(
                text=self._text,
                font=self.make_font(
                    RectangleRound.default_typeface, 14, CONCEPT_BORDER
                ),
            )
        )

        self._image.arrangement_fill_text(
            arrangement=spans.typeset(
                h_align=pixie.CENTER_ALIGN,
                # v_align=pixie.TOP_ALIGN,
                v_align=pixie.CENTER_ALIGN,
                # v_align=pixie.BOTTOM_ALIGN,
                wrap=True,
                bounds=pixie.Vector2(
                    self._width * DEFAULT_GRID
                    - self._border_width
                    - self._border_width,
                    (self._height - 2) * DEFAULT_GRID
                    - self._border_width
                    - self._border_width,
                ),
            ),
            transform=pixie.translate(
                self._x * DEFAULT_GRID + self._border_width,
                self._y * DEFAULT_GRID + self._border_width + DEFAULT_GRID,
            ),
        )
        return self

    def draw_glyph(self):
        spans = pixie.SeqSpan()
        spans.append(
            pixie.Span(
                text=self._glyph,
                font=self.make_font(
                    RectangleRound.default_typeface, 12, CONCEPT_BORDER
                ),
            )
        )

        self._image.arrangement_fill_text(
            arrangement=spans.typeset(
                h_align=pixie.RIGHT_ALIGN,
                v_align=pixie.TOP_ALIGN,
                wrap=True,
                bounds=pixie.Vector2(
                    self._width * DEFAULT_GRID
                    - self._border_width
                    - self._border_width,
                    self._height * DEFAULT_GRID
                    - self._border_width
                    - self._border_width,
                ),
            ),
            transform=pixie.translate(
                self._x * DEFAULT_GRID + self._border_width - DEFAULT_GRID / 2,
                self._y * DEFAULT_GRID + self._border_width + DEFAULT_GRID / 2,
            ),
        )
        return self

    def draw(self):
        return self.draw_outer().draw_inner().draw_text().draw_glyph()
