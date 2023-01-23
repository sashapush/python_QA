class Coffee_machine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "start"
        print("Write action (buy, fill, take, remaining, exit):")

    def action(self, state):
        if self.state == "start":
            if state == "buy":
                self.state = state
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
                return True
            elif state == "fill":
                self.state = "fill"
                self.n_fill = 0
                print("Write how many ml of water do you want to add:")
                return True
            elif state == "take":
                print("I gave you $%d" % self.money)
                self.money = 0
                print("Write action (buy, fill, take, remaining, exit):")
                return True
            elif state == "remaining":
                self.info()
                return True
            elif state == "exit":
                return False
            else:
                print("Unknown command")
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        elif self.state == "buy":
            if state == "1":
                self.espresso()
            if state == "2":
                self.latte()
            if state == "3":
                self.cappu()
            if state == "back":
                pass
            self.state = "start"
            print("Write action (buy, fill, take, remaining, exit):")
            return True
        elif self.state == "fill":
            if self.n_fill == 0:
                self.water += int(state)
                print("Write how many ml of milk do you want to add:")
                self.n_fill += 1
            elif self.n_fill == 1:
                self.milk += int(state)
                print("Write how many grams of coffee beans do you want to add:")
                self.n_fill += 1
            elif self.n_fill == 2:
                self.beans += int(state)
                print("Write how many disposable cups of coffee do you want to add:")
                self.n_fill += 1
            elif self.n_fill == 3:
                self.cups += int(state)
                self.n_fill = None
                self.state = "start"
                print("Write action (buy, fill, take, remaining, exit):")
            return True

    def info(self):
        print("""
        The coffee machine has:
        %d of water
        %d of milk
        %d of coffee beans
        %d of disposable cups
        %d of money
        """ % (self.water, self.milk, self.beans, self.cups, self.money))
        print("Write action (buy, fill, take, remaining, exit):")

    def espresso(self):
        if self.water < 250:
            print("Sorry, not enough water")
        if self.beans < 16:
            print("Sorry, not enough beans")
        if self.cups < 1:
            print("Sorry, not enough cups")
        if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4
            print("I have enough resources, making you a coffee!")

    def latte(self):
        if self.water < 350:
            print("Sorry, not enough water")
        if self.milk < 75:
            print("Sorry, not enough milk")
        if self.beans < 20:
            print("Sorry, not enough beans")
        if self.cups < 1:
            print("Sorry, not enough cups")
        if self.milk < 75:
            print("Sorry, not enough milk")
        if self.water >= 350 and self.beans >= 20 and self.milk >= 75 and self.cups >= 1:
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7
            print("I have enough resources, making you a coffee!")

    def cappu(self):
        if self.water < 200:
            print("Sorry, not enough water")
        if self.beans < 20:
            print("Sorry, not enough beans")
        if self.cups < 1:
            print("Sorry, not enough cups")
        if self.milk < 100:
            print("Sorry, not enough milk")
        if self.water >= 200 and self.beans >= 12 and self.milk >= 100 and self.cups >= 1:
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6
        print("I have enough resources, making you a coffee!")


my_machine = Coffee_machine()
catch = True
while catch == True:
    p_state = input()
    catch = my_machine.action(p_state)