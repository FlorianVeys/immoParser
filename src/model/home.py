class Home:
    def __init__(self):
        self.link = ""
        self.price = 0
        self.address = ""
        self.description = ""
        self.bedroom_count = 0
        self.land_surface = 0

    def __str__(self):
        return "description: {description}\nlink: {link}\nprice: {price}\naddress: {address}\nbedroom: {bedroom}\nlandSurface: {surface}".format(
            description=self.description,
            link=self.link,
            price=self.price,
            address=self.address,
            bedroom=self.bedroom_count,
            surface=self.land_surface
        )

    def __repr__(self):
        return "description: {description}\nlink: {link}\nprice: {price}\naddress: {address}\nbedroom: {bedroom}\nlandSurface: {surface}".format(
            description=self.description,
            link=self.link,
            price=self.price,
            address=self.address,
            bedroom=self.bedroom_count,
            surface=self.land_surface
        )

    def __eq__(self, other):
        return self.link == other.link

    def __hash__(self):
        return hash(self.link)
