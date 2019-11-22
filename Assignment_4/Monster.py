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
		self.exp += 5
        self.current_hp = self.max_hp

	def lose_fight(self):
		self.exp += 1
        self.current_hp = self.max_hp

def monster_fight(monster1, monster2):
	while(monster1.current_hp > 0 and monster2.current_hp > 0):
        rounds = 0
        
