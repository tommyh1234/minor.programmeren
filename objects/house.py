from objects.water import Water


class House(object):
    """Blueprint for object in which a house instance will be saved"""

    x = None
    y = None
    height = None
    width = None
    minimumSpace = None
    priceIncrease = None
    space = None
    value = None
    area = None

    def __init__(self, area):
        """Extra characteristics for a house instance created
        on initialization"""

        self.area = area
        self.space = 0

    def surface(self):
        """Calculate the total surface of a house"""

        return self.width * self.height

    def check_validity(self):
        """Checks the validity of the placement of a house
        by checking if the required minimum space is present
        and if there is nothing else at the coordinates of this house"""

        endX = self.x + self.width + self.minimumSpace
        endY = self.y + self.height + self.minimumSpace

        # check if coordinates covered by house are not
        # covered by something else
        for i in range(self.x - self.minimumSpace, endX):
            for j in range(self.y - self.minimumSpace, endY):
                # if space in grid is not empty or current house itself
                if (self.area.grid[i][j] is not None and
                        self.area.grid[i][j] is not self):
                    # if a space is water...
                    if isinstance(self.area.grid[i][j], Water):
                        # ... and space is inside house
                        if (i >= self.x and i <= self.x + self.width and
                                j >= self.y and j <= self.y + self.height):
                            return False
                    # or if space is filled by another house
                    elif isinstance(self.area.grid[i][j], House):
                        return False
        return True

    def get_space(self):
        """Get the possible free space for a house"""

        space = 0
        x = self.x
        y = self.y

        # while a given grid position is not taken by something else...
        while (self.area.grid[x][y] is None or
               self.area.grid[x][y] is self or
               isinstance(self.area.grid[x][y], Water)):

            # if x-coordinate + house width + free space is smaller than
            # current x-coordinate and falls within area
            if (x < self.x + self.width - 1 + space and
                    x >= 0 and x < self.area.width - 1):
                # check next x-coordinate
                x += 1

            # if y-coordinate + house height + free space is smaller than
            # current y-coordinate and falls within area
            elif (y < self.y + self.height - 1 + space and
                  y >= 0 and y < self.area.height - 1):
                # check next y-coordiante and reset x-coordinate
                y += 1
                x = self.x - space

                # make sure x and y-coordinates will not be outside of area
                if x < 0:
                    x = 0
                if x > self.area.width - 1:
                    x = self.area.width - 1
                if y > self.area.height - 1:
                    y = self.area.height - 1

            # if free space + house's width or height falls within map...
            elif (self.width + space < self.area.width or
                  self.height + space < self.area.height):

                # reset x and y-coordinates and check a
                # larger area around house
                space += 1
                x = self.x - space
                y = self.y - space

                # make sure x and y-coordinates will not be outside of area
                if x < 0:
                    x = 0
                if x > self.area.width - 1:
                    x = self.area.width - 1
                if y < 0:
                    y = 0
                if y > self.area.height - 1:
                    y = self.area.height - 1
            else:
                break

        return space - 1

    def get_price(self):
        """Get the value for a house"""

        # (Re)calculate the houses' space
        self.space = self.get_space()

        # calculate value of one m2 extra free space for current house
        addedValue = self.value * self.priceIncrease

        # calculate house's extra free space
        # (divide by 2 because of grid of 0.5m's)
        extraMeters = (self.space - self.minimumSpace) / 2

        # calcluate total value of house
        totalValue = self.value + (extraMeters * addedValue)

        return totalValue
