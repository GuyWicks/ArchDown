from .rectangle_round import RectangleRound


def test_001_round_rectangle():
    rec = RectangleRound(x=5, y=5,).draw()
    rec._image.write_file("output/rounded_rectangle_001.png")


def test_002_with_text():
    rec = RectangleRound(x=5, y=5, text="Hello World",).draw()
    rec._image.write_file("output/rounded_rectangle_002.png")


def test_003_with_long_text():
    rec = RectangleRound(
        x=5,
        y=5,
        text="Hello World\nGuy Wicks\nwas here\nthis is a long line that overflows a single line",
    ).draw()
    rec._image.write_file("output/rounded_rectangle_003.png")


def test_004_square_with_glyph():
    rec = RectangleRound(
        x=5,
        y=5,
        radius=0,
        text="Application",
        glyph="=[]",
    ).draw()
    rec._image.write_file("output/rounded_rectangle_004.png")


def test_005_square_with_glyph():
    rec = RectangleRound(
        x=5,
        y=5,
        radius=0,
        text="Application",
        glyph="-O",
    ).draw()
    rec._image.write_file("output/rounded_rectangle_005.png")


def test_006_service():
    rec = RectangleRound(
        x=5,
        y=5,
        radius=15 * 5,
        text="Service",
    ).draw()
    rec._image.write_file("output/rounded_rectangle_006.png")
