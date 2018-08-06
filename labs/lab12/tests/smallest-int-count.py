test = {
  'name': 'smallest-int-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM smallest_int_count LIMIT 50;
          1|37
          2|3
          3|8
          4|5
          5|2
          6|4
          7|14
          8|3
          9|2
          11|8
          12|2
          13|2
          14|5
          15|1
          16|1
          17|2
          18|4
          19|4
          20|1
          21|2
          22|3
          23|8
          24|1
          26|3
          27|2
          29|2
          31|1
          32|3
          33|2
          34|3
          35|1
          36|1
          37|1
          38|1
          39|1
          42|1
          44|1
          47|2
          53|1
          58|1
          68|1
          74|1
          87|1
          89|1
          97|1
          112|1
          420|1
          698|1
          42069|1
          2147483647|2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab12_extra.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
