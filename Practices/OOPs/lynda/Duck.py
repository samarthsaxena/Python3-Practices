#!/usr/bin/env python3

class Duck:
    sound = 'Quack!!!'
    movement = 'Walk like a duck..'

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)

#Driver functione
def main():
    duck = Duck()
    duck.quack()
    duck.move()

if __name__ == '__main__':
    main()
