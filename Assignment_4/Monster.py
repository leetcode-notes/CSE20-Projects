import operator

class Monster():
    def __init__(self, name, hp=20):
        self.exp = 0
        self.attacks = {'wait': 0}
        self.name = name
        self.known_attacks = {'sneak_attack': 1, 'slash': 2, 'ice_storm': 3, 'fire_storm': 3,
            'whirlwind': 3, 'earthquake': 2, 'double_hit': 4, 'wait': 0}
        self.current_hp = hp
        self.max_hp = hp
        self.type = 'normal'

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
        self.exp+=1
        self.current_hp = self.max_hp

class Dragon(Monster):

    def __init__(self, name, hp=20):
        super().__init__(name, hp)
        self.type = 'dragon'
        self.counter = 10

    def win_fight(self):
        self.exp+=5
        self.current_hp = self.max_hp
        if self.exp >= self.counter:
            self.counter += 10
            for key in self.attacks:
                self.attacks[key] = self.attacks.get(key) + 1

    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp

class Ghost(Monster):

    def __init__(self, name, hp=20):
        super().__init__(name, hp)
        self.type = 'ghost'
        self.counter = 10

    def win_fight(self):
        self.exp+=5
        self.current_hp = self.max_hp
        if self.exp >= self.counter:
            self.counter += 10
            self.max_hp += 5


    def lose_fight(self):
        self.exp += 1
        self.current_hp = self.max_hp

def monster_fight(monster1, monster2):

    M1round = 0
    M2round = 0
    monster2attackLis = []
    monster1attackLis = []
    winner = None
    round = 0

    for values in monster2.attacks.values():
        monster2attackLis.append(values)
    for values in monster1.attacks.values():
        monster1attackLis.append(values)

    monster2attackLis = sorted(monster2attackLis, reverse=True)
    monster1attackLis = sorted(monster1attackLis, reverse=True)
        #-----------------------------------------#

    M1attacknames = sorted(monster1.attacks.items(), key=operator.itemgetter(1), reverse=True)
    M2attacknames = sorted(monster2.attacks.items(), key=operator.itemgetter(1), reverse=True)

    winnerList = []  #list of the winners moves

    index1 = 0
    index2 = 0

    if all(key == 'wait' for key in monster1.attacks.keys()) and all(key == 'wait' for key in monster1.attacks.keys()):
        return (-1, None, None)

    while(monster2.current_hp > 0):

        try:
            monster2.current_hp -= monster1attackLis[index1]
            index1 += 1
            M1round += 1

        except IndexError:

            index1 = 0

    while(monster1.current_hp > 0):

        try:
            monster1.current_hp -= monster2attackLis[index2]
            index2 += 1
            M2round += 1

        except IndexError:

            index2 = 0

    if(M1round == M2round):
        winner = monster1
        round = M1round
        monster1.win_fight()
        monster2.lose_fight()
        index = 0
        i = 0
        while i < round:
            try:
                winnerList.append(M1attacknames[index][0])
                index += 1
                i+=1
            except:
                index = 0
                continue

    if(M1round < M2round):
        winner = monster1
        monster1.win_fight()
        monster2.lose_fight()
        round = M1round
        index = 0
        i = 0
        while i < round:
            try:
                winnerList.append(M1attacknames[index][0])
                index += 1
                i+=1
            except:
                index = 0
                continue

    if(M2round < M1round):
        winner = monster2
        monster2.win_fight()
        monster1.lose_fight()
        round = M2round
        index = 0
        i = 0
        while i < round:
            try:
                winnerList.append(M2attacknames[index][0])
                index += 1
                i += 1
            except:
                index = 0
                continue


    return (round, winner, winnerList)
