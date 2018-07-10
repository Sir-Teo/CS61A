test = {
  'name': 'Trees',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab06 import *
          >>> t = tree(1, tree(2))
          Error
          >>> t = tree(1, [tree(2)])
          Nothing
          >>> label(t)
          1
          >>> label(branches(t)[0])
          2
          >>> x = branches(t)
          >>> len(x)
          1
          >>> is_leaf(x[0])
          True
          >>> branch = x[0]
          >>> label(t) + label(branch)
          3
          >>> len(branches(branch))
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from lab06 import *
          >>> b1 = tree(5, [tree(6), tree(7)])
          >>> b2 = tree(8, [tree(9, [tree(10)])])
          >>> t = tree(11, [b1, b2])
          >>> for b in branches(t):
          ...     print(label(b))
          5
          8
          >>> for b in branches(t):
          ...     print(is_leaf(branches(b)[0]))
          True
          False
          >>> [label(b) + 100 for b in branches(t)]
          [105, 108]
          >>> [label(b) * label(branches(b)[0]) for b in branches(t)]
          [30, 72]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
