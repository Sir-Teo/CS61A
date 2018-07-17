test = {
  'name': 'gcd',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (gcd 0 4)
          f2991d685f624ad59b79213e20800653
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 8 0)
          2ce69256b3a4325ad04f8cf5c5dd6244
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 34 19)
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 20 30)
          700368183fe24919898aaeca9b976fbd
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (gcd 40 40)
          8e05377a4831f0232f795834a8e1d6eb
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'lab07)
      scm> (load 'lab07_extra)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
