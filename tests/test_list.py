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
    tu.dcompare(
        d,  [
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
# --------------------------------------------------------
def test2():
    "Nested unordered list"
    md = '''
* Level 1 a
   * Level 2 a
   * Level 2 b
* Level 1 b
'''
    layout = parse(md)
    d = tu.todict(layout)
    tu.dcompare(
        d, {
            'name': 'List', 
            'children': [
                {
                    'name': 'ListItem', 
                    'children': [
                        'Level 1 a', 
                        {
                            'name': 'List', 
                            'children': [
                                {'name': 'ListItem', 'children': 'Level 2 a'}, 
                                {'name': 'ListItem', 'children': 'Level 2 b'}
                            ], 
                            'type': 'unordered'
                        }
                    ]
                }, 
                {'name': 'ListItem', 'children': 'Level 1 b'}
            ], 
            'type': 'unordered'
        }
    )
# --------------------------------------------------------
def test3():
    "Combination of nesting, emphasis and continuation lines"
    md = '''
* Item 1 *emphasis* normal
with continuation
    * Level 2
with continuation
* Item 2
'''
    layout = parse(md)
    d = tu.todict(layout)
    tu.dcompare(
        d, {
            'name': 'List', 
            'children': [
                {
                    'name': 'ListItem', 
                    'children': [
                        'Item 1 ', 
                        {'name': 'Text', 'children': 'emphasis', 'fs': 'italic', 'style': {'display': 'inline'}}, 
                        ' normal', 
                        '\n', 
                        'with continuation', 
                        {
                            'name': 'List', 
                            'children': {
                                'name': 'ListItem', 
                                'children': ['Level 2', '\n', 'with continuation']
                            }, 
                            'type': 'unordered'
                        }
                    ]
                }, 
                {'name': 'ListItem', 'children': 'Item 2'}
            ], 
            'type': 'unordered'
        }
    )
