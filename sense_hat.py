from Sense_Hat import Sense_Hat

sense = Sense_Hat()

X = [255, 255, 255] # RGB Color selection
O = [0, 0, 0]

questionmark = [
O, O, O, O, O, O, O, O,
O, X, X, O, O, O, O, O,
]

sense.set_pixels(questionmark)

sense.show_message("thats great")

sense.get_humidity()
sense.get_orientation_radiants()

# sense clear can be used for either clearing the pixels or clearing and setting the new pixels
sense.clear()
# or
sense.clear(X)