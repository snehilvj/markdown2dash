from markdown2dash import parse
import tests.testutils as tu

def test1():
    md = '''
Normal, *em*, **strong**, ***strong em***, normal
'''
    layout = parse(md)
    d = tu.todict(layout)
    assert(
        d == {
            'name': 'Text', 
            'children': [
                'Normal, ', 
                {'name': 'Text', 'children': 'em', 'fs':'italic'}, 
                ', ', 
                {'name': 'Text', 'children': 'strong', 'weight':'bold'}, 
                ', ', 
                {
                    'name': 'Text', 
                    'fs':'italic',
                    'children': {'name': 'Text', 'children': 'strong em', 'weight':'bold'}
                }, 
                ', normal'
            ]
        }
    )