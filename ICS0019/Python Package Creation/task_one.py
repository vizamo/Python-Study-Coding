from triangle_area_package import triangle_area


piece_heigh = int(input("How long is the height of your pizza? "))
piece_base = int(input("How long is the base of your pizza? "))
people_count = int(input("How many people with you eat that pizza? "))

def how_big_is_pizza(piece_heigh, piece_base, people_count):
    piece_area = triangle_area.triangle_area(piece_heigh, piece_base)
    pizza = piece_area * people_count
    return "Yours pizza area is " + str(int(pizza))


print(how_big_is_pizza(piece_heigh, piece_base, people_count))
