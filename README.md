## Markdown-2-Dash

.. toc::
    :min_level: 3

Markdown-2-Dash or M2D is a standalone package forked out of source code of [official documentation of dash-mantine-components](https://www.dash-mantine-components.com).
Some form of M2D has always existed since the inception of the documentation, but I figured more people can make use of this to document their dash
apps or component libraries.

Have a look [here](https://github.com/snehilvj/markdown2dash/tree/main/preview) to see how this README would look after parsing with M2D. The render also
works perfectly with dark mode without any extra code.

.. admonition::Note
    :icon: radix-icons:info-circled
    :color: red

    The theme switcher has been added only for this demo, its not available as part of markdown2dash.

### Installation

```bash
pip install markdown2dash
```

```bash
poetry add markdown2dash
```

### Quickstart

#### Parsing M2D's README

Let's start by parsing the readme of this repository with M2D.

.. admonition::Note
    :icon: radix-icons:bookmark-filled
    :color: yellow

    Make sure to include stylesheets for all extensions you are planning to use in your app.    

```python
import dash_mantine_components as dmc
from dash import Dash

from markdown2dash import parse

with open("../README.md") as f:
    md = f.read()

layout = parse(md)

stylesheets = [
    "https://unpkg.com/@mantine/dates@7/styles.css",
    "https://unpkg.com/@mantine/code-highlight@7/styles.css",
    "https://unpkg.com/@mantine/charts@7/styles.css",
    "https://unpkg.com/@mantine/carousel@7/styles.css",
    "https://unpkg.com/@mantine/notifications@7/styles.css",
    "https://unpkg.com/@mantine/nprogress@7/styles.css",
]

app = Dash(__name__, external_stylesheets=stylesheets)


app.layout = dmc.MantineProvider(
    dmc.Container(layout, size="lg", p=20),
    theme={
        "primaryColor": "indigo",
        "colorScheme": "light",
        "fontFamily": "'Inter', sans-serif",
        "components": {
            "Table": {"defaultProps": {"striped": True, "withTableBorder": True, "highlightOnHover": True}},
            "Alert": {"styles": {"title": {"fontWeight": 500}}},
        },
    },
)

if __name__ == "__main__":
    app.run()
```

There's no styling by default, so you'll have to provide your own css. You can do that in two ways:
1. Use MantineProvider to style your page (as you can see above)
2. Create CSS files. You can get started with the one provided in this repository: [styles.css]()

Each component rendered by M2D will have a class name attached to it. 

#### Available tokens and class names

M2D can render following types of tokens:

| Token               | Class Name            |
|---------------------|-----------------------|
| Links               | .m2d-link             |
| Paragraph           | .m2d-paragraph        |
| Emphasis            | .m2d-emphasis         |
| Strong              | .m2d-strong           |
| Code Span           | .m2d-codespan         |
| Heading             | .m2d-heading          |
| Thematic Break      | .m2d-thematic-break   |
| Block Code          | .m2d-block-code       |
| Block Quote         | .m2d-block-quote      |
| List Item           | .m2d-list-item        |
| List                | .m2d-list             |
| Strikethrough       | .m2d-strikethrough    |
| Mark                | .m2d-mark             |
| Table               | .m2d-table            |
| Table Head          | .m2d-table-head       |
| Table Body          | .m2d-table-body       |
| Table Row           | .m2d-table-row        |
| Table Cell          | .m2d-table-cell       |
| Spoiler             | .m2d-block-spoiler    |
| Admonition          | .m2d-block-admonition |
| Divider             | .m2d-block-divider    |
| Executable Block    | .m2d-block-exec       |
| Image               | .m2d-block-image      |
| Dash Component Docs | .m2d-block-kwargs     |
| Source Code         | .m2d-block-source     |
| Table of Contents   | .m2d-block-toc        |

### Special Directives

M2D includes some special directives enabling you to do a lot more than just rendering static markdown into a dash layout.

The directives are all extensible, and you can just overwrite the render method to suit your own needs. The default render method is provided in all directives out of the box.

#### Executable Block

You can use the `exec` directive to embed the output of a python script as well as its source code. This directive expects that 
you have stored the output layout in the variable called `component`.

```markdown
.. exec::example.navlink
```

Here's the output if you are viewing this in a dash app:

.. exec::example.navlink

You can hide the source code using the `code` argument, and the border using `border`.

```markdown
.. exec::example.navlink
    :code: false
    :border: false
```

#### Source Code

You can use SourceCode directive to display code from a file in your project. The path of file is relative to current working directory.

Here's the css used to style this page.

```markdown
.. source::markdown2dash/example/assets/styles.css
    :language: css
```

.. source::assets/styles.css
    :language: css

#### Admonition

You can use `admonition` directive to add dmc.Alert components in your page.
Admonition directive uses [DashIconify]() to render icons as well.

```markdown
.. admonition::Alert Title
    :icon: radix-icons:github-logo
    :variant: outline
    
    This is to show that now you can render alerts directly from the markdown.
```

Here's the output if you are viewing this in a dash app:

.. admonition::Alert Title
    :icon: radix-icons:github-logo
    :variant: outline

    This is to show that now you can render alerts directly from the markdown.

#### Image

Render images using dmc.Image like this:

```markdown
.. image::https://www.dash-mantine-components.com/assets/superman.jpeg
    :w: 300px
    :h: 300px
```

Here's the output if you are viewing this in a dash app:

.. image::https://www.dash-mantine-components.com/assets/superman.jpeg
    :w: 300px
    :h: 300px

#### Dash Component API Docs

It's very simple to add API docs of your component using M2D. You just have to specify the package and the component.
Let's create one for DashIconify:

```markdown
.. kwargs::DashIconify
    :library: dash_iconify
```

Here's the output if you are viewing this in a dash app:

.. kwargs::DashIconify
    :library: dash_iconify
 
#### Table of Contents

This directive will parse all the headings and create a table of contents like this:

```python

# a placeholder for self and a list of [<level>, <title>, <id>]
[
    (4, 'Installation', 'installation'),
    (4, 'Quickstart', 'quickstart'), 
    (5, 'Example App', 'example-app'),
    (4, 'Special Directives', 'special-directives'),
    (5, 'Dash Component API Docs', 'dash-component-api-docs'),
    (5, 'Table of Contents', 'table-of-contents')
]
```

This will then be used to render the TOC using the render method. You can enable TOC like this:

```markdown
.. toc::
    :min_level: 3
```

#### Divider

A simple way to add dividers would be to just add `---` in your markdown file.

```markdown
---
```

---

But let's say you to add a label to the divider and also customize it. You can use the divider directive to do that.

```markdown
.. divider::Section Changed!
    :labelPosition: left

.. divider::Section Changed!

.. divider::Section Changed!
    :labelPosition: right
```

.. divider::Section Changed!
    :labelPosition: left

.. divider::Section Changed!

.. divider::Section Changed!
    :labelPosition: right

### More Examples

#### Tasks List

You can create tasks list like below and a checkbox list will be rendered automatically in your dash app.

```markdown
- [ ] Create README for library.
- [x] Resolve GitHub issues [here](https://github.com/snehilvj/dash-mantine-components).
```

- [ ] Create README for library.
- [x] Resolve GitHub issues [here](https://github.com/snehilvj/dash-mantine-components).

#### Spoiler

Create spoiler content like this:

```markdown
>! In the final moments of Dune: Part Two...
>! Why does Paul need to marry Princess Irulan...
>! In the book, we learn that a dea...
```

And this is how it will look when rendered (wrapped by dmc.Spoiler):

>! In the final moments of Dune: Part Two, Paul Atreides does two shocking things: he says he’ll marry Princess Irulan (Florence Pugh), and then, he sends his Fremen troops out into the universe to start a holy war against the great houses. This is the horrific future vision that Paul has been seeing since Dune: Part One. The Fremen and House Atreides prevail on Arrakis, but the cost is a massive war that will burn half the universe. Let's break down how this happens.
>! Why does Paul need to marry Princess Irulan to take over the throne from Emperor Shaddam IV? Because he has control of the spice on Arrakis, couldn’t he just kill everyone and marry Chani, his true love? The answer lies in the book. When Paul sees Irulan in the final pages of the book, he thinks, “There’s my key,” and on the very last page of the book, he tells Chani, “We must obey the forms.” This means that he wants to gain power within the system.
>! In the book, we learn that a deal has been made to “place a Bene Gesserit on the throne, and Irulan is the one they’ve groomed for it.” In the movie, before everything goes down in the end, Reverend Mother Gaius Helen Mohiam tells Irulan that “there’s one way your family can remain in power… are you prepared?”

#### Nested Lists

Let's try to render a mix of items in a nested list.

```markdown
1. Ingredients
   - spaghetti
   - marinara sauce
   - salt
2. Cooking
   1. Bring water to boil, add a pinch of salt and spaghetti.
   2. Cook until pasta is **tender**.
3. Serve: Drain the pasta on a plate. Add heated sauce.
4. No man is lonely eating spaghetti, it requires so much attention.
```

1. Ingredients
   - spaghetti
   - marinara sauce
   - salt
2. Cooking
   1. Bring water to boil, add a pinch of salt and spaghetti.
   2. Cook until pasta is **tender**.
3. Serve: Drain the pasta on a plate. Add heated sauce.
4. No man is lonely eating spaghetti, it requires so much attention.

#### Charts

You can use the exec block to add charts in your app. The following block will render a BarChart as defined in example/chart.py

```markdown
.. exec::example.chart
    :code: false
    :border: true
```

.. exec::example.chart
    :code: false
    :border: false

#### Blockquote

> Life is like npm install – you never know what you are going to get.

### Adding your own directives

You can create a new directive by extending the BaseDirective class and creating a new parser. Here's how you can add a
new directive that adds a scroll to top button in the bottom right of your app.

.. source::scroll.py

The associated css class name will be: `m2d-block-scroll`.

And here's how you can use it in the markdown.

```markdown
.. scroll::
```

.. scroll::

.. exec::example.theme
    :code: false
    :border: false
