from random import randint

class Items:
    def __init__(self, name=None, currency_value=None, weight=None):
        self.item_name = name
        self.gold_value = currency_value
        self.item_weight = weight

    def __str__(self):
        return '{}'.format(self.item_name)


class Weapons(Items):
    def __init__(self):
        super().__init__(name=None, currency_value=None, weight=None)
        available_weapons = {
            1: {'name': 'Laser', 'currency_value': 80, 'weight': 90, 'hit_points': 100, 'attack_power': 4,
                'attack_speed': 6},
            2: {'name': 'Cannon', 'currency_value': 90, 'weight': 100, 'hit_points': 110, 'attack_power': 6,
                'attack_speed': 5},
            3: {'name': 'Plasma Ray', 'currency_value': 100, 'weight': 110, 'hit_points': 120,
                'attack_power': 8,'attack_speed': 4},
            4: {'name': 'Rail Gun', 'currency_value': 110, 'weight': 120, 'hit_points': 130, 'attack_power': 10,
                'attack_speed': 3},
            5: {'name': 'Photon Torpedo', 'currency_value': 120, 'weight': 130, 'hit_points': 140,
                'attack_power': 12, 'attack_speed': 2},
        }
        key = randint(1, 5)
        self.item_name = available_weapons[key]['name']
        self.gold_value = available_weapons[key]['currency_value']
        self.item_weight = available_weapons[key]['weight']
        self.hit_points = available_weapons[key]['hit_points']
        self.attack_power = available_weapons[key]['attack_power']
        self.attack_speed = available_weapons[key]['attack_speed']

    def attack(self, enemy_hp):
        enemy_hp -= self.attack_power
        return enemy_hp

    # def __str__(self):
    #     return self.item_name + ", " + self.attack_power +  ", " + self.attack_speed


class Shields(Items):
    def __init__(self):
        super().__init__(name=None, currency_value=None, weight=None)
        available_shields = {
            1: {'name': 'Tin', 'currency_value': 100, 'weight': 100, 'hit_points': 75, 'defensive_power': 100},
            2: {'name': 'Steel', 'currency_value': 120, 'weight': 200, 'hit_points': 100,
                'defensive_power': 125},
            3: {'name': 'Silver', 'currency_value': 140, 'weight': 400, 'hit_points': 125,
                'defensive_power': 150},
            4: {'name': 'Titanium', 'currency_value': 160, 'weight': 600, 'hit_points': 150,
                'defensive_power': 175},
            }
        key = randint(1, 4)
        self.item_name = available_shields[key]['name']
        self.gold_value = available_shields[key]['currency_value']
        self.item_weight = available_shields[key]['weight']
        self.hit_points = available_shields[key]['hit_points']
        self.defensive_power = available_shields[key]['defensive_power']

    # def __str__(self):
    #     return self.item_name + ", " + self.defensive_power


class Drive(Items):
    def __init__(self):
        super().__init__(name=None, currency_value=None, weight=None)
        available_engines = {
            1: {'name': 'Sub-light Drive', 'currency_value': 100, 'weight': 150, 'hit_points': 200,
                'speed_boost': 2},
            2: {'name': 'Alcubierre Drive', 'currency_value': 200, 'weight': 200, 'hit_points': 300,
                'speed_boost': 4},
            3: {'name': 'Warp Drive', 'currency_value': 300, 'weight': 250, 'hit_points': 400,
                'speed_boost': 6},
            4: {'name': 'Improbability Drive', 'currency_value': 400, 'weight': 300, 'hit_points': 500,
                'speed_boost': 8},
            5: {'name': 'Ludicrous Drive', 'currency_value': 500, 'weight': 350, 'hit_points': 600,
                'speed_boost': 10}
        }
        key = randint(1, 5)
        self.item_name = available_engines[key]['name']
        self.gold_value = available_engines[key]['currency_value']
        self.item_weight = available_engines[key]['weight']
        self.hit_points = available_engines[key]['hit_points']
        self.speed_boost = available_engines[key]['speed_boost']


class Gold(Items):
    def __init__(self):
        super().__init__(name=None, currency_value=None, weight=None)
        self.item_name = 'Gold'
        self.gold_value = 1
        self.item_weight = 0


class Heal(Items):
    def __init__(self):
        super().__init__(name=None, currency_value=None, weight=None)
        self.item_name = 'Universal Heal'
        self.gold_value = 50
        self.item_weight = 50
        self.heal_value = 500

    def heal_it(self, ship_hp):
        ship_hp += self.heal_value
        return ship_hp
        #may need to remove a Universal Heal from inventory as well?


class Key(Items):
    def __init__(self):
        super().__init__(name=None, currency_value=None, weight=None)
        available_keys = {
            1: {'name': 'Small Key', 'currency_value': 50, 'weight': 50},
            2: {'name': 'Big Key', 'currency_value': 50, 'weight': 50},
            3: {'name': 'Master Key', 'currency_value': 50, 'weight': 50},
            4: {'name': 'Skull Key', 'currency_value': 50, 'weight': 50},
        }
        key = randint(1, 4)
        self.item_name = available_keys[key]['name']
        self.gold_value = available_keys[key]['currency_value']
        self.item_weight = available_keys[key]['weight']


class Inventory:
    def __init__(self):
        self.inventory = [] # 23 slots
        self.heals = [] # 1 slot stacking
        self.gold = [] # 1 slot stacking
        self.max_weight = 5000
        self.current_weight = 0
#max weight should be 5k. adds weight of each item in it, and if new item makes inventory exceed 5k, then cannot be added
#when removing from inventory, should subtract weight of item removed

    def add_to_inventory(self, new_item):
        if len(self.inventory) <= 23 and self.current_weight + new_item.item_weight <= self.max_weight:
            self.inventory.append(new_item)
            self.current_weight += new_item.item_weight
            return '{} has been added to inventory'.format(new_item.item_name)
        else:
            return '{} cannot be added due to space or weight.'.format(new_item.item_name)

    def display_inventory(self):
        for i, o in enumerate(self.inventory):
            print('{} - {}'.format(i, o))


    def remove_from_inventory(self, item_index):
        removed_item =  self.inventory.pop(item_index)
        self.current_weight -= removed_item.item_weight
        return 'You have removed {} from your inventory'.format(removed_item.item_name)


    def display_gold_total(self):
        pass

shield = Shields()
inv = Inventory()
print(inv.add_to_inventory(shield))
engine = Drive()
print(inv.add_to_inventory(engine))
inv.display_inventory()
print()
print(inv.remove_from_inventory(0))
inv.display_inventory()