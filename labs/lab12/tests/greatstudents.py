test = {
  'name': 'greatstudents',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM greatstudents LIMIT 10;
          10/1|blue|lemur|humpback whale|23|42
          4/20|green|sloth|cat|42|4
          4/20|green|sloth|howard dean|42|42
          4/20|green|sloth|cat|42|69
          10/8|blue|dog|gorilla|8|69
          6/16|blue|denero|dog|97|99
          1/23|blue|eagle|griffin|42|69
          12/25|blue|pig|elephant |18|14
          12/25|blue|pig|dog|18|17
          12/25|blue|pig|tiger|18|17
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
