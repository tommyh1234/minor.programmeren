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
This codebase will be written in Python 3.6.3. Older versions of python should be used at users own risk. We have verified that this codebase won't work with Python 2.7. We will put all the requirements in requirements.txt, which can be installed by using ```pip install -r requirements.txt```

## Authors
* Tommy Hokkeling
* Jos Vlaar
* Pim ten Thije

## Structure
The program is run from `python3 application.py`. Any given run consist of three important classes. Area is the data model and deals with storing, validating and scoring a state. An algorithm class is the meat of the program, this is where all the nifty stuff happens. Then there are visualizers. These are what actually run an algorithm. Since drawing and executing happen in the same loop it was decided to have this all handled by the visualizers. Each of these three are kept in seperate folders with seperate readme's goin into more detail.

## Stickler Linting
This project uses Stickler-CI to check all pull requests for code linting errors and tries to fix them where possible.

## Git pre-commit hook
Everyone working on this project is required to install a flake8 pre-commit hook. This is to ensure good code quality and consistent styling.
To know how look at: https://www.smallsurething.com/how-to-automatically-lint-your-python-code-on-commit/

## Acknowledgments
We would like to thank our techassist Bart van Baal voor his indispensable advice; our lecturer Daan van den Berg for the provided inspiration and our class for the necessary feedback.
