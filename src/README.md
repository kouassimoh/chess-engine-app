# Chess Engine Application

This project is a chess engine application that allows users to play chess against an AI engine or another player. The engine supports different difficulty levels (easy, hard, master) and is built using the Universal Chess Interface (UCI) protocol. The application features a web interface for an interactive chess experience.

## Project Structure

The project is organized into the following directories and files:

- **src/**
  - **engine/**: Contains the chess engine implementation.
    - `tiny_uci_engine.py`: The main engine file implementing UCI protocol, move generation, evaluation, and search algorithms.
    - `__init__.py`: Marks the engine directory as a Python package.
  - **web/**: Contains the web application files.
    - `app.py`: The entry point for the Flask web server, handling routing and serving the chess game interface.
    - **templates/**: Contains HTML templates for the web application.
      - `index.html`: The main HTML structure for the chess game interface.
    - **static/**: Contains static files such as JavaScript and CSS.
      - `chessboard.js`: JavaScript code for managing the chessboard UI and user interactions.
  - **utils/**: Contains utility functions.
    - `difficulty.py`: Functions to set the difficulty level of the chess engine.

## Requirements

To run this project, you need to install the following dependencies:

- Python 3.x
- Flask
- python-chess

You can install the required Python packages using the following command:

```
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the `src/web` directory.
2. Run the Flask application:

```
python app.py
```

3. Open your web browser and go to `http://127.0.0.1:5000` to access the chess game interface.

## Difficulty Levels

The chess engine supports three difficulty levels:

- **Easy**: The engine plays with a limited search depth, making it easier for beginners.
- **Hard**: The engine uses a moderate search depth and evaluation, providing a balanced challenge.
- **Master**: The engine plays at its highest capability, using advanced search techniques and evaluations.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.