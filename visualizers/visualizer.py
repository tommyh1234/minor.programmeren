import pygame
import matplotlib
import matplotlib.backends.backend_agg as agg
import pylab


class Visualizer:
    """Draws a visualisation for a given area"""

    def __init__(self, area, algorithm, showDecrease=False):
        """Initiate all elements necessary to create a visualization

        Keyword arguments:
        area      -- the area that should be visualised
        algorithm -- the algorithm by which the given area is filled
        """

        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 1040, 770
        self.area = area
        self.algorithm = algorithm
        self.lastPrice = 0
        self.scores = []
        self.allTimeHigh = 0
        self.showDecrease = showDecrease

    def on_init(self):
        """Starts pygame"""

        # initialize pygame
        pygame.init()
        self._running = True

        # set dimensions of pygame window
        self.screen = pygame.display.set_mode(self.size,
                                              (pygame.HWSURFACE |
                                               pygame.DOUBLEBUF))

        # set background and title of pygame window
        self.img_grass = pygame.image.load("images/grass.jpg")
        pygame.display.set_caption("Amstelhaege")

        # draw visualization
        self.on_render()

    def on_event(self, event):
        """Listens for input"""

        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.USEREVENT:
            self.area = event.area

    def on_render(self):
        """Executes given algorithm and draws visualization"""

        # set text font for in visualization
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 24)

        # continue running algorithm until done
        if self.algorithm.isDone is False:
            self.algorithm.execute()

        # draw background
        for i in range(0, 3):
            for j in range(0, 3):
                self.screen.blit(self.img_grass, (i * 270, j * 270))

        # get water instances to draw and draw them
        allWatersList = []
        allWatersList.extend(self.area.allWatersList)

        for water in allWatersList:
            pygame.draw.rect(
                self.screen, (0, 0, 128),
                (water.x * 2,
                 water.y * 2,
                 water.width * 2,
                 water.height * 2)
                )
        pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            (0, self.height-50, self.width, 50)
            )

        # get house instances to draw and draw them
        housesToPlace = []
        housesToPlace.extend(self.area.mansionList)
        housesToPlace.extend(self.area.familyHomeList)
        housesToPlace.extend(self.area.bungalowList)

        for house in housesToPlace:
            # draw free space
            space = pygame.Surface((house.space * 4 + house.width * 2,
                                    house.space * 4 + house.height * 2))
            space.set_alpha(64)
            space.fill((180, 0, 0))
            self.screen.blit(space,
                             (house.x * 2 - house.space * 2,
                              house.y * 2 - house.space * 2))

            # draw minimum free space
            space = pygame.Surface((house.minimumSpace * 4 + house.width * 2,
                                    house.minimumSpace * 4 + house.height * 2))
            space.set_alpha(110)
            space.fill((100, 0, 0))
            self.screen.blit(space,
                             (house.x * 2 - house.minimumSpace * 2,
                              house.y * 2 - house.minimumSpace * 2))

        for house in housesToPlace:
            # draw house, colored based on type
            kind = type(house).__name__
            if kind == "Mansion":
                pygame.draw.rect(self.screen,
                                 (200, 255, 40),
                                 (house.x * 2,
                                  house.y * 2,
                                  house.width * 2,
                                  house.height * 2))
            elif kind == "Bungalow":
                pygame.draw.rect(self.screen,
                                 (255, 40, 200),
                                 (house.x * 2,
                                  house.y * 2,
                                  house.width * 2,
                                  house.height * 2))
            elif kind == "FamilyHome":
                pygame.draw.rect(self.screen,
                                 (0, 255, 0),
                                 (house.x * 2,
                                  house.y * 2,
                                  house.width * 2,
                                  house.height * 2))

        # Draw black bar at bottom of screen for extra info
        pygame.draw.rect(self.screen,
                         (0, 0, 0),
                         (0, self.height - 50, self.width, 50))

        # Draw area value and last value increase in infobox
        textSurface = font.render('Score: '
                                  + str(self.area.price),
                                  True, (255, 255, 255))
        self.screen.blit(textSurface, (10, self.height-35))

        # create distinct color for value decreases
        increaseColor = (255, 255, 255)
        if (self.area.price - self.lastPrice < 1):
            increaseColor = (80, 80, 80)
        textSurface = font.render('Increase: ' +
                                  str(self.area.price - self.lastPrice),
                                  True, increaseColor)
        self.screen.blit(textSurface, (330, self.height-35))
        pygame.draw.rect(self.screen,
                         (0, 0, 0),
                         (640, 0, 400, self.height))

        # save area values to draw graph
        if (self.area.price >= self.lastPrice and
                self.algorithm.isDone is False and
                self.showDecrease is False):

            self.scores.append(self.area.price)
            self.lastPrice = self.area.price

        if self.showDecrease is True and self.algorithm.isDone is False:
            self.scores.append(self.area.price)
            self.lastPrice = self.area.price

        # draw graph with area values
        fig = pylab.figure(figsize=[4, 4],  # Inches
                           dpi=100)  # 100 dots per inch
        ax = fig.gca()
        ax.plot(self.scores)

        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()

        surf = pygame.image.fromstring(raw_data, (400, 400), "RGB")
        self.screen.blit(surf, (640, 0))
        matplotlib.pyplot.close(fig)

        # Draw all time highest score if that's set
        if self.allTimeHigh is not 0:
            textSurface = font.render('Highest score: ' +
                                      str(self.allTimeHigh),
                                      True, (255, 255, 255))
            self.screen.blit(textSurface, (650, 410))

        pygame.display.flip()
        pass

    def on_cleanup(self):
        """Closes the pygame window"""

        pygame.quit()

    def on_execute(self):
        """Starts and executes the visualisation"""

        # cannot run without visualization
        if self.on_init() is False:
            self._running = False

        # while running listen for events and render these
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()

        # after running, quit pygame
        self.on_cleanup()
