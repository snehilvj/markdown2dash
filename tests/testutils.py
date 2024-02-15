"Utilities to support unit tests"

def todict(layout):
    "Simple partial converter of layout structure to dict"
    ltype = type(layout).__name__
    if isinstance(layout, list):
        if len(layout) == 1:
            return todict(layout[0])
        else:
            children = [todict(item) for item in layout]
    elif not hasattr(layout, 'children'):
        children = str(layout)
    else:
        children = todict(layout.children)
    d = {
        "type": ltype,
        "children" : children
    }
    return d