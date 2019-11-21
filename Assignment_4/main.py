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
        if attack_name in self.known_attacks.keys() and attack_name not in self.attacks.keys():
            self.attacks[attack_name] = self.known_attacks.get(attack_name)
            min_value = min(self.attacks.keys(), key=(lambda k: self.attacks[k]))
            if len(self.attacks) > 4 and attack_name != min_value:
                #FIXME
                #change output error where attack_name is taken out
                for keys, values in self.attacks.items():
                    if self.attacks[min_value] == values and min(min_value, keys) == keys:
                        min_value = keys
                del self.attacks[min_value]
            elif len(self.attacks) > 4 and attack_name == min_value:
                #FIXME
                del self.attacks[min_value]
                next_min_value = min(self.attacks.keys(), key=(lambda k: self.attacks[k]))
                for keys, values in self.attacks.items():
                    if self.attacks[next_min_value] == values and min(min_value, keys) == keys:
                        next_min_value = keys
                del self.attacks[next_min_value]
                self.attacks[min_value] = self.known_attacks.get(min_value)
            return True
        else:
            return False

    def remove_attack(self, attack_name):
        #if attack_name in known_attacks, then return True and remove attack_name
        if attack_name in self.attacks.keys():
            del self.attacks[attack_name]
            if len(self.attacks) == 0:
                self.attacks['wait'] = 0
            return True
        else:
            return False
