from icecream import ic
from textx import (
    get_children_of_type,
    metamodel_from_file,
)
from pprint import pprint as pp


class Assignment:
    def __init__(self, parent, name):  # remember to include parent param.
        self.parent = parent
        self.name = name


mm = metamodel_from_file("./grammar/archimate.tx", classes=[Assignment])
model = mm.model_from_file("./model/test.archimate")

# At this point model is a plain Python object graph with instances of
# dynamically created classes and attributes following the grammar.


def cname(o):
    return o.__class__.__name__
