# All cards available in a standard deck.
from classes import *

# Instructors

james = InstructorCard('James, Voice of Zendikar', 3000, 1500)
jen = InstructorCard('Jen, jathak', 2000, 4000)
mitas = InstructorCard('Mitas, Obelisk the Tormentor', 4000, 4000)
tammy = InstructorCard('Tammy, Collector of Souls', 2500, 3000)

# TAs

alexs = TACard('President Lieutenant Stennet for Senate', 1800, 2200)
alexw = TACard('Alex W, The Overclocked', 2800, 1700)
cameron = TACard('Cameron Sensei', 1500, 3000)
chae = TACard('Chae-Z', 2000, 2000)
chris = TACard('Chris, Caller of Men', 2300, 1700)
christina = TACard('Christina, czhang51', 1700, 1500)
derek = TACard('Derek, The Wan and Only', 2600, 1900)
erica = TACard('Erica, King Kong of the Arena', 1500, 1800)
griffin = TACard('Griffin, gprechter', 2700, 300)
jemin = TACard('Jemin, Destroyer of Belgium', 2100, 2000)
jennifer = TACard('Jennifer, Zzzzzzz', 1400, 2800)
jenny = TACard('Jenny, Dude of Asuh', 2500, 1800)
kevin = TACard('Kevin, Vanquisher of Unclosed Parentheses', 2600, 500)
nancy = TACard('Nancy the Shaw', 2300, 1400)

# Tutors

aaron = TutorCard('Aaron the Airbender', 1900, 1600)
ajan = TutorCard('Ajan, ajanlorenz.adr', 1700, 1100)
amyh = TutorCard('Amy, Always Hung-ry', 2400, 700)
amym = TutorCard('Amy, AmyMendelsohn', 1900, 1500)
asli = TutorCard('Asli, asliakalin', 2000, 1600)
daniel = TutorCard('Daniel, Soylent Guardian', 1800, 1100)
jacob = TutorCard('Super Saiya Jacob', 2200, 1600)
hermish = TutorCard('Hermish, hermishmehta', 2400, 600)
jemmy = TutorCard('Jemmy, The Zhou-ker of Gotham City', 1900, 1300)
jericho = TutorCard('Jericho, Cowboy of Tax Evasion', 1900, 1700)
kate = TutorCard('Kate, The Exponential Runtime of Ra', 1500, 2100)
lauren = TutorCard('Scorin\' Lauren', 2700, 2000)
rachel = TutorCard('Rachel \'Genes of Jeans\' de Jaen', 1100, 2300)
shide = TutorCard('The Sidhe', 2100, 600)
tiffany = TutorCard('Tiffany, A Bridge Troll', 1500, 2100)
wenyuan = TutorCard('Wenyuan, WenyuanMa95', 1300, 1800)

# Professors
denero = ProfessorCard('John DeNero, Protector of Abstraction Barriers', 5000, 5000)

# A standard deck contains all standard cards.
standard_cards = [james, jen, mitas, tammy, alexs, alexw, cameron, chae, chris, christina, derek, erica, griffin, jemin, jennifer, jenny, kevin, nancy, aaron, ajan, amyh, amym, asli, daniel, jacob, hermish, jemmy, jericho, kate, lauren, rachel, shide, tiffany, wenyuan, denero]
standard_deck = Deck(standard_cards)

# The player and opponent's decks are the standard deck by default.
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()