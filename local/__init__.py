import hashlib
import inspect


def thisname():
    return inspect.stack()[1][3]


def hash_shape(name, shape):
    shape._image.write_file(f"output/{name}.png")
    return hashlib.md5(open(f"output/{name}.png", mode="rb").read()).hexdigest()


def hash_filename(name):
    return hashlib.md5(open(f"output/{name}.png", mode="rb").read()).hexdigest()
