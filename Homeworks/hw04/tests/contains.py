test = {
  'name': 'contains?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (contains? odds 3)
          #t
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (contains? odds 9)
          #t
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (contains? odds 6)
          #f
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw04)
      scm> (define odds (list 3 5 7 9))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
