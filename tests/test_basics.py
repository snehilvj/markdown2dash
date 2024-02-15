from markdown2dash import parse
import tests.testutils as tu

def test1():
    md = '''
    # Header

    Text.
    Continuation
    '''
    layout = parse(md)
    d = tu.todict(layout)
    assert(
        d == {
            'type': 'Code', 
            # -- A single \n does not appear to trigger a line break, but two do
            'children': {'type': 'str', 'children': '# Header\n\nText.\nContinuation'}
        }
    )