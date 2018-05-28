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

        # while a given grid position is not taken by something else...
        while (space < self.area.width):

            # first check horizontally
            for x in range(self.x - space, self.x + self.width + space):
                safeX = x
                if safeX >= self.area.width - 1:
                    safeX = self.area.width - 1

                if safeX < 0:
                    safeX = 0

                topY = self.y - space
                if topY < 0:
                    topY = 0

                # first check the top
                if(self.area.grid[safeX][topY] is not None and
                   self.area.grid[safeX][topY] is not self and
                   not isinstance(self.area.grid[safeX][topY], Water)):
                    return space - 1

                bottomY = self.y + self.height + space
                if bottomY >= self.area.height - 1:
                    bottomY = self.area.height - 1
                # then check the bottom
                if(self.area.grid[safeX][bottomY] is not None and
                   self.area.grid[safeX][bottomY] is not self and
                   not isinstance(self.area.grid[safeX][bottomY], Water)):
                    return space - 1

            # then check vertically
            for y in range(self.y - space, self.y + self.height + space):
                safeY = y
                if safeY >= self.area.height - 1:
                    safeY = self.area.height - 1

                if safeY < 0:
                    safeY = 0

                # make sure the left x is not out of bounds
                leftX = self.x - space
                if leftX < 0:
                    leftX = 0

                # check the left side
                if(self.area.grid[leftX][safeY] is not None and
                   self.area.grid[leftX][safeY] is not self and
                   not isinstance(self.area.grid[leftX][safeY], Water)):
                    return space - 1

                # make sure the right x is not out of bounds
                rightX = self.x + self.width + space
                if rightX >= self.area.width - 1:
                    rightX = self.area.width - 1

                # then check the right side
                if(self.area.grid[rightX][safeY] is not None and
                   self.area.grid[rightX][safeY] is not self and
                   not isinstance(self.area.grid[rightX][safeY], Water)):
                    return space - 1

            space += 1

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
