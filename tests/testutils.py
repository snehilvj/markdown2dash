"Utilities to support unit tests"

def todict(layout):
    "Simple partial converter of layout structure to dict"
    if isinstance(layout, list):
        if len(layout) == 1:
            return todict(layout[0])
        else:
            return [todict(item) for item in layout]
    elif not hasattr(layout, 'children'):
        return str(layout)
    else:
        d = {
            "name": type(layout).__name__,
            "children" : todict(layout.children)
        }
        if hasattr(layout, 'type'):
            d.update({"type":layout.type})
        return d