# Objects

The objects folder contains all the classes that make up the data model of the project.

## Area
Area is a representation of a given map. Area contains a 2d array used as a grid as well as several arrays that keep track of all the houses and water that are placed on the area. Area also handles all the logic of changing its state. This means that placing houses, removing houses or rotating them for example all happen through the area class. Area also contains functions for validating the current state and calculating the price.

## Houses
All house types inherit from the House base class. Each house class contains information specific to that house such as the width, height and minimum free space. The House class contains functions relating to a individual house such as checking how much free space it has and what its value is. These functions are called upon by the area.

## Water
Water is implemented through the Water class. Water doesn't do much and thus this class doesn't do much either.