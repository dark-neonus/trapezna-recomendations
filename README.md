# PageRank-Based Recommendation Application for "Trapezna"

## Project Overview

This project implements a recommendation system for the "Trapezna," based on the PageRank algorithm. The system helps users discover dishes tailored to their preferences by analyzing user sessions and connections between the ingredients in various dishes. Additionally, the application offers a visualization feature to explore these connections as a graph.

## Features

1. **Personalized Recommendations:**
   - Analyzes user choices during food orders.
   - Builds connections between user sessions and dish ingredients.
   - Recommends dishes that contain the user's preferred products.

2. **Graph Visualization:**
   - Displays the connections between user sessions, dishes, and their ingredients as an interactive graph.

## How It Works

1. **Session Analysis:**
   - Tracks user sessions to identify preferences based on ordered dishes.
2. **Ingredient Mapping:**
   - Maps dishes to their ingredients to establish a network of connections.
3. **PageRank Algorithm:**
   - Applies the PageRank algorithm to prioritize dishes containing popular or user-favored ingredients.
4. **Recommendations:**
   - Generates a ranked list of recommended dishes for the user.

## Technologies Used

- **Programming Language:** Python
- **Graph Libraries:** NetworkX, Matplotlib (for graph generation and visualization)
- **Data Handling:** Pandas, SQLite (or any database solution for user session tracking)
- **Web Framework (optional):** Flask/Django (if the application has a web-based interface)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name/pagerank-recommendation-app.git
   cd pagerank-recommendation-app
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the database (if applicable):
   ```bash
   python setup_database.py
   ```

4. Run the application:
   ```bash
   python app.py
   ```

## Usage

1. Launch the application.
2. Log in or create a user profile.
3. Browse and order dishes from "Trapezna."
4. View personalized dish recommendations based on your preferences.
5. Explore the graph visualization to understand ingredient connections.

## Future Enhancements

- Adding support for dietary restrictions and allergens.
- Enhancing the graph visualization with interactive features.
- Implementing a feedback loop to refine recommendations.

## Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation of your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any inquiries or support, please contact us at [your-email@example.com].
