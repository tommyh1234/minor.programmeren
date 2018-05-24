# Algorithms
This folder contains all the algorithms that this application can run. Each algorithm is based off of the `algorithm.py` base class. This class does not contain much functionality but rather serves as a template to bass the other algorithms off of.

## Structure
Each algorithm consists of two main parts: a init funciton and a execute function. The init function contains all logic to prepare an area for the algorithm. This can include calling other algorithms! Next to that it also handles all of the setup for the algorithms own state containing information such as move counts and past prices.

The execute function is where the actual logic of the algorithm happens. This function is called upon consecutively many times until the algorithm sets `self.isDone` to true. This allows algorithms to work with radically different logic and runtimes.

## The available algorithms
There are several algorithms available:
* Random (randomalg.py)
* Speedrandom (speedrandom.py)
* Hill Climbing (hillClimbing.py)
* Simmulated Annealing (also hillClimbing.py)

Random is a algorithm that tries to randomly fill a map within 1500 tries. If it doesn't succeed it restarts until it eventually does succeed.

Speedrandom is much the same like random but with fewer prints. This is used in other algorithms to generate a map to start from.

Hill climbing is a algorithm that tries to improve a given (or generated) map by randomly moving, switching or rotating a house. After every move the score is calculated. If the score is lower the move is reverted and a new move is tried.

Simmulated annealing resides in the same file as hill climbing. The two algorithms are largely similar. When simmulated annealing gets a unbeneficial move it has a chance to still accept the move based on a cooling function. Wether simmulated annealing is used or not depends on what paramaters are passed to the algorithm on initialisation.