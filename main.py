""" Main script that runs program """

import argparse
from ui import main_loop, clear_graph, GRAPH_FILE
from graph_visualization_png import generate_graph_png, organise_graph
from graph_visualization_animation import create_scene
from graph_logic import load_graph


def main():
    """ Main function that runs program """

    # Think to parse arguments from terminal, for example:
    # python main.py --visualization
    parser = argparse.ArgumentParser()

    parser.add_argument("--visualization",
                        help="run visualization animation for graph.json",
                        action="store_true")

    parser.add_argument("--visualization_png",
                        help="save png of graph visualization",
                        action="store_true")

    parser.add_argument("--clear",
                        help="clear current graph.json with preferences",
                        action="store_true")
    # Get given parameters from terminal
    args = parser.parse_args()

    if args.visualization:
        scene = create_scene(load_graph(GRAPH_FILE))
        scene.render(True)
    elif args.visualization_png:
        generate_graph_png(organise_graph(load_graph(GRAPH_FILE)), "graph")
    elif args.clear:
        clear_graph()
    else:
        main_loop()

if __name__ == "__main__":
    main()
