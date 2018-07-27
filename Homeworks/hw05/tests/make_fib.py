test = {
  'name': 'make-fib',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define fib (make-fib))
          fib
          scm> (fib)
          0
          scm> (fib)
          1
          scm> (fib)
          1
          scm> (fib)
          2
          scm> (fib)
          3
          scm> (fib)
          5
          scm> (fib)
          8
          scm> (fib)
          13
          scm> (define fib2 (make-fib))
          fib2
          scm> (fib2)
          0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw05)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
