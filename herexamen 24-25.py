#DEEL1: Speler
class Player:
    def __init__(self, name, number):
        self.name = str(name)
        self.number = int(number)

    def __eq__(self, other):  ##self is dit object en other is het object waar je mee vergelijkt
        if isinstance(other, Player):
            return self.name == other.name
        return False

    def __lt__(self, other):
        if isinstance(other, Player):
            return self.name < other.name #retourneert true indien het zo is, false indien niet
        else:
            return NotImplemented

    def __str__(self):
        return f"{self.name} ({self.number})"

#test voor deel 1
p1 = Player("Eden Hazard", 10)
p2 = Player("Moussa Dembele", 19)
p3 = Player("Jan Vertonghen", 5)
players = [p1, p2, p3]
print(p1)
print("\nTest eq-methode:")
print(p1 == p2)  #hier roep je de eq methode op door == te gebruiken
print(Player("Eden Hazard", 99) == p1)
print("\nGesorteerde spelers (op rugnummer):")
sorted_players = sorted(players)

#DEEL2 PASS:

class Pass:
    def __init__(self, sender, receiver, nr_of_times):
        self.sender = sender
        self.receiver = receiver
        self.nr_of_times = int(nr_of_times)

    def get_weight(self,nr_of_times):
        return nr_of_times

    def get_start(self, sender):
        return sender

    def get_end(self, receiver):
        return receiver

    def __eq__(self, other):
        if isinstance(other, Pass):
            return self.sender == self.receiver and self.receiver == self.sender
        return False #other is geen Pass dus nooit gelijk

    def __str__(self):
        return f"Pass from {self.sender} to {self.receiver}"

#test voor deel 2

p1 = Player("Eden Hazard", 10)
p2 = Player("Moussa Dembele", 19)
p3 = Player("Jan Vertonghen", 5)
pass1_2 = Pass(p1, p2, 3)
pass2_1 = Pass(p2, p1, 4)
pass2_2 = Pass(p1, p3, 1)

print(pass1_2)
print(pass2_1 == pass2_2) #zal false zijn aangezien receiver en passer niet gelijk zijn
print(pass1_2.get_weight())

#DEEL 3: LINKEDLIST PASS_GRAPH

class PassGraph:
    def __init__(self):
        self.players = []
        self.adj = {} #dict met key sender_naam en value een lijst van passen die vanuit de sender vertrekken

    def add_player(self, player):
        for p in self.players:
            if p.name == player.name: # vergelijken op name, niet op object!
                return                 # speler bestaat al → niets doen
            self.players.append(player) # Speler bestaat nog niet → toevoegen

            if player.name not in self.adj:
                self.adj[player.name] = []  #creatie van dict met key player name

    def has_player(self, speler):
        # Als argument een Player-object is → check op name
        if isinstance(speler, Player):
            for p in self.players:
                if p.name == speler.name:
                    return True
            return False

        elif isinstance(speler, str): #indien speler een string is
            for p in self.players:
                if p.name == speler:
                    return True
            return False

        else: return False  #andere data types worden niet ondersteund

    def get_player(self, name: str):
        for p in self.players:
            if p.name == name:
                return p
            return None

    def add_pass(self, sender, receiver, times: int(1)):
        if times <= 0:
            raise ValueError
        if sender or receiver not in self.players:
            raise ValueError("Both players must be added to the graph before adding a pass.")
        sender_name = sender.name

        # zorg dat er al een lijst bestaat voor deze sender
        if sender_name not in self.adj:
            self.adj[sender_name] = []

        # check of de pass al bestaat --> dan weight verhogen
        for p in self.adj[sender_name]:
            if p.get_end() == receiver:
                p.nr_of_times += times
                return
        # bestaat nog niet --> nieuwe Pass toevoegen
        new_pass = Pass(sender, receiver, times)
        self.adj[sender_name].append(new_pass)

    def get_pass(self, sender_name, receiver_name):
        if sender_name not in self.adj:
            return None
        for p in self.adj[sender_name]: #doorloop elke pas dat deze sender heeft gemaakt
            if p.get_end() == receiver_name: #indien een pass gegeven door sender aankomt bij receiver
                return p  #return dan deze pass

        return None

    def neighbors(self, sender_name):
        if sender_name not in self.adj:
            return []
        else:
            return self.adj[sender_name]

#ANALYSE FUNCTIONS

    def total_weight(self, subset = None):
        # 1. Als subset None is → neem ALLE spelersnamen
        if subset is None:
            subset = [p.name for p in self.players]

        total = 0

        # 2. Loop door alle zenders in de subset
        for sender_name in subset:
            # zender moet uitgaande passes hebben
            if sender_name not in self.adj:
                continue

            # 3. Loop door alle passes van deze zender
            for p in self.adj[sender_name]:
                receiver_name = p.get_end().name

                # 4. telt alleen als receiver óók in subset zit
                if receiver_name in subset:
                    total += p.get_weight()

        return total

    def pass_intensity(self, subset: list[str] | None = None) -> float:
        # 1. Als subset None is: neem alle spelersnamen
        if subset is None:
            subset = [p.name for p in self.players]

        n = len(subset)

        # 2. Speciale case: minder dan 2 spelers → intensiteit = 0.0
        if n < 2:
            return 0.0

        # 3. Teller: totaal aantal passes binnen de subset
        numerator = self.total_weight(subset)

        # 4. Noemer: maximaal aantal mogelijke gerichte passes
        denominator = n * (n - 1)

        # 5. Intensiteit = teller / noemer
        return numerator / denominator


    def top_pairs(self, k: int = 5):
        # verzamel alle Pass-objecten in één lijst
        all_passes = []
        for passes_from_sender in self.adj.values():
            all_passes.extend(passes_from_sender)

        # sorteer op weight (nr_of_times), dalend
        all_passes.sort(key=lambda p: p.get_weight(), reverse=True)

        # geef de top k terug (of minder als er niet genoeg zijn)
        if k <= 0:
            return []
        return all_passes[:k]

    def distribution_from(self, sender_name: str):
        # haal alle uitgaande passes van deze zender op
        passes = self.adj.get(sender_name, [])

        # maak lijst van (receiver_name, count)
        dist = []
        for p in passes:
            receiver_name = p.get_end().name
            count = p.get_weight()
            dist.append((receiver_name, count))

        # sorteer dalend op count
        dist.sort(key=lambda x: x[1], reverse=True)

        return dist

