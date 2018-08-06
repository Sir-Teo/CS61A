test = {
  'name': 'lets-count',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * from sp18favnum;
          69|31
          sqlite> SELECT * from sp18favpets;
          dog|47
          cat|20
          tiger|16
          panda|11
          dragon|9
          dolphin|5
          elephant|5
          hedgehog|5
          monkey|5
          capybara|4
          sqlite> SELECT * from su18favpets;
          dog|19
          cat|14
          tiger|6
          doge|4
          dolphin|4
          human|4
          panda|3
          red panda|3
          sloth|3
          axolotl|2
          sqlite> SELECT * from su18dog;
          dog|19
          sqlite> SELECT * from su18alldogs;
          dog|34
          sqlite> SELECT * from obedienceimages;
          7|Image 1|8
          7|Image 2|11
          7|Image 3|12
          7|Image 4|8
          7|Image 5|9
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
