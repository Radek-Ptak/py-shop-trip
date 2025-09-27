import json
import math
from typing import Dict, Any, List


Location = List[float, int]


def load_config(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, "r") as file:
            read_config = json.load(file)
        return read_config
    except FileNotFoundError:
        print(f"Error: Configuration file not found at {file_path}")


def calculate_distance(loc1: Location, loc2: Location) -> float:

    if len(loc1) != len(loc2):
        raise ValueError("Location must be of same length")

    squared_diff_sum = sum((loc1[i] - loc2[i]) ** 2 for i in range(len(loc1)))
    return math.sqrt(squared_diff_sum)
