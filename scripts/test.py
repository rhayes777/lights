from lights import ada, strip as s

try:
    import rpi_ws281x as r
except ImportError:
    raise

if __name__ == "__main__":
    strip = s.Strip(
        ada=ada.make()
    )

    strip.clear()

    strip[0][0].color = r.Color(255, 255, 255)
    strip[1][0].color = r.Color(255, 0, 0)
    strip[0][1].color = r.Color(0, 255, 0)
    strip[1][1].color = r.Color(0, 0, 255)

    strip.update()
