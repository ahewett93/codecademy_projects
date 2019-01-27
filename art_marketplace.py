class Art:
  '''
  Models works of art for merchants.
  '''
  def __init__(self, artist, title, medium, year, owner):
    # Owner is instance of 'Client'
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner

  def __repr__(self):
    # return artist name, artwork name, year and medium; citation style.
    return "{artist}. \"{title}\". {year}, {medium}. {owner}, {owner_location}.".format(
      artist=self.artist, title=self.title, year=self.year,
      medium=self.medium, owner=self.owner.name, owner_location=self.owner.location)

class Marketplace:

  def __init__(self):
    self.listings = []

  def add_listing(self, new_listing):
    self.listings.append(new_listing)

  def remove_listing(self, old_listing):
    self.listings.remove(old_listing)

  def show_listings(self):
    for listing in self.listings:
      print(listing)

veneer = Marketplace()

class Client:

  def __init__(self, name, location, is_museum=False):
    self.name = name
    self.location = location
    self.is_museum = is_museum

  def sell_artwork(self, artwork, price):
    # Creates new listing for artwork with desired price.
    try:
      artwork.owner.name == self.name
    except OwnerError:
      print("Does not have owner permission to post listing.")
    listing = Listing(artwork, price, artwork.owner)
    veneer.add_listing(listing)

  def buy_artwork(self, artwork):
    # Allows user to purchase artwork
    try:
      artwork.owner.name != self.name
    except OwnerError:
      print("You own this listing.")
    for listing in veneer.listings:
      if listing.art.title == artwork.title:
        art_listing = listing
    art_listing.art.owner = self
    veneer.remove_listing(art_listing)


class Listing:

  def __init__(self, art, price, seller):
    # 'seller' should be instance of 'Client'
    self.art = art
    self.price = price
    self.seller = seller

  def __repr__(self):
    return "Artwork: {name}, Price: {price}".format(name=self.art.title, price=self.price)

def main():
  edytta = Client("Edytta Halprit", 'Private Collection')
  girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", "1910", edytta)

  moma = Client("The MOMA", "New York", True)
  print(girl_with_mandolin.owner.name)
  print(edytta.name)
  edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")
  veneer.show_listings()
  moma.buy_artwork(girl_with_mandolin)
  veneer.show_listings()
  print(girl_with_mandolin)
main()
