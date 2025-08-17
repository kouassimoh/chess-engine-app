// chessboard.js
// This file contains the JavaScript code for handling the chessboard UI.
// It manages user interactions, updates the board state, and communicates
// with the Flask backend to send and receive moves.

const boardElement = document.getElementById('chessboard');
const statusElement = document.getElementById('status');
const difficultySelect = document.getElementById('difficulty');
let board;
let game = new Chess(); // Initialize a new chess game

// Function to render the chessboard
function renderBoard() {
    board = ChessBoard('chessboard', {
        draggable: true,
        position: 'start',
        onDrop: handleMove,
        onSnapEnd: onSnapEnd,
    });
}

// Function to handle moves made on the board
function handleMove(source, target) {
    const move = game.move({
        from: source,
        to: target,
        promotion: 'q' // Automatically promote to a queen
    });

    if (move === null) return 'snapback'; // Invalid move, snap back

    renderMoveHistory(game.history());
    updateStatus();

    // Send the move to the server
    sendMoveToServer(move);
}

// Function to send the move to the Flask backend
function sendMoveToServer(move) {
    fetch('/move', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ move: move })
    })
    .then(response => response.json())
    .then(data => {
        if (data.bestMove) {
            game.move(data.bestMove);
            renderMoveHistory(game.history());
            updateStatus();
        }
    });
}

// Function to render the move history
function renderMoveHistory(moves) {
    const historyElement = document.getElementById('move-history');
    historyElement.innerHTML = moves.join(', ');
}

// Function to update the game status
function updateStatus() {
    let status = '';

    if (game.inCheck()) {
        status = 'You are in check!';
    } else {
        status = 'Your turn';
    }

    if (game.game_over()) {
        status = 'Game over';
    }

    statusElement.innerHTML = status;
}

// Function to handle the end of a move
function onSnapEnd() {
    board.position(game.fen());
}

// Function to set the difficulty level
function setDifficulty() {
    const difficulty = difficultySelect.value;
    fetch('/set_difficulty', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ difficulty: difficulty })
    });
}

// Event listeners
difficultySelect.addEventListener('change', setDifficulty);

// Initialize the chessboard on page load
document.addEventListener('DOMContentLoaded', renderBoard);