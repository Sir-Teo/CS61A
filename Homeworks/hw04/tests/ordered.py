test = {
  'name': 'ordered?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (ordered? '(1 2 3 4 5))
          #t
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (ordered? '(1 5 2 4 3))
          #f
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (ordered? '(2 2))
          #t
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (ordered? '(1 2 2 4 3))
          #f
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw04)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
