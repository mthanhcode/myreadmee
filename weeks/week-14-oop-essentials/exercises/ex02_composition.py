"""Exercise 02: compose Bot with a strategy."""

from collections.abc import Callable

State = dict[str, int]
Strategy = Callable[[State], str]


class Bot:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def choose_action(self, state: State) -> str:
        return self.strategy(state)


def move_toward_goal(state: State) -> str:
    """Move one step toward goal, whether it is to the left or right."""
    if state["position"] < state["goal"]:
        return "right"
    if state["position"] > state["goal"]:
        return "left"
    return "wait"


def defensive(state: State) -> str:
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: State) -> str:
    return move_toward_goal(state)


def aggressive(state: State) -> str:
    return move_toward_goal(state)


if __name__ == "__main__":
    state = {"position": 1, "opponent_position": 4, "goal": 4}
    for name, strategy in (
        ("defensive", defensive),
        ("balanced", balanced),
        ("aggressive", aggressive),
    ):
        print(f"{name}: {Bot(strategy).choose_action(state)}")
