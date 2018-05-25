class Water(object):
    """Blueprint for water object"""

    x = None
    y = None
    height = None
    width = None
    value = None
    area = None

    def __init__(self, area):
        """Extra characteristics for a water instance created on initialization"""
        self.area = area

    def surface(self):
        """Calculate the total surface of a water instance"""
        return self.width * self.height

    def check_validity(self):
        """Checks the validity of the placement of a water
        instance by checking if there is nothing else at the
        coordinates of this water instance"""

        endX = self.x + self.width
        endY = self.y + self.height

        # check if coordinates covered by water are not
        # covered by something else
        for i in range(self.x, endX):
            for j in range(self.y, endY):
                if (self.area.grid[i][j] is not None
                        and self.area.grid[i][j] is not self):
                    return False

        return True
