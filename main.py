import math

"""
Calculator for finding needed dimensions to make a 2 piece kiln hood face (symmetrical only)
position =  distance from skirt to seem on face
lap = amount of lap on seem per piece
height of face = distance from the skirt to the top
"""

print("Give the following dimensions to find the width\n"
      "of the top and bottom pieces at the seem. When making\n"
      "a face of a hood out of 2 pieces\n\n")

height_of_face = float(input("Enter Height of Front Face(-skirt): "))
width_of_face = float(input("Enter Width: "))
top = float(input("Enter Size of Top: "))
position = float(input("Enter Seem Distance from Skirt: "))
lap = float(input("Enter Lap Size: "))


def front_split():
    bottom_height = position + lap
    top_height = (height_of_face - position) + lap
    starting_base = (width_of_face - top)/2

    tan_radians = math.atan(height_of_face / starting_base)
    tan_of_tan = math.tan(tan_radians)

    bottom_piece_adjacent = bottom_height / tan_of_tan
    top_piece_adjacent = top_height / tan_of_tan
    seem_adjacent = position / tan_of_tan
    top_of_bottom_piece = width_of_face - (bottom_piece_adjacent * 2)
    bottom_of_top_piece = top + (top_piece_adjacent * 2)
    seem_length = width_of_face - (seem_adjacent * 2)
    print("top of bottom piece = " + str(round(top_of_bottom_piece, 3)))
    print("bottom of top piece = " + str(round(bottom_of_top_piece, 3)))
    print("Seem Length = " + str(round(seem_length, 3)))

front_split()

"""
Notes:
tan opposite / adjacent
Tangent: tan(θ) = Opposite / Adjacent
tan(tana) = bottomheight / ?base?
?base? = bottomheight / tan(tana)
"""
