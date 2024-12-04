# PageRank-Based Recommendation Application for "Trapezna"

## Project Overview

This project implements a recommendation system for the "Trapezna," based on the PageRank algorithm. The system helps users discover dishes tailored to their preferences by analyzing user sessions and connections between the ingredients in various dishes. Additionally, the application offers a visualization feature to explore these connections as a graph.

## Features

1. **Personalized Recommendations:**
   - Analyzes user choices during food orders.
   - Builds connections between user sessions and dish ingredients.
   - Recommends dishes that contain the user's preferred products.

2. **Graph Visualization:**
   - Displays the connections between user sessions and the dishes' ingredients as an interactive graph.

## How It Works

1. **Session Analysis:**
   - Tracks user sessions to identify preferences based on ordered dishes.
2. **Ingredient Mapping:**
   - Maps dishes to their ingredients to establish a network of connections.
3. **PageRank Algorithm:**
   - Applies the PageRank algorithm to prioritize dishes containing popular or user-favored ingredients.
4. **Recommendations:**
   - Generates a ranked list of recommended dishes for the user.

## Principles of Discrete Mathematics
1. **Graph Theory**
   - Nodes (products) and edges (session relationships) form the core of the analysis.
2. **Node Weighting**
   - Importance is derived from connections, akin to PageRank.
3. **Ranking Algorithms**
   - Items are sorted by their computed weight or power.


## Split Tasks
1. **UI**
   - Nazar took over the implementation of the interface.
2. **PageRank**
   - How to implement algorithms for converting dishes into products and calculating ranks - distributed by Iya and Oleksiy.
3. **Graph**
   - creation of a popularity graph and implementation of the output - Maria and Daria.

## Technologies Used

- **Programming Language:** Python
- **Graph Libraries:** graphviz (for graph visualization)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dark-neonus/trapezna-recomendations.git
   cd trapezna-recomendations
   ```

2. Install required dependencies:
   ### Install the Necesarry Library: graphviz
   ```bash
   pip install graphviz
   ```
   #### Instalation steps:
   ##### Windows
   1. Download the Graphviz installer from Graphviz Downloads.
   2. Run it through and follow the prompt.
   3. Add the Graphviz bin directory to your system PATH.

   ##### MacOS: use Homebrew
   ```bash
   brew install graphviz
   ```
   ##### Linux:
   - Debian-based:
   ```bash
   sudo apt-get install graphviz
   ```
   - Red Hat-based:
   ```bash
   sudo yum install graphviz
   ```

3. Run the application:
   ```bash
   python3 main.py
   ```

## Usage

1. Launch the application.
2. Browse and order dishes from "Trapezna."
3. For the next time view personalized dish recommendations based on your preferences.
4. Explore the graph visualization to understand ingredient connections.

## Feedback 
   - Our assistant Anton - has been helping us throughout the whole work and he always answered our questions. He offered valuable advice on structuring project, splitting tasks and realization of PageRank algorithm. The assistant offered suggestions to enhance the documentation and made sure all project requirements were addressed.


## Thanks to developers

- Nazar [pasichnyk.pn@ucu.edu.ua] 
- Daryna [onopriienko.pn@ucu.edu.ua] 
- Iia [maharyta.pn@ucu.edu.ua]
- Maria [hamaniuk.pn@ucu.edu.ua]
- Oleksii [lasiichuk.pn@ucu.edu.ua]
