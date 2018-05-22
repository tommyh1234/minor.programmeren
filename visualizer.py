import pygame


class Visualizer:
    def __init__(self, area, algorithm):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 640, 770
        self.area = area
        self.algorithm = algorithm

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
        if self.algorithm.isDone is False:
            self.algorithm.execute()

        for i in range(0, 3):
            for j in range(0, 3):
                self.screen.blit(self.img_grass, (i * 270, j * 270))

        waterList = []
        waterList.extend(self.area.waterList)

        for water in waterList:
            # place water
            pygame.draw.rect(
                self.screen, (30, 144, 255),
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
        pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            (0, self.height - 50, self.width, 50)
            )

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
