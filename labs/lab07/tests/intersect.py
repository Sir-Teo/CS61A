test = {
  'name': 'intersect',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> ((intersect add-two square) 2)
          22366cc874047a10e8dc566d9bd86d5f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((intersect add-two square) 3)
          3c6c80f70953f551231b2e51b4d9b1ce
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((intersect (lambda (x) (* 5 x)) square) 5)
          22366cc874047a10e8dc566d9bd86d5f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((intersect (lambda (x) x) square) 1)
          22366cc874047a10e8dc566d9bd86d5f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((intersect square (lambda (x) x)) 1)
          22366cc874047a10e8dc566d9bd86d5f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((intersect (lambda (x) x) square) 5)
          3c6c80f70953f551231b2e51b4d9b1ce
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> ((intersect (lambda (x) (/ x 1)) (lambda (x) x)) -1)
          22366cc874047a10e8dc566d9bd86d5f
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
      scm> (define (add-two a) (+ a 2))
      scm> (define (square a) (* a a))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
