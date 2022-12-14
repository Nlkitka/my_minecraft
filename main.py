class Stive:
    hp = 100
    damage = 5
    speed = 2
    jump = 1

    def eat(self, food):
        if Stive.hp < 150:
            Stive.hp += food.add_hp
            print('Stives hp = ' + str(Stive.hp))
            print('Stive ate ' + str(food.food_category))
        else:
            print('hp is max')

    def booty(self, block):
        if(block.hp>0):
            block.hp = block.hp - self.damage
            print('blocks strength: ' + str(block.hp))
        else:
            print(str(block.category) + 'was broken')


class Block:
    hp = 20
    weight = 1
    useful_resource = 1
    category = 'Earth'

    def __init__(self, category):
        self.category = category


class Food:
    add_hp = 3
    food_category = 'bread'

    def __init__(self, food_category):
        self.food_category = food_category


if __name__ == '__main__':
    my_stive = Stive()
    bread = Food('bread')
    my_stive.eat(bread)
    rabbit = Food('rabbit')
    my_stive.eat(rabbit)
