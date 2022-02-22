class Home:
    def __init__(self):
        self.link = ""
        self.price = 0
        self.address = ""
        self.description = ""
        self.bedroom_count = 0
        self.land_surface = 0

    def __str__(self):
        return "{description} - {link}".format(
            description=self.description,
            link=self.link
        )
