from flask import Flask, render_template, request, jsonify
from engine.tiny_uci_engine import Searcher
from utils.difficulty import set_difficulty

app = Flask(__name__)

# Initialize the chess engine
engine = Searcher()

@app.route('/')
def index():
    # Render the main chess game interface
    return render_template('index.html')

@app.route('/set_difficulty', methods=['POST'])
def set_difficulty_route():
    # Set the difficulty level for the chess engine
    difficulty = request.json.get('difficulty')
    set_difficulty(engine, difficulty)
    return jsonify({"status": "success", "difficulty": difficulty})

@app.route('/make_move', methods=['POST'])
def make_move():
    # Handle a move made by the player
    move = request.json.get('move')
    board_state = request.json.get('board_state')
    
    # Update the engine's board state and make the move
    engine.board.set_fen(board_state)
    engine.board.push_uci(move)
    
    # Get the engine's response move
    engine_move = engine.iterative_deepening(engine.board)
    
    # Return the engine's move and the updated board state
    return jsonify({
        "engine_move": engine_move.uci(),
        "board_state": engine.board.fen()
    })

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode for development
