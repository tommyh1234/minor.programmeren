# Visualizers

Visualizers are both the runners and the visualisation of the program. Since the logic loop and the rendering loop are one and the same we decided to bring these two functionalities together in a single class.

There are two kinds of visualizers, single and bulk. Each has two variants. The single visualizer runs a given algorithm a single time while the bulk visualizer can run a algorithm many time. The bulk visualizer extends the normal visualizer (it will however only vizualize the area that was created last). The only difference is in what it does when the algorithm tells it it's done.

Both visualizers also have a nodraw variant. This variant does not render anything to the screen but instead only outputs to the terminal and saves to files

## Pygame & Matplotlib
For the visualizations initially only pygame was used. Pygame is used to both create a loop that calls to the algorithm and to render to the screen. Drawing graphs in pygame quickly grew cumbersome so the choice was made to use matplotlib for this instead and to include the created graphs in the pygame render.