import random
from collections import deque


class SimpleReflexAgent:
    """
    Simple Reflex Agent
    Makes decisions only using the current percept.
    No memory is stored.
    """

    def sense_and_act(self, percept: dict) -> str:

        # Condition-Action Rules
        if percept["food_here"]:
            return "Up"

        elif percept["wall_ahead"]:
            return random.choice(["Left", "Right"])

        else:
            return "Up"


class ModelBasedAgent:
    """
    Model-Based Reflex Agent
    Maintains a small internal state to avoid loops.
    """

    def __init__(self):
        self.last_action = None
        self.turn_left_last_time = False

    def sense_and_act(self, percept: dict) -> str:

        # Update internal memory (Sensor Model)
        if percept["wall_ahead"]:

            # If we already turned left last time and still see a wall,
            # try turning right instead.
            if self.turn_left_last_time:
                action = "Right"
                self.turn_left_last_time = False
            else:
                action = "Left"
                self.turn_left_last_time = True

        elif percept["food_here"]:
            action = "Up"
            self.turn_left_last_time = False

        else:
            action = "Up"
            self.turn_left_last_time = False

        # Save previous action (Transition Model)
        self.last_action = action

        return action


class SearchAgent:
    """
    Breadth-First Search Agent
    Used only for Practical 03 and the autograder.
    """

    def bfs_search(self, start, goal, walls, grid_size):

        width, height = grid_size
        walls = set(walls)

        moves = [
            ("Up", (0, 1)),
            ("Down", (0, -1)),
            ("Left", (-1, 0)),
            ("Right", (1, 0))
        ]

        queue = deque()
        queue.append((start, []))

        visited = {start}

        while queue:

            position, path = queue.popleft()

            if position == goal:
                return path

            for action, (dx, dy) in moves:

                new_pos = (position[0] + dx, position[1] + dy)

                if (
                    0 <= new_pos[0] < width
                    and 0 <= new_pos[1] < height
                    and new_pos not in walls
                    and new_pos not in visited
                ):

                    visited.add(new_pos)
                    queue.append((new_pos, path + [action]))

        return None


class GreedyGridAgent:
    """
    Original Lab 01 Agent.
    Kept so older programs still work.
    """

    def __init__(self):
        self.actions_pool = ["Up", "Down", "Left", "Right"]

    def sense_and_act(self, percept):

        return random.choice(self.actions_pool)