from . import hash_filename, thisname
from .ArchiShape import ArchiShape
from .ArchiShape.Canvas import Canvas


def test_canvas_assign():
    canvas = Canvas(width=640, height=800)


def test_canvas_with():
    with Canvas(width=640, height=800) as canvas:
        canvas.image()


def test_ArchiShape_application():
    with ArchiShape() as archi:
        archi.application().interface(x=5, y=5, text="GET product")
        archi.application().component(x=5, y=15, text="Product Application")
        archi.application().service(x=5, y=25, text="Product Service")
        archi.application().event(x=25, y=5, text="Product Event")
        archi.application().process(x=25, y=15, text="Product Process")
        archi.application().dataobject(x=25, y=25, text="Data Object")
        archi.write_image(f"output/{thisname()}.png")

        assert hash_filename(name=thisname()) == r"115648b739418074fb75d1b441e723df"
