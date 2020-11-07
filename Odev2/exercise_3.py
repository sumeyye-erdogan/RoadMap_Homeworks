# Menu Program

class Lunch:
    def __init__(self, menu):
        self.menu = menu

    def menu_price(self):
        switcher = {
            "menu 1": "Your choice: {}, Price:12.00".format(self.menu),

            "menu 2": "Your choice: {}, Price:13.40".format(self.menu)

        }
        return switcher.get(self.menu,"Error in menu")


Paul = Lunch("menu 1")
print(Paul.menu_price())