from . import hash_shape, thisname
from .ArchiShape.Application import Application


def test_application_service():
    shape = Application().service(x=5, y=5, text="Application Service")
    assert hash_shape(thisname(), shape) == r"334b8e4a740dfcfcda4cbfcff546de31"


def test_application_component():
    shape = Application().component(x=5, y=5, text="Application Component")
    assert hash_shape(thisname(), shape) == r"828a691d6e1fd83af8aadd851675d07d"


def test_application_interface():
    shape = Application().interface(x=5, y=5, text="Application Interface")
    assert hash_shape(thisname(), shape) == r"ae1e52ea700b087724ddaf17483a8ae2"


def test_application_process():
    shape = Application().process(x=5, y=5, text="Application Process")
    assert hash_shape(thisname(), shape) == r"abf64317eca6336856f0f3b486bbc26a"


def test_application_event():
    shape = Application().event(x=5, y=5, text="Application Event")
    assert hash_shape(thisname(), shape) == r"38e6223d5f4c9ea0df04906741d3a3c8"
