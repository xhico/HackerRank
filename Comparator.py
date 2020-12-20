from functools import cmp_to_key
import json


class Player:
    def __init__(self, name, score):
        self.name, self.score = name, score

    def __repr__(self):
        return json.dumps({"name": self.name, "score": self.score})

    def comparator(a, b):
        if a.score > b.score:
            return -1

        if a.score < b.score:
            return 1

        if a.name < b.name:
            return -1

        if a.name > b.name:
            return 1

        return 0


data = [Player("amy", 100), Player("david", 100), Player("heraldo", 50), Player("aakansha", 75), Player("aleksa", 150)]
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)
