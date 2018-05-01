from objects.area import Area
from constructionlist import construction_list
import random

class RandomAlgorithm(object):

    def fillRandomGrid(self, area, fhAmount, bAmount, mAmount):

        houses = construction_list(area, fhAmount, bAmount, mAmount)

        # place a house from the list on random coordinates
        counter = 0
        while len(houses) > 0:
            print('Run {} | Houses left: {}'.format(counter, len(houses)))
            currentHouse = random.choice(houses)
            try:
                xCor = random.randint(0, area.width - currentHouse.width)
                yCor = random.randint(0, area.height - currentHouse.height)
                print('Trying to place "{}" on ({}, {})'.format(currentHouse, xCor, yCor))
                area.place_house(currentHouse, xCor, yCor)
                houses.remove(currentHouse)
            except RuntimeError:
                print("Cannot validly place house at these coordinates.")
            counter += 1
        print('All houses placed')
        print('Grid value: {}'.format(area.get_area_price()))
