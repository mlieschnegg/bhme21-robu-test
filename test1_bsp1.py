import os
# from rpi_ws281x import ws, Adafruit_NeoPixel, Color

name_dict = {
    "ambtin20": {"katnr": 1, "vorname": "Timo"},
    "baylun20": {"katnr": 2, "vorname": "Lukas"},
    "forman21": {"katnr": 3, "vorname": "Marco"},
    "dorjon21": {"katnr": 4, "vorname": "Jonas"},
    "engsan21": {"katnr": 5, "vorname": "Samuel"},
    "fasmin21": {"katnr": 6, "vorname": "Michael"},
    "ferdon21": {"katnr": 7, "vorname": "Dominik"},
    "finman21": {"katnr": 8, "vorname": "Maximilian"},
    "frisan21": {"katnr": 9, "vorname": "Sarah"},
    "hadman21": {"katnr": 10,"vorname": "Matthias"},
    "hauran21": {"katnr": 11,"vorname": "Rafael"},
    "husfln21": {"katnr": 12,"vorname": "Florentina"},
    "hutaln21": {"katnr": 13,"vorname": "Alexander"},
    "kiealn20": {"katnr": 14,"vorname": "Alexander"},
    "kocman21": {"katnr": 15,"vorname": "Maximilian"},
    "krealn21": {"katnr": 16,"vorname": "Alexander"},
    "magman21": {"katnr": 17,"vorname": "Matthias"},
    "orophn21": {"katnr": 18,"vorname": "Philip"},
    "seuchn20": {"katnr": 19,"vorname": "Christoph"},
    "soelun21": {"katnr": 20,"vorname": "Lukas"},
    "swenin21": {"katnr": 21,"vorname": "Nico"},
    "taxpan20": {"katnr": 22,"vorname": "Patrick"},
    "weijun21": {"katnr": 23,"vorname": "Julian"}
}

# LED_COUNT = 3  
# LED_PIN = 21
# LED_FREUQ_HZ = 800000
# LED_DMA = 10
# LED_BRIGHTNESS = 255
# LED_INVERT = False
# LED_CHANNEL = 0
# LED_STRIP = ws.WS2811_STRIP_GRB

# led_disp = Adafruit_NeoPixel(LED_COUNT, 
#                           LED_PIN, 
#                           LED_FREUQ_HZ, 
#                           LED_DMA, 
#                           LED_INVERT, 
#                           LED_BRIGHTNESS,
#                           LED_CHANNEL,
#                           LED_STRIP)

name_key = os.getenv("NAME")
# print(name_key)
if name_key in name_dict:
    decimal_value = name_dict[name_key]["katnr"]
    firstname = name_dict[name_key]["vorname"]

    binary_value = f"{decimal_value:05b}"
    bits = list(binary_value)
    
    # led_disp.begin()
    # led_disp.setPixelColor(1, Color(255, 0, 0))
    # led_disp.show()

    print(f"Hallo {firstname},")
    print("das hast du gut gemacht!")
    print(f"Wie lautet die Dezimalzahl von {binary_value}?")
else:
    print("Der Name ist nicht im Dictionary vorhanden.")
