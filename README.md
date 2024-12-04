# PageRank-Based Recommendation Application for "Trapezna"

## Project Overview

This project implements a recommendation system for the "Trapezna," based on the PageRank algorithm. The system helps users discover dishes tailored to their preferences by analyzing user sessions and connections between the ingredients in various dishes. Additionally, the application offers a visualization feature to explore these connections as a graph.

## Steps We Implemented

1. **Graph Modeling**
   - Designed a graph structure to represent sessions and product relationships.
2. **PageRank Algorithms**
   - Implemented logic to rank products and dishes based on their connections and importance.
3. **Recommendations**
   - Created mechanisms for sorting and recommending dishes based on their calculated importance.

## Features

1. **Personalized Recommendations:**
   - Analyzes user choices during food orders.
   - Builds connections between user sessions and dish ingredients.
   - Recommends dishes that contain the user's preferred products.

2. **Graph Visualization:**
   - Displays the connections between user sessions and the dishes' ingredients as an interactive graph.

3. **Graph Logic**
   1. Graph Management
      - Save Graph (save_graph): Saves the graph to a JSON file for persistence.
      - Load Graph (load_graph): Loads a graph from a JSON file, creating an empty file if one doesn’t exist.
      - Add Session (add_session): Adds a session of products to the graph.
   2. Menu Processing
      - Structure Menu (structure_menu): Transforms a nested dictionary of dishes and products into a flat, usable structure.
      - Dishes to Products (dishes_to_products): Extracts all products used in the selected dishes.
   3. Power Calculation
      - Calculate Product Power (calculate_products_power): Computes the power of each product based on its frequency across sessions (PageRank-inspired logic).
      - Calculate Dish Power (calculate_dishes_power): Aggregates product powers to compute the power of dishes.
   4. Ranking and Categorization
      - Sort Dishes (sort_dishes): Ranks dishes by their power in descending order.
      - Divide Dishes by Type (divide_dishes_by_type): Groups dishes into categories based on their type.

     

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

## Implemented Algorithms
1. **Graph Storage and Manipulation**
   - Functions for saving, loading, and updating graphs.
2. **PageRank Logic**
   - Calculating the "importance" of nodes (products).
3. **Aggregating node importance to evaluate dish relevance**
   - Ranking and Categorization: Sorting and grouping dishes by importance and type.

## Split Tasks
1. **UI**
   - Nazar took over the implementation of the interface and program loop.
2. **PageRank**
   - How to implement algorithms for converting dishes into products and calculating ranks - distributed by Iya and Oleksiy.
3. **Graph**
   - Create logic of graph and working with graph file - Maria.
4. **Graph**
   - Visualization of graph - Daria.

## Technologies Used

- **Programming Language:** Python
- **Graph Libraries:** graphviz and manim (for graph visualization)

## Installation

1. ### Clone the repository:
   ```bash
   git clone https://github.com/dark-neonus/trapezna-recomendations.git
   cd trapezna-recomendations
   ```

Here’s the updated README section with instructions for activating the virtual environment on different systems:

---

2. ### Create virtual environment
   > Be aware that the way of calling python may be different on different systems.  
   > For Linux and MacOS, use `python` or `python3`. For Windows, use `python` or `py`. Further we will use `python` to show you commands, please, use one that suites your system.

   Now, using the appropriate python command for your system, run the following command in your repository folder (e.g., `trapezna-recomendations`):

   ```bash
   python -m venv .venv
   ```

   **Activate the virtual environment**:
   - On **Linux/MacOS**:
     ```bash
     source .venv/bin/activate
     ```
   - On **Windows (Command Prompt)**:
     ```cmd
     .venv\Scripts\activate
     ```
   - On **Windows (PowerShell)**:
     ```powershell
     .venv\Scripts\Activate.ps1
     ```

   After activation, the command prompt will show the virtual environment name (e.g., `(venv)`), indicating that the environment is active.

3. ### Install required dependencies:
   #### Install Graphviz
   Follow instruction from [official graphviz site](https://graphviz.org/download/) to install it for your system.
   #### Install Graphviz
   Follow instruction from [official manim site](https://docs.manim.community/en/stable/installation.html) to install it for your system.

   After that go to app folder and activate `.venv` environment(if this wasn't done yet).
   To finally install all required python libraries, run next command:
   ```bash
   pip install graphviz manim
   ``` 


4. ### Run the application:
   ```bash
   python main.py
   ```
Here's the completed **Usage** section with detailed instructions for the application's command-line options:

---

## Usage
   > Make sure that you run the program with its environment activated.  

   ### Standard User Interface
   To run the standard user interface, use the following command:
   ```bash
   python main.py
   ```

   ### Terminal Options
   The Trapezna Recommendation app has several terminal options to modify its behavior. Below is a list of available commands:

   1. ### Help Command
      Display information about available terminal options:
      ```bash
      python main.py --help
      ```

   2. ### Visualization Mode
      Run a visualization animation for the graph stored in `graph.json`:
      ```bash
      python main.py --visualization
      ```

   3. ### Save Visualization as PNG
      Generate and save a PNG file representing the graph stored in `graph.json`:
      ```bash
      python main.py --visualization_png
      ```

   4. ### Clear Graph Data
      Clear the current `graph.json` file, removing all preferences and data:
      ```bash
      python main.py --clear
      ```

## Feedback 
   - Our assistant Anton - has been helping us throughout the whole work and he always answered our questions. He offered valuable advice on structuring project, splitting tasks and realization of PageRank algorithm. The assistant offered suggestions to enhance the documentation and made sure all project requirements were addressed.


## Thanks to developers

- Nazar [pasichnyk.pn@ucu.edu.ua] 
- Daryna [onopriienko.pn@ucu.edu.ua] 
- Iia [maharyta.pn@ucu.edu.ua]
- Maria [hamaniuk.pn@ucu.edu.ua]
- Oleksii [lasiichuk.pn@ucu.edu.ua]
