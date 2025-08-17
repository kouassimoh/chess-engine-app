# Chess Engine Application

This project is a chess engine application that allows users to play chess against an AI engine or another player. The engine supports different difficulty levels: easy, hard, and master. The application is built using Flask for the web interface and utilizes the Universal Chess Interface (UCI) protocol for the chess engine.

## Project Structure

```
chess-engine-app
├── src
│   ├── engine
│   │   ├── tiny_uci_engine.py  # Implementation of the chess engine using UCI protocol
│   │   └── __init__.py         # Marks the engine directory as a Python package
│   ├── web
│   │   ├── app.py               # Entry point for the web application
│   │   ├── templates
│   │   │   └── index.html       # HTML structure for the chess game interface
│   │   └── static
│   │       └── chessboard.js    # JavaScript code for handling the chessboard UI
│   ├── utils
│   │   └── difficulty.py         # Functions to set the difficulty level of the chess engine
│   └── README.md                 # Documentation for the engine
├── requirements.txt              # Python dependencies required for the project
├── package.json                  # Configuration file for npm
└── README.md                     # Documentation for the project
```

## Features

- Play against a chess engine with adjustable difficulty levels (easy, hard, master).
- Play against another human player.
- Web-based interface for an interactive chess experience.
- Modular design for easy upgrades and maintenance.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd chess-engine-app
   ```

2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install JavaScript dependencies:
   ```
   npm install
   ```

## Usage

1. Start the Flask server:
   ```
   python src/web/app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` to access the chess game interface.

3. Select the difficulty level and start playing!

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.