# **Find Cost of Tile to Cover W x H Floor** 
# Calculate the total cost of tile it would take
# to cover a floor plan of width and height, 
# using a cost entered by the user.

width = int(raw_input("Floor width: "))
height = int(raw_input("Floor height: "))
cost = int(raw_input("Tile cost per sq ft: "))

cost = width * height * cost

print cost