class Menu:
  '''Class that represents a restaraunt menu.'''
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    # return menu and time available.
    return "{name} menu available from {start} to {end}".format(name=self.name, start=self.start_time, end=self.end_time)

  def calculate_bill(self, purchased_items):
    # calculate bill using menu prices.
    bill = 0
    for purchased_item in purchased_items:
      price = self.items[purchased_item]
      bill += price
    return bill
# Menus.
brunch = Menu('brunch', {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, '11am', '4pm')

early_bird = Menu('early_bird', {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, '3pm', '6pm')

dinner = Menu('dinner', {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, '5pm', '11pm')

kids = Menu('kids', {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, '11am', '9pm')

menu_list = [brunch, early_bird, dinner, kids]

class Franchise:
  '''A class to store menu, location, and service time for a franchise restaraunt.'''
  def __init__(self, address, menus):
    # Menu must be a list of 'Menu' objects.
    self.address = address
    self.menus = menus

  def __repr__(self):
    # Print the location of the franchise.
    return self.address

  def available_menus(self, time):
    # returns the available menus given the time of day.
    if time < 3 or time >= 11:
      return [self.menus[0], self.menus[3]]
    if time >= 3 and time < 5:
      return [self.menus[1], self.menus[3]]
    if time >= 5 and time < 6:
      return self.menus[1:]
    if time >= 6 and time < 11:
      return self.menus[2:]

class Business:

  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises



def main():
  flagship_store = Franchise("1232 West End Road", menu_list)
  new_installment = Franchise("12 East Mulberry Street", menu_list)
  business_name = "Basta Fazoolin' with my Heart"
  franchises = [flagship_store, new_installment]
  basta = Business(business_name, franchises)
  arepas_menu = Menu("Take a' Arepa", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, "10am", "8pm")
  arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)
  arepa = Business("Take a' Arepa", arepas_place)
   
main()
