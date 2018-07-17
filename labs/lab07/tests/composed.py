test = {
  'name': 'composed',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> ((composed add-one add-one) 2)
          f2991d685f624ad59b79213e20800653
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two multiply-by-two) 2)
          2ce69256b3a4325ad04f8cf5c5dd6244
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed add-one multiply-by-two) 2)
          b93035e430af620ab1eedc5adaea0a82
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two add-one) 2)
          5c5050141c04dffb4cedd647366d0e59
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed (composed add-one add-one) add-one) 2)
          b93035e430af620ab1eedc5adaea0a82
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed (composed add-one add-one) multiply-by-two) 2)
          5c5050141c04dffb4cedd647366d0e59
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((composed multiply-by-two (composed add-one add-one)) 2)
          2ce69256b3a4325ad04f8cf5c5dd6244
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab07)
      scm> (load 'lab07_extra)
      scm> (define (add-one a) (+ a 1))
      scm> (define (multiply-by-two a) (* a 2))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
