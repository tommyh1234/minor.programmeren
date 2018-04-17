# a house 
class House(object):
    width = None
    height = None
    value = None
    gardenSize = None
    gardenValue = None
    houseSurface = None
    lotSurface = None

    def surface(self):
        return self.width * self.height

class Map(object):
    width = None
    height = None
    percMapFamilyHome = None
    percMapBungalowSurface = None
    percMapMansionSurface = None
    percMapWaterSurface = None
    percHouseFamilyHome = None
    percHouseBungalow = None
    percHouseMansion = None

    def getSurface(self):
        return self.width * self.height

    def getFamliyHomeSurface(self):
        return self.width * self.height * self.percMapFamilyHome

    def getBungalowSurface(self):
        return self.width * self.height * self.percMapBungalowSurface
    
    def getMansionSurface(self):
        return self.width * self.height * self.percMapMansionSurface

    def getWaterSurface(self):
        return self.width * self.height * self.percMapWaterSurface

    def getBuildableSurface(self):
        return self.getSurface() - self.getWaterSurface()

class Scenario(object):
    totHouseAmount = None
    famliyHomeAmount = None
    bungalowAmount = None
    mansionAmount = None
    familyHomeCovered = None
    bungalowCovered = None
    mansionCovered = None
    Uncovered = None

    def getFamilyHomeAmount(self, Map):
        return Map.percHouseFamilyHome * self.totHouseAmount

    def getBungalowAmount(self, Map):
        return Map.percHouseBungalow * self.totHouseAmount

    def getMansionAmount(self, Map):
        return Map.percHouseMansion * self.totHouseAmount

    def getUpperboundValue(self, Map, familyHome, bungalow, mansion):
        return self.getFamilyHomeAmount(Map) * familyHome.value \
               + self.getBungalowAmount(Map) * bungalow.value \
               + self.getMansionAmount(Map) * mansion.value

    def getFamilyHomeCovered(self, Map, House):
        return self.getFamilyHomeAmount(Map) * House.lotSurface

    def getBungalowCovered(self, Map, House):
        return self.getBungalowAmount(Map) * House.lotSurface

    def getMansionCovered(self, Map, House):
        return self.getMansionAmount(Map) * House.lotSurface

    def getUncovered(self, Map, familyHome, bungalow, mansion):
        covered = self.getFamilyHomeCovered(Map, familyHome) \
                + self.getBungalowCovered(Map, bungalow) \
                + self.getMansionCovered(Map, mansion)
        surface = Map.getBuildableSurface()
        water = Map.getWaterSurface()
        return surface - covered - water

##################
#initialze the map we're building on
ourMap = Map()
ourMap.width = 180
ourMap.height = 160
ourMap.percMapFamilyHome = 0.48
ourMap.percMapBungalowSurface = 0.20
ourMap.percMapMansionSurface = 0.12
ourMap.percMapWaterSurface = 0.20
ourMap.percHouseFamilyHome = 0.60
ourMap.percHouseBungalow = 0.25
ourMap.percHouseMansion = 0.15

#initialize Family Home
familyHome = House()
familyHome.width = 8.00
familyHome.height = 8.00
familyHome.value = 285000.00
familyHome.gardenSize = 2.00
familyHome.gardenValue = 0.03
familyHome.houseSurface = familyHome.width * familyHome.height
familyHome.lotSurface = (familyHome.gardenSize * 2 + familyHome.width) \
                        * (familyHome.gardenSize * 2 + familyHome.height)

#initialize Bungalow
bungalow = House()
bungalow.width = 10.00
bungalow.height = 7.50
bungalow.value = 399000.00
bungalow.gardenSize = 3.00
bungalow.gardenValue = 0.04
bungalow.houseSurface = bungalow.width * bungalow.height
bungalow.lotSurface = (bungalow.gardenSize * 2 + bungalow.width) \
                      * (bungalow.gardenSize * 2 + bungalow.height)

#initialize Mansion
mansion = House()
mansion.width = 11.00
mansion.height = 10.50
mansion.value = 610000.00
mansion.gardenSize = 6.00
mansion.gardenValue = 0.06
mansion.houseSurface = mansion.width * mansion.height
mansion.lotSurface = (mansion.gardenSize * 2 + mansion.width) \
                     * (mansion.gardenSize * 2 + mansion.height)

# initialize small, middle and large scenario's (nr of houses)
small = Scenario()
small.totHouseAmount = 20
small.famliyHomeAmount = small.getFamilyHomeAmount(ourMap)
small.bungalowAmount = small.getBungalowAmount(ourMap)
small.mansionAmount = small.getMansionAmount(ourMap)

middle = Scenario()
middle.totHouseAmount = 40
middle.famliyHomeAmount = middle.getFamilyHomeAmount(ourMap)
middle.bungalowAmount = middle.getBungalowAmount(ourMap)
middle.mansionAmount = middle.getMansionAmount(ourMap)

large = Scenario()
large.totHouseAmount = 60
large.famliyHomeAmount = large.getFamilyHomeAmount(ourMap)
large.bungalowAmount = large.getBungalowAmount(ourMap)
large.mansionAmount = large.getMansionAmount(ourMap)

#print some values
print('Our map:')
print('- is {}m by {}m'.format(ourMap.width, ourMap.height))
print('- contains:')
print('-- {}% Family homes'.format(ourMap.percMapFamilyHome*100))
print('-- {}% Bungalows'.format(ourMap.percMapBungalowSurface*100))
print('-- {}% Mansions'.format(ourMap.percMapMansionSurface*100))
print('-- {}% Water'.format(ourMap.percMapWaterSurface*100))
print('- The buildable surface contains:')
print('-- {}% Family homes'.format(ourMap.percHouseFamilyHome*100))
print('-- {}% Bungalows'.format(ourMap.percHouseBungalow*100))
print('-- {}% Mansions'.format(ourMap.percHouseMansion*100))
print('\n')

print('On a small map:')
print('- there are {} Family homes, {} Bungalows and {} Mansions.'.format(small.famliyHomeAmount,
                                                                          small.bungalowAmount,
                                                                          small.mansionAmount))
print('-- Family Homes cover {}m2 of the {}m2 available.'.format(small.getFamilyHomeCovered(ourMap,
                                                                                            familyHome),
                                                                 ourMap.getFamliyHomeSurface()))
print('-- Bungalows cover {}m2 of the {}m2 available.'.format(small.getBungalowCovered(ourMap,
                                                                                       bungalow),
                                                              ourMap.getBungalowSurface()))
print('-- Mansions cover {}m2 of the {}m2 available.'.format(small.getMansionCovered(ourMap,
                                                                                     mansion),
                                                             ourMap.getMansionSurface()))
print('-- {}m2 of the {}m2 buildable land is uncovered.'.format(small.getUncovered(ourMap,
                                                                                   familyHome,
                                                                                   bungalow,
                                                                                   mansion),
                                                                Map.getBuildableSurface(ourMap)))
print('- the max. value of all houses together is: ${}.'.format(small.getUpperboundValue(ourMap,
                                                                                         familyHome,
                                                                                         bungalow,
                                                                                         mansion)))
print('\n')

print('On a middle map:')
print('- there are {} Family homes, {} Bungalows and {} Mansions.'.format(middle.famliyHomeAmount,
                                                                          middle.bungalowAmount,
                                                                          middle.mansionAmount))
print('-- Family Homes cover {}m2 of the {}m2 available.'.format(middle.getFamilyHomeCovered(ourMap,
                                                                                             familyHome),
                                                                 ourMap.getFamliyHomeSurface()))
print('-- Bungalows cover {}m2 of the {}m2 available.'.format(middle.getBungalowCovered(ourMap,
                                                                                        bungalow),
                                                              ourMap.getBungalowSurface()))
print('-- Mansions cover {}m2 of the {}m2 available.'.format(middle.getMansionCovered(ourMap,
                                                                                      mansion),
                                                             ourMap.getMansionSurface()))
print('-- {}m2 of the {}m2 buildable land is uncovered.'.format(middle.getUncovered(ourMap,
                                                                                    familyHome,
                                                                                    bungalow,
                                                                                    mansion),
                                                                Map.getBuildableSurface(ourMap)))
print('The max. value of all houses together is: ${}.'.format(middle.getUpperboundValue(ourMap,
                                                                                        familyHome,
                                                                                        bungalow,
                                                                                        mansion)))
print('\n')
print('On a large map:')
print('- there are {} Family homes, {} Bungalows and {} Mansions.'.format(large.famliyHomeAmount,
                                                                          large.bungalowAmount,
                                                                          large.mansionAmount))
print('-- Family Homes cover {}m2 of the {}m2 available.'.format(large.getFamilyHomeCovered(ourMap,
                                                                                            familyHome),
                                                                 ourMap.getFamliyHomeSurface()))
print('-- Bungalows cover {}m2 of the {}m2 available.'.format(large.getBungalowCovered(ourMap,
                                                                                       bungalow),
                                                              ourMap.getBungalowSurface()))
print('-- Mansions cover {}m2 of the {}m2 available.'.format(large.getMansionCovered(ourMap,
                                                                                     mansion),
                                                             ourMap.getMansionSurface()))
print('-- {}m2 of the {}m2 buildable land is uncovered.'.format(large.getUncovered(ourMap,
                                                                                   familyHome,
                                                                                   bungalow,
                                                                                   mansion),
                                                                Map.getBuildableSurface(ourMap)))
print('The max. value of all houses together is: ${}.'.format(large.getUpperboundValue(ourMap,
                                                                                       familyHome,
                                                                                       bungalow,
                                                                                       mansion)))
print('\n')
print('Family Homes:')
print('- Family Home value: ${}'.format(familyHome.value))
print('- Family Home surface: {}m2'.format(familyHome.houseSurface))
print('- Family Home lot surface: {}m2'.format(familyHome.lotSurface))
print('Bungalows:')
print('- Bungalow value: ${}'.format(bungalow.value))
print('- Bungalow Home surface: {}m2'.format(bungalow.houseSurface))
print('- Bungalow lot surface: {}m2'.format(bungalow.lotSurface))
print('Mansions:')
print('- Mansion value: ${}'.format(mansion.value))
print('- Mansion surface: {}m2'.format(mansion.houseSurface))
print('= Mansion lot surface: {}m2'.format(mansion.lotSurface))