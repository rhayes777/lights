from lights import ada, strip as s

try:
    import rpi_ws281x as r
except ImportError:
    raise

if __name__ == "__main__":
    strip = s.Strip(
        ada=ada.make()
    )

    strip.color_wipe(
        r.Color(255, 0, 0)
    )
