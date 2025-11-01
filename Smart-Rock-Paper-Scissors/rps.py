import json
import os
import random
import time
from collections import defaultdict, Counter
from typing import Dict, List, Tuple

SAVE_FILE = "rps_save.json"
MOVES = ["rock", "paper", "scissors"]
BEATS = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
COUNTER = {m: [x for x in MOVES if x != BEATS[m]][0] for m in MOVES}

# ------------------ Persistence ------------------

def save_state(state: Dict):
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(state, f, indent=2)
    except Exception as e:
        print(f"Warning: could not save state ({e})")

def load_state() -> Dict:
    if not os.path.exists(SAVE_FILE):
        return {}
    try:
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {}

# ------------------ Opponents ------------------

class RandomOpponent:
    def choose(self, _: List[str]) -> str:
        return random.choice(MOVES)

class PatternOpponent:
    def __init__(self):
        self.history: List[str] = []

    def _suffix_prediction(self) -> Tuple[str, float]:
        H = self.history
        for L in range(min(6, len(H)), 0, -1):
            suffix = tuple(H[-L:])
            counts = Counter()
            for i in range(len(H) - L):
                if tuple(H[i:i + L]) == suffix and i + L < len(H):
                    counts[H[i + L]] += 1
            if counts:
                nxt, cnt = counts.most_common(1)[0]
                total = sum(counts.values())
                return nxt, cnt / total
        return None, 0.0

    def choose(self, player_history: List[str]) -> str:
        self.history = player_history
        if len(self.history) < 3:
            return random.choice(MOVES)
        pred, conf = self._suffix_prediction()
        if pred and conf > 0.4 and random.random() < 0.85:
            return COUNTER[pred]
        recent = self.history[-6:]
        freq = Counter(recent).most_common()
        if freq and random.random() < 0.7:
            most = freq[0][0]
            return COUNTER[most]
        return random.choice(MOVES)

class PredictiveOpponent:
    def __init__(self, state: Dict = None):
        self.trans: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
        self.unigrams: Counter = Counter()
        self.total_seen = 0
        if state:
            self._load_state(state)

    def _load_state(self, state: Dict):
        trans = state.get("trans", {})
        for k, v in trans.items():
            for nxt, cnt in v.items():
                self.trans[k][nxt] = cnt
        self.unigrams = Counter(state.get("unigrams", {}))
        self.total_seen = state.get("total_seen", 0)

    def get_state(self) -> Dict:
        return {
            "trans": {k: dict(v) for k, v in self.trans.items()},
            "unigrams": dict(self.unigrams),
            "total_seen": self.total_seen,
        }

    def update(self, last_moves: List[str], next_move: str):
        self.total_seen += 1
        self.unigrams[next_move] += 1
        if len(last_moves) >= 2:
            k = ",".join(last_moves[-2:])
            self.trans[k][next_move] += 1
        elif len(last_moves) == 1:
            k = last_moves[-1]
            self.trans[k][next_move] += 1

    def predict(self, last_moves: List[str]) -> Tuple[str, float]:
        if len(last_moves) >= 2:
            k = ",".join(last_moves[-2:])
            counts = self.trans.get(k)
            if counts:
                total = sum(counts.values())
                pred = max(counts, key=counts.get)
                return pred, counts[pred] / total
        if len(last_moves) >= 1:
            k = last_moves[-1]
            counts = self.trans.get(k)
            if counts:
                total = sum(counts.values())
                pred = max(counts, key=counts.get)
                return pred, counts[pred] / total
        if self.total_seen > 0:
            pred = self.unigrams.most_common(1)[0][0]
            return pred, self.unigrams[pred] / self.total_seen
        return None, 0.0

    def choose(self, last_moves: List[str]) -> str:
        pred, conf = self.predict(last_moves)
        if not pred or conf < 0.35 or random.random() < 0.12:
            return random.choice(MOVES)
        return COUNTER[pred]

# ------------------ Game Logic ------------------

class RPSGame:
    def __init__(self):
        self.player_history: List[str] = []
        self.scores = {"player": 0, "opponent": 0, "tie": 0}
        self.best_streak = 0
        self.win_streak = 0
        self.opp_mode = None
        self.pred_opponent: PredictiveOpponent = None
        self.pattern_opponent: PatternOpponent = None
        self.random_opponent = RandomOpponent()
        self.load_progress()

    def load_progress(self):
        raw = load_state()
        if not raw:
            return
        stats = raw.get("stats", {})
        self.scores = stats.get("scores", self.scores)
        self.best_streak = stats.get("best_streak", 0)
        self.player_history = raw.get("player_history", [])
        state = raw.get("predictive_state")
        self.pred_opponent = PredictiveOpponent(state) if state else PredictiveOpponent()
        self.pattern_opponent = PatternOpponent()

    def save_progress(self):
        state = {
            "stats": {
                "scores": self.scores,
                "best_streak": self.best_streak,
            },
            "player_history": self.player_history[-2000:],
            "predictive_state": self.pred_opponent.get_state() if self.pred_opponent else {},
            "saved_at": time.time(),
        }
        save_state(state)

    def set_mode(self, mode: str):
        mode = mode.lower()
        if mode == "easy":
            self.opp_mode = "easy"
        elif mode == "medium":
            self.opp_mode = "medium"
        elif mode == "hard":
            self.opp_mode = "hard"
        else:
            raise ValueError("unknown mode")

    def _choose_opponent_move(self) -> str:
        if self.opp_mode == "easy":
            return self.random_opponent.choose(self.player_history)
        if self.opp_mode == "medium":
            if not self.pattern_opponent:
                self.pattern_opponent = PatternOpponent()
            return self.pattern_opponent.choose(self.player_history)
        if self.opp_mode == "hard":
            if not self.pred_opponent:
                self.pred_opponent = PredictiveOpponent()
            return self.pred_opponent.choose(self.player_history)
        return random.choice(MOVES)

    def _resolve(self, p_move: str, o_move: str) -> str:
        if p_move == o_move:
            return "tie"
        if BEATS[p_move] == o_move:
            return "player"
        return "opponent"

    def _update_after_round(self, p_move: str, o_move: str, result: str):
        if result == "player":
            self.scores["player"] += 1
            self.win_streak += 1
            self.best_streak = max(self.best_streak, self.win_streak)
        elif result == "opponent":
            self.scores["opponent"] += 1
            self.win_streak = 0
        else:
            self.scores["tie"] += 1
        if self.pred_opponent:
            self.pred_opponent.update(self.player_history, p_move)
        self.player_history.append(p_move)
        if len(self.player_history) > 2000:
            self.player_history = self.player_history[-2000:]

    def play_round(self, p_move: str) -> Tuple[str, str, str]:
        p_move = p_move.lower()
        if p_move not in MOVES:
            raise ValueError("invalid move")
        o_move = self._choose_opponent_move()
        result = self._resolve(p_move, o_move)
        self._update_after_round(p_move, o_move, result)
        return p_move, o_move, result

    def stats_text(self) -> str:
        total = sum(self.scores.values())
        return (f"Played: {total} | Player: {self.scores['player']} | Opponent: {self.scores['opponent']} | "
                f"Ties: {self.scores['tie']} | Best Win Streak: {self.best_streak}")

# ------------------ CLI ----------------

def print_menu():
    print("\n--- Rock Paper Scissors — Smart Mode ---")
    print("Type: rock / paper / scissors to play")
    print("Commands: mode, stats, save, quit, reset")
    print("Modes: easy, medium, hard")

def main():
    game = RPSGame()
    print_menu()
    game.set_mode("easy")
    print("Current mode: easy (change with: mode easy|medium|hard)")
    while True:
        try:
            cmd = input('Your Move >').strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting — progress saved.")
            game.save_progress()
            break
        if not cmd:
            continue
        if cmd in ("quit", "exit"):
            print("Goodbye — saving progress.")
            game.save_progress()
            break
        if cmd == "save":
            game.save_progress()
            print("Progress saved.")
            continue
        if cmd == "stats":
            print(game.stats_text())
            continue
        if cmd.startswith("mode"):
            parts = cmd.split()
            if len(parts) == 1:
                print(f"Current mode: {game.opp_mode}")
                continue
            try:
                game.set_mode(parts[1])
                print(f"Mode set to {parts[1]}")
            except Exception:
                print("Unknown mode. Available: easy, medium, hard")
            continue
        if cmd == "reset":
            confirm = input("Are you sure? This clears saved progress (yes/no): ").strip().lower()
            if confirm in ("y", "yes"):
                game = RPSGame()
                game.set_mode("easy")
                if os.path.exists(SAVE_FILE):
                    try:
                        os.remove(SAVE_FILE)
                    except Exception:
                        pass
                print("Progress reset.")
            continue
        if cmd in MOVES:
            p, o, res = game.play_round(cmd)
            if res == "player":
                print(f"You played {p} — Opponent {o} => You win!")
            elif res == "opponent":
                print(f"You played {p} — Opponent {o} => You lose.")
            else:
                print(f"You played {p} — Opponent {o} => It's a tie.")
            print(game.stats_text())
            continue
        print("Unknown command. Type rock/paper/scissors to play, or 'mode', 'stats', 'save', 'quit'.")

if __name__ == "__main__":
    main()
