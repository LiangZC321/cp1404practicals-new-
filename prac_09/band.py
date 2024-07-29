class Band:

    def __init__(self, name):
        self.name = name
        self.bands = []

    def __str__(self):
        band_list = ', '.join(str(i) for i in self.bands)
        return f"{self.name} in ({band_list})"

    def add(self, band):
        self.bands.append(band)

    def play(self):
        for band in self.bands:
            if not vars(band)['instruments']:
                print(f"{vars(band)['name']} needs an instrument!")
            else:
                print(f"{vars(band)['name']} is playing: {vars(band)['instruments'][0]}")
        return None