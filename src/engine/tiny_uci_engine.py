#!/usr/bin/env python3
# Tiny UCI Chess Engine with Difficulty Levels
# This engine supports easy, hard, and master difficulty levels.
# It can play against a human or another engine using the UCI protocol.

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import time
import math
import random
import chess
from utils.difficulty import set_difficulty


# ---------- TUNABLES ----------
PIECE_VALUES = {
    chess.PAWN:   100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK:   500,
    chess.QUEEN:  900,
    chess.KING:   0,    # evaluated via PST/safety if desired
}

# Piece-square tables for evaluation
PST = {
    chess.PAWN:   [...],  # Add piece-square table values here
    chess.KNIGHT: [...],
    chess.BISHOP: [...],
    chess.ROOK:   [...],
    chess.QUEEN:  [...],
    chess.KING:   [...],
}

# Search parameters
INF = 10_000_000
TT_EXACT, TT_LOWER, TT_UPPER = 0, 1, 2

class TTEntry:
    __slots__ = ("zob", "depth", "flag", "score", "best_move")
    def __init__(self, zob, depth, flag, score, best_move):
        self.zob = zob
        self.depth = depth
        self.flag = flag   # EXACT / LOWER / UPPER
        self.score = score
        self.best_move = best_move

class TranspositionTable:
    def __init__(self, size_mb=32):
        self.size = (size_mb * 1024 * 1024) // 24  # rough slot estimate
        self.table = {}

    def get(self, key):
        return self.table.get(key % self.size)

    def store(self, key, entry: TTEntry):
        self.table[key % self.size] = entry

# ---------- EVALUATION ----------
def evaluate(board: chess.Board) -> int:
    """Evaluate the board position based on material and piece-square tables."""
    score = 0
    for piece_type in PIECE_VALUES:
        for sq in board.pieces(piece_type, chess.WHITE):
            score += PIECE_VALUES[piece_type] + PST[piece_type][sq]
        for sq in board.pieces(piece_type, chess.BLACK):
            score -= PIECE_VALUES[piece_type] + PST[piece_type][chess.square_mirror(sq)]
    return score if board.turn == chess.WHITE else -score

# ...existing code...

def move_score(board: chess.Board, move: chess.Move, tt_best: chess.Move | None):
    """Assign a score to a move for move ordering."""
    score = 0
    # Prioritize the transposition table best move
    if tt_best is not None and move == tt_best:
        score += 10000
    # Prioritize captures
    if board.is_capture(move):
        score += 1000
    # Prioritize promotions
    if move.promotion:
        score += 500
    # Otherwise, neutral
    return score

# ...existing code...

# ---------- MOVE ORDERING ----------
def ordered_moves(board: chess.Board, tt_best: chess.Move | None):
    moves = list(board.legal_moves)
    moves.sort(key=lambda m: move_score(board, m, tt_best), reverse=True)
    return moves

# ---------- SEARCH ----------
class Searcher:
    def __init__(self):
        self.tt = TranspositionTable(size_mb=64)
        self.start_time = 0.0
        self.stop_time = 0.0
        self.nodes = 0

    def time_up(self) -> bool:
        return time.time() >= self.stop_time

    def negamax(self, board: chess.Board, depth, alpha, beta, ply=0):
        self.nodes += 1
        if depth <= 0:
            return evaluate(board)

        best_move = None
        value = -INF
        for move in ordered_moves(board, best_move):
            if self.time_up():
                break
            board.push(move)
            score = -self.negamax(board, depth-1, -beta, -alpha, ply+1)
            board.pop()

            if score > value:
                value = score
                best_move = move
            if value > alpha:
                alpha = value
            if alpha >= beta:
                break

        return value

    def iterative_deepening(self, board: chess.Board, max_time_s=2.0, max_depth=64):
        self.start_time = time.time()
        self.stop_time = self.start_time + max_time_s
        best_move = None

        for depth in range(1, max_depth + 1):
            if self.time_up():
                break
            score = self.negamax(board, depth, -INF, INF, 0)
            best_move = best_move or random.choice(list(board.legal_moves))

        return best_move

# ---------- UCI LOOP ----------
def uci_loop():
    board = chess.Board()
    engine = Searcher()

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        cmd = line.strip()

        if cmd == "uci":
            print("id name TinyUCI-LearnEngine")
            print("id author You+GPT")
            print("uciok", flush=True)

        elif cmd.startswith("position"):
            # Handle position commands
            pass

        elif cmd.startswith("go"):
            # Handle go commands and difficulty settings
            difficulty = set_difficulty(cmd)
            best_move = engine.iterative_deepening(board, max_time_s=2.0)
            print(f"bestmove {best_move.uci()}", flush=True)

        elif cmd == "quit":
            break

if __name__ == "__main__":
    uci_loop()