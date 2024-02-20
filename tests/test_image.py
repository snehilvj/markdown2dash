# In case it is being run as a submodule
import sys
sys.path.append('./markdown2dash')

from markdown2dash import parse
import tests.testutils as tu

def test1():
    md = '''
### XKCD  on Python
![XKCD on Python](https://imgs.xkcd.com/comics/python_environment_2x.png)
'''
    layout = parse(md)
    d = tu.todict(layout)
    tu.dcompare(
        d, [
            {'name': 'Title', 'children': 'XKCD  on Python', 'order':3}, 
            {
                'name': 'Text', 
                'children': {
                    'name': 'Image', 
                    'src': 'https://imgs.xkcd.com/comics/python_environment_2x.png', 
                    'alt': 'XKCD on Python', 
                    'styles': {'imageWrapper': {'width': 983}}
                }
            }
        ]
    )