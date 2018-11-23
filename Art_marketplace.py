class Art:
	def __init__(self, artist, title, medium, year, owner):
		self.artist = artist
		self.title = title
		self.medium = medium
		self.year = year
		self.owner = owner
	
	def __repr__(self):
		return "%s. \"%s\". %s, %s, %s, %s." %(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)

class  Marketplace:
	def __init__(self):
		self.listings = []

	def add_listing(self, new_listing):
		self.listings.append(new_listing)

	def remove_listing(self, expired_listing):
		self.listings.remove(expired_listing)

	def show_listings(self):
		for listing in self.listings:
			print(listing)

class Client:
	def __init__(self, name, location="Private Collection", is_museum=False, wallet=0, wishlist=None):
		self.name = name
		self.location = location
		self.is_museum = is_museum
		self.wallet = wallet
		self.wishlist = wishlist

	def sell_artwork(self, artwork, price):
		if artwork.owner == self:
			new_listing = Listing(artwork, price, self)
			veneer.add_listing(new_listing)
			self.wallet += price
		return "Transaction successful. Your wallet is: $%sM(USD)." %(self.wallet)

	def buy_artwork(self, artwork):
		if artwork.owner == self:
			pritn("You are the current owner of this artwork! You can't buy it from yourself!")
		else:
			art_listing = None
			for listing in veneer.listings:
				if listing.art == artwork:
					art_listing = listing
					break
			if art_listing != None:
				artwork.owner == self
				self.wallet -= art_listing.price
				veneer.remove_listing(art_listing)
			return "Transaction successful. Your wallet is: $%sM(USD)." %(self.wallet)
	def show_withlist(self):
		print(self.wishlist)

class Listing:
	def __init__(self, art, price, seller):
		self.art = art
		self.price = price
		self.seller = seller

	def __repr__(self):
		return "%s, $%s M(USD)." %(self.art.title, self.price)


veneer = Marketplace()
edytta = Client("Edytta Halpirt", None, False, "Mona Lisa")
moma = Client("The MOMA", "New York", True, 50, "Girl with a Mandolin (Fanny Tellier)")
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)
mona_lisa = Art("Da'Vinci Leonardo", "Mona Lisa", "oil on canvas", 1503, moma)
edytta.sell_artwork(girl_with_mandolin, 6)
moma.buy_artwork(girl_with_mandolin)
veneer.show_listings()
print(edytta.show_withlist())

	