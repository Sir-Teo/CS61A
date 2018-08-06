test = {
  'name': 'matchmaker',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM matchmaker LIMIT 10;
          dinosaur|God's Plan|pastel blue|blue
          dog|Bohemian Rhapsody|red|blue
          dog|Bohemian Rhapsody|red|white
          dog|Bohemian Rhapsody|red|red
          dog|Bohemian Rhapsody|blue|white
          dog|Bohemian Rhapsody|blue|red
          tiger|God's Plan|violet|blue
          human|Everytime We Touch|gray|blackpink
          human|Everytime We Touch|gray|yellow
          sloth|Bohemian Rhapsody|seabreeze|gray
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
