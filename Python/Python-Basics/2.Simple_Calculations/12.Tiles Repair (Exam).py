# 24th April 2016 - SoftUni exam question.
"""
Tiles should be placed on the site in front of a block of flats. The site has a square form with N-meter sides.
The tiles are W meters wide and L meters long. There is a bench on the site with a width of M meters and a length of I
meters. There is no need to put tiles under the bench. Each tile is being placed for 0.2 minutes.
Write a program that reads the size of the site, tiles and bench from the console and calculate how many tiles are
needed to cover the site and also the time needed to place all the tiles.
Example:
Size with a size of 20 meters has an area of 400sq.m. Bench which is 1m wide and 2m long, occupies an area of 2sq.m.
One tile is 5m wide and 4m long => has an area of 20sq.m. Therefore, the area that has to be covered is 400-2=398sq.m
398/2 = 19.90 tiles are needed and 19.90*0.2 = 3.98 minutes are needed to cover the site.

Input(reading 5 numbers, one per line):
• N - the length of the site's side
• W - the width of one tile
• L - the length of one tile
• M - the width of the bench
• I - the length of the bench
Output:
• Print two numbers to the console: the number of tiles needed for covering the site and the time for placement,
each on a new line.
"""
if __name__ == '__main__':
    n = int(input("Enter side of the square: "))
    w = float(input("Enter width of the tile: "))
    l = float(input("Enter height of the tile: "))

    m = int(input("Enter the width of the bench: "))
    i = int(input("Enter the height of the bench: "))

    area_of_the_playground = n * n
    area_of_a_tile = w * l
    area_of_a_bank = m * i

    total_area = area_of_the_playground - area_of_a_bank

    number_of_tiles_needed = total_area / area_of_a_tile
    time_needed = number_of_tiles_needed * 0.2

    print("The number of tiles needed to cover the playground are: " + str(number_of_tiles_needed))
    print("The needed time is: " + str(time_needed))
