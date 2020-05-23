
class CoffeeMachine():
    water_amount = 400
    milk_amount = 540
    coffee_amount = 120
    cups_amount = 9
    money_amount = 550
    stage = "choosing action"

    def print_machine_status(self, water_amount, milk_amount, coffee_amount, cups_amount, money_amount):
        print('The coffee machine has: \n ' +
              str(water_amount) + ' of water \n ' +
              str(milk_amount) + ' of milk \n ' +
              str(coffee_amount) + ' of coffee beans \n ' +
              str(cups_amount) + ' of disposable cups \n ' +
              '$' + str(money_amount) + ' of money')

    def check_amount(self, water, milk, coffee, cups, type_of_coffee):
        if type_of_coffee == '1':
            water -= 250
            coffee -= 16
            cups -= 1
        elif type_of_coffee == '2':
            water -= 350
            milk -= 75
            coffee -= 20
            cups -= 1
        elif type_of_coffee == '3':
            water -= 200
            milk -= 100
            coffee -= 12
            cups -= 1

        if water < 0:
            return 'Sorry, not enough water!'
        elif milk < 0:
            return 'Sorry, not enough milk!'
        elif coffee < 0:
            return 'Sorry, not enough coffee'
        elif cups < 0:
            return 'Sorry, not enough cups'
        else:
            return 'I have enough resources, making you a coffee!'

    def user_input(self, us_in):

        if us_in == "exit":
            self.stage = "exit"

        if self.stage == "choosing type":
            status = self.check_amount(self.water_amount, self.milk_amount, self.coffee_amount,
                                       self.cups_amount, us_in)
            print(status)
            if status == 'I have enough resources, making you a coffee!':
                if us_in == '1':
                    self.water_amount -= 250
                    self.coffee_amount -= 16
                    self.cups_amount -= 1
                    self.money_amount += 4
                elif us_in == '2':
                    self.water_amount -= 350
                    self.milk_amount -= 75
                    self.coffee_amount -= 20
                    self.cups_amount -= 1
                    self.money_amount += 7
                elif us_in == '3':
                    self.water_amount -= 200
                    self.milk_amount -= 100
                    self.coffee_amount -= 12
                    self.cups_amount -= 1
                    self.money_amount += 6

            self.stage = "choosing action"

        elif self.stage == "Fill water":
            self.water_amount += int(us_in)
            self.stage = "Fill milk"
            self.user_input(input())

        elif self.stage == "Fill milk":
            self.milk_amount += int(us_in)
            self.stage = "Fill coffee"
            self.user_input(input())

        elif self.stage == "Fill coffee":
            self.coffee_amount += int(us_in)
            self.stage = "Fill cups"
            self.user_input(input())

        elif self.stage == "Fill cups":
            self.cups_amount += int(us_in)
            self.stage = "choosing action"
            self.user_input(input())

        else:
            if us_in == 'buy':
                self.stage = 'choosing type'
                self.user_input(input())

            elif us_in == 'fill':
                self.stage = "Fill water"
                self.user_input(input())

            elif us_in == 'take':
                print('I gave you $' + str(self.money_amount))
                self.money_amount = 0

            elif us_in == 'remaining':
                self.print_machine_status(self.water_amount, self.milk_amount,
                                          self.coffee_amount, self.cups_amount, self.money_amount)


my_coffee_machine = CoffeeMachine()
while my_coffee_machine.stage != 'exit':
    my_coffee_machine.user_input(input())

