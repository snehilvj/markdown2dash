from markdown2dash import parse
import tests.testutils as tu

def test1():
    md = '''
# Header

Lorem
ipsum
'''
    layout = parse(md)
    d = tu.todict(layout)
    tu.dcompare(
        d, [
            {
                'name': 'Title', 
                'children': 'Header'
            }, 
            {
                'name': 'Text', 
                # A single \n does not appear to trigger a line break in rendered output
                'children': ['Lorem', '\n', 'ipsum']
            }
        ]
    )