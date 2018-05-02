# AmstelHaege - Team 3
We're developping a new neighbourhoud in Duivendrecht of 160x180m. There are three scenarios to build houses here: one with 20 homes, one with 40 homes and one with 60 homes. In this project we try to find the neigbourhood with the highest monetary value by placing the houses on a map. The map has to adhere to the following constraints:

| Type        	| Amount 	| Dimensions 	| Value    	| (1, 2)Free space 	| Value addition per m free space 	|
|-------------	|--------	|------------	|----------	|------------------	|---------------------------------	|
| Family Home 	| 60%    	| 8 x 8m     	| €285.000 	| 2m            	| 3% (€8.550)                     	|
| Bungalow    	| 25%    	| 10 x 7.5m  	| €399.000 	| 3m            	| 4% (€15.960)                    	|
| Mansion     	| 15%    	| 11 x 10.5m 	| €610.000 	| 6m            	| 6% (€36.600)                    	|

There is also water in the neighbourhoud: 20% of the total area should be covered in water and may be split up in max. four different oval or rectangualr ponds with a maximimal height:width ratio of 1:4. 

* (1) The free space of a house is the smallest distance to the nearest house in the neighbourhood, calculated from the walls of the houses. For example: for a free space of 6m all houses in the surrounding should be at a minimum of 6m from the house.
* (2) Required free space has to be within the boundaries of the map.
* (3) All constraints (dutch) can be found at http://heuristieken.nl/wiki/index.php?title=Amstelhaege

## Prerequisites
This codebase will be written in Python 3.6.3. We will put all the requirements in requirements.txt, which can be installed by using ```pip install -r requirements.txt```

## Authors
* Tommy Hokkeling
* Jos Vlaar
* Pim ten Thije

## Structure
In the folder 'objects' we've created a House class (which is inheritated by the familyHome, Bungalow and Mansion classes) and an area class to represent the map. Water will be added later as a seperate class. This entry will be updated as we expand our code... 

## Stickler Linting
This project uses Stickler-CI to check all pull requests for code linting errors and tries to fix them where possible.

## Git pre-commit hook
Everyone working on this project is required to install a flake8 pre-commit hook. This is to ensure good code quality and consistent styling.
To know how look at: https://www.smallsurething.com/how-to-automatically-lint-your-python-code-on-commit/

## Acknowledgments
We would like to thank our techassist Bart van Baal voor his indispensable advice and our lecturer Daan van den Berg for his inspiration.