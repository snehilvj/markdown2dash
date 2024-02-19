"Utilities to support unit tests"

def todict(layout):
    "Simple partial converter of layout structure to dict"
    if isinstance(layout, list):
        if len(layout) == 1:
            return todict(layout[0])
        else:
            return [todict(item) for item in layout]
    elif hasattr(layout, '__module__') and layout.__module__.split('.')[0] == "dash_mantine_components":   #hasattr(layout, 'children'):
        d = {
            "name": type(layout).__name__,
        }
        if hasattr(layout, 'children'):
            d.update({"children":todict(layout.children)})
        if hasattr(layout, 'type'):
            d.update({"type":layout.type})
        if hasattr(layout, 'fs'):
            d.update({"fs":layout.fs})
        if hasattr(layout, 'weight'):
            d.update({"weight":layout.weight})
        if hasattr(layout, 'src'):
            d.update({"src":layout.src})
        if hasattr(layout, 'alt'):
            d.update({"alt":layout.alt})
        if hasattr(layout, 'style'):
            d.update({"style":layout.style})
        if hasattr(layout, 'styles'):
            d.update({"styles":layout.styles})
        if hasattr(layout, 'order'):
            d.update({"order":layout.order})
        return d
    else:
        return str(layout)

def dcompare(d1, d2, path="(root)"):
    "Comparison of data structures that gives useful info on where a mismatch is"
    if isinstance(d1, list):
        if not isinstance(d2, list):
            assert False, f"At {path}, d1 is a list, d2 is not"
        if len(d1) != len(d2):
            assert False, f"At {path}, d1 length={len(d1)}, d2 length is {len(d2)}"
        for index, (item1, item2) in enumerate(zip(d1, d2)):
            dcompare(item1, item2, f"{path}/[{index}]")
    elif isinstance(d1, dict):
        if not isinstance(d2, dict):
            assert False, f"At {path}, d1 is a dict, d2 is not"
        for key in set(d1) | set(d2):
            dcompare(d1.get(key, None), d2.get(key, None), f"{path}/{key}")
    else:
        assert d1 == d2, f"Mismatch at {path}. d1={d1}, d2={d2}"