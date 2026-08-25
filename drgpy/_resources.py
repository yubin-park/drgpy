from importlib.resources import files


def open_text(filename):
    resource = files("drgpy").joinpath(*filename.split("/"))
    return resource.open("r", encoding="utf-8")
