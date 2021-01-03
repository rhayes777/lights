import time

try:
    import rpi_ws281x as r
except ImportError:
    raise


class Pixel:
    def __init__(self, strip, number):
        self.strip = strip
        self.number = number

        self._color = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        print(self.number)
        self._color = color
        self.strip.ada.setPixelColor(self.number, color)


class Column:
    def __init__(self, strip, number):
        self.strip = strip
        self.number = number

    def __getitem__(self, item):
        return Pixel(
            self.strip,
            self.strip.width * item + self.number
        )

    def __iter__(self):
        return iter(self.pixels)

    @property
    def pixels(self):
        return [
            self[number]
            for number
            in range(self.strip.height)
        ]


class Strip:
    def __init__(self, ada, width=8, height=8):
        self.ada = ada
        self.width = width
        self.height = height

    def __getitem__(self, number):
        return Column(
            self,
            number
        )

    @property
    def columns(self):
        return [
            self[number]
            for number
            in range(self.width)
        ]

    def __iter__(self):
        return iter(self.columns)

    def update(self):
        self.ada.show()

    def color_wipe(self, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(self.ada.numPixels()):
            self.ada.setPixelColor(i, color)
            self.ada.show()
            time.sleep(wait_ms / 1000.0)

    def clear(self):
        for column in self:
            for pixel in column:
                pixel.color = r.Color(0, 0, 0)

        self.update()
