class Record:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name


RECORDS = [
    Record(1, 'Zaylee Williamson'),
    Record(2, 'Emerson Beltran'),
    Record(3, 'Kaydence Hutchinson'),
    Record(4, 'Korbin O’Neal'),
    Record(5, 'Treasure Dyer'),
    Record(6, 'Atreus Webb'),
    Record(7, 'Ariella Norman'),
    Record(8, 'Aziel Carey'),
    Record(9, 'Alora Benton'),
    Record(10, 'Jamal Frye'),
]


def fetch(query):
    records = {}

    for term in query.lower().split():
        records.update({record.id: record for record in RECORDS if term in record.name.lower()})

    return [*records.values()]
