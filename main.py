game.splash("Let's figure out the price of your pizza")
LABOUR = 0.75
RENT = 1
MATERIALS = 0.5
Diameter = game.ask_for_number("How big do you want the diameter")
Subtotal = LABOUR + RENT + MATERIALS * Diameter
game.splash("The cost of the pizza with the diamater of " + ("" + str(Diameter)) + "is " + ("" + str(Subtotal)))