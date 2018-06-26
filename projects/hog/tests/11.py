test = {
  'name': 'Question 11',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> swap_strategy(11, 20, 8, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(19, 11, 2, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(30, 54, 3, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(7, 24, 8, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(6, 38, 6, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from tests.check_strategy import check_strategy
          >>> check_strategy(swap_strategy)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> swap_strategy(10, 35, 5, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(12, 21, 3, 6)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(44, 37, 8, 6)
          6
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> swap_strategy(27, 99, 8, 6)
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
