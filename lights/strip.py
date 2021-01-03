import time


class Strip:
    def __init__(self, ada):
        self.ada = ada

    def color_wipe(self, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(self.ada.numPixels()):
            self.ada.setPixelColor(i, color)
            self.ada.show()
            time.sleep(wait_ms / 1000.0)
