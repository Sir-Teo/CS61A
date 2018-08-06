test = {
  'name': 'obedience',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM obedience LIMIT 10;
          7|Image 2
          the number 7 below.|Image 3
          Choose this option instead|Image 5
          You're not the boss of me!|Image 5
          the number 7 below.|Image 4
          Choose this option instead|Image 4
          the number 7 below.|Image 4
          7|Image 3
          the number 7 below.|Image 5
          Choose this option instead|Image 2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
