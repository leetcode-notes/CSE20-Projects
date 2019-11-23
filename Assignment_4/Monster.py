class Monster():
    def __init__(self, name, hp=20):
        self.exp = 0
        self.attacks = {'wait': 0}
        self.name = name
        self.known_attacks = {'sneak_attack': 1, 'slash': 2, 'ice_storm': 3, 'fire_storm': 3,
            'whirlwind': 3, 'earthquake': 2, 'double_hit': 4, 'wait': 0}
        self.current_hp = hp
        self.max_hp = hp

    def add_attack(self, attack_name):
        if attack_name in self.known_attacks and attack_name not in self.attacks:
            try:
                assert(len(self.attacks) < 4)
                self.attacks[attack_name] = self.known_attacks.get(attack_name)
                return True
            except:
                #find the min value of self.attacks
                minval = min(self.attacks.keys(), key=(lambda k: self.attacks[k]))
                for keys, values in self.attacks.items():
                    if self.attacks[minval] == values and min(minval, keys) == keys:
                        minval = keys
                del self.attacks[minval]
                self.attacks[attack_name] = self.known_attacks.get(attack_name)
                return True
        else:
            return False

    def remove_attack(self, attack_name):
        if attack_name in self.attacks.keys():
            del self.attacks[attack_name]
            if len(self.attacks) == 0:
                self.attacks['wait'] = 0
            return True
        else:
            return False

    def win_fight(self):
        self.exp+=5
        self.current_hp = self.max_hp

    def lose_fight(self):
        self.exp+=5
        self.current_hp = self.max_hp

class Dragon(Monster):

    def __init__(self, name, hp=20):
        self.name = name
        super().__init__(exp, known_attacks, current_hp, max_hp)

class Ghost(Monster):

    def __init__(self, name, hp=20):
        self.name = name
        super().__init__(exp, known_attacks, current_hp, max_hp)

def monster_fight(monster1, monster2):
    round = 0  #counts how many rounds have gone by
    monster2attackLis = []
    monster1attackLis = []

    for values in monster2.attacks.values():
        monster2attackLis.append(values)
    for values in monster1.attacks.values():
        monster1attackLis.append(values)

    monster2attackLis = sorted(monster2attackLis, reverse=True)
    monster2attackLis = sorted(monster1attackLis, reverse=True)
        #-----------------------------------------#

    winnerList = []  #list of the winners moves
    winner  = None  #winner in the end

    m1Counter = 0
    m2Counter = 0

    monster1.current_hp -= monster2attackLis[0]
    print(monster1.current_hp)
    

    #return round, winnerList, winner
