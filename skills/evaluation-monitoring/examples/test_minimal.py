import sys
from pathlib import Path
import pytest

# Add the examples directory to sys.path to allow importing minimal.py
sys.path.insert(0, str(Path(__file__).parent))

from minimal import trajectory_score

def test_trajectory_score_exact_match():
    actual = ["search", "answer"]
    expected = ["search", "answer"]
    result = trajectory_score(actual, expected)
    assert result == {"in_order": True, "tool_precision": 1.0}

def test_trajectory_score_out_of_order():
    actual = ["answer", "search"]
    expected = ["search", "answer"]
    result = trajectory_score(actual, expected)
    assert result == {"in_order": False, "tool_precision": 1.0}

def test_trajectory_score_partial_match():
    actual = ["search", "calc"]
    expected = ["search", "answer"]
    result = trajectory_score(actual, expected)
    assert result == {"in_order": False, "tool_precision": 0.5}

def test_trajectory_score_no_match():
    actual = ["calc", "summarize"]
    expected = ["search", "answer"]
    result = trajectory_score(actual, expected)
    assert result == {"in_order": False, "tool_precision": 0.0}

def test_trajectory_score_empty_lists():
    actual = []
    expected = []
    result = trajectory_score(actual, expected)
    assert result == {"in_order": True, "tool_precision": 0.0}

def test_trajectory_score_empty_expected():
    actual = ["search"]
    expected = []
    result = trajectory_score(actual, expected)
    assert result == {"in_order": False, "tool_precision": 0.0}

def test_trajectory_score_empty_actual():
    actual = []
    expected = ["search"]
    result = trajectory_score(actual, expected)
    assert result == {"in_order": False, "tool_precision": 0.0}

def test_trajectory_score_duplicates_in_actual():
    actual = ["search", "search", "answer"]
    expected = ["search", "answer"]
    result = trajectory_score(actual, expected)
    assert result == {"in_order": False, "tool_precision": 0.67}

def test_trajectory_score_duplicates_in_expected():
    actual = ["search", "answer"]
    expected = ["search", "search", "answer"]
    result = trajectory_score(actual, expected)
    assert result == {"in_order": False, "tool_precision": 1.0}
