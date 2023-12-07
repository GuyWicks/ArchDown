from . import hash_shape, thisname
from .ArchiShape.Business import Business


def test_business_service():
    shape = Business().service(x=5, y=5, text="Business Service")
    assert hash_shape(thisname(), shape) == r"86ede19109323d079ffda6fab606bf04"


def test_business_process():
    shape = Business().process(x=5, y=5, text="Business Process")
    assert hash_shape(thisname(), shape) == r"2480beb4c1842a378b47066ad62f2297"


def test_business_event():
    shape = Business().event(x=5, y=5, text="Business Event")
    assert hash_shape(thisname(), shape) == r"07a41534c46f8b5663ce4c679601f890"
