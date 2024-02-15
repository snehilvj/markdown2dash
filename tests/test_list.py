from markdown2dash import parse
import tests.testutils as tu

def test1():
    "Single-level unordered list"
    md = '''
Prior line
* Item 1
* Item 2
'''
    layout = parse(md)
    d = tu.todict(layout)
    assert(
        d == [
            {
                'name': 'Text', 
                'children': 'Prior line'
            }, 
            {
                'name': 'List',
                'type': 'unordered', 
                'children': [
                    {'name': 'ListItem', 'children': 'Item 1'},
                    {'name': 'ListItem', 'children': 'Item 2'}
                ]
            }
        ]
    )