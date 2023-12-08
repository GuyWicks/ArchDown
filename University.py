from icecream import ic
from textx import (
    get_children_of_type,
    metamodel_from_file,
)
from pprint import pprint as pp

mm = metamodel_from_file("./grammar/university.tx")

# At this point model is a plain Python object graph with instances of
# dynamically created classes and attributes following the grammar.


class Computer:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name

    def __str__(self):
        return "{},{}".format(self.name)


model = mm.model_from_file("./model/test.university", classes=[Computer])


def cname(o):
    return o.__class__.__name__


# Let's interpret the model
# for command in model.commands:
#     match cname(command):
#         case "Assignment":
#             print(command.name, "is a", command.type)
#             ic(command.type)

#         case _:
#             print("OTHER", cname(command))
