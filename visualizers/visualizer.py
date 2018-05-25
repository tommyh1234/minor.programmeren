import pygame
import matplotlib
import matplotlib.backends.backend_agg as agg
import pylab


class Visualizer:
    def __init__(self, area, algorithm):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 1040, 770
        self.area = area
        self.algorithm = algorithm
        self.lastPrice = 0
        self.scores = []
        self.allTimeHigh = 0

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
                                            self.size,
                                            pygame.HWSURFACE | pygame.DOUBLEBUF
                                            )
        self._running = True
        self.img_grass = pygame.image.load("images/grass.jpg")
        pygame.display.set_caption("Amstelhaege")
        self.on_render()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.USEREVENT:
            self.area = event.area

    def on_render(self):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 24)

        if self.algorithm.isDone is False:
            self.algorithm.execute()

        for i in range(0, 3):
            for j in range(0, 3):
                self.screen.blit(self.img_grass, (i * 270, j * 270))

        allWatersList = []
        allWatersList.extend(self.area.allWatersList)

        for water in allWatersList:
            # place water
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

        housesToPlace = []
        housesToPlace.extend(self.area.mansionList)
        housesToPlace.extend(self.area.familyHomeList)
        housesToPlace.extend(self.area.bungalowList)

        for house in housesToPlace:
            # draw space
            space = pygame.Surface((
                house.space * 4 + house.width * 2,
                house.space * 4 + house.height * 2
                ))
            space.set_alpha(64)
            space.fill((180, 0, 0))
            self.screen.blit(
                space,
                (house.x * 2 - house.space * 2, house.y * 2 - house.space * 2)
                )

            # draw minimum space
            space = pygame.Surface((
                house.minimumSpace * 4 + house.width * 2,
                house.minimumSpace * 4 + house.height * 2
                ))
            space.set_alpha(110)
            space.fill((100, 0, 0))
            self.screen.blit(
                space,
                (house.x * 2 - house.minimumSpace * 2,
                 house.y * 2 - house.minimumSpace * 2))

        for house in housesToPlace:
            # draw house
            kind = type(house).__name__
            if kind == "Mansion":
                pygame.draw.rect(
                    self.screen, (200, 255, 40),
                    (house.x * 2,
                     house.y * 2,
                     house.width * 2,
                     house.height * 2)
                    )
            elif kind == "Bungalow":
                pygame.draw.rect(
                    self.screen, (255, 40, 200),
                    (house.x * 2,
                     house.y * 2,
                     house.width * 2,
                     house.height * 2)
                    )
            elif kind == "FamilyHome":
                pygame.draw.rect(
                    self.screen, (0, 255, 0),
                    (house.x * 2,
                     house.y * 2,
                     house.width * 2,
                     house.height * 2)
                    )
        # Draw a black bar at the bottom of the screen
        pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            (0, self.height - 50, self.width, 50)
            )

        # Draw the score and the last increase
        textSurface = font.render('Score: ' + str(self.area.price),
                                  True, (255, 255, 255))
        self.screen.blit(textSurface, (10, self.height-35))

        increaseColor = (255, 255, 255)
        if (self.area.price - self.lastPrice < 1):
            increaseColor = (80, 80, 80)

        textSurface = font.render('Increase: ' +
                                  str(self.area.price - self.lastPrice),
                                  True, increaseColor)
        self.screen.blit(textSurface, (330, self.height-35))
        pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            (640, 0, 400, self.height)
            )

        if (self.area.price >= self.lastPrice and
                self.algorithm.isDone is False):

            self.scores.append(self.area.price)
            self.lastPrice = self.area.price

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

        # Draw the all time highest score if that's set
        if self.allTimeHigh is not 0:
            textSurface = font.render('Highest score: ' +
                                      str(self.allTimeHigh),
                                      True, (255, 255, 255))
            self.screen.blit(textSurface, (650, 410))

        pygame.display.flip()
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() is False:
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()
