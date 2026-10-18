from minimal import get_feedback, GOALS

def test_get_feedback_all_unmet():
    code = "def binary_gap(n):\n    return 0\n"
    feedback = get_feedback(code, GOALS)
    assert "missing docstring" in feedback
    assert "does not reject negative input" in feedback
    assert "does not handle n == 0" in feedback

def test_get_feedback_missing_docstring():
    code = "def binary_gap(n):\n    if n < 0:\n        raise ValueError()\n    if n == 0:\n        return 0\n    return 0\n"
    feedback = get_feedback(code, GOALS)
    assert feedback == "missing docstring"

def test_get_feedback_missing_negative_input_check():
    code = "def binary_gap(n):\n    \"\"\"Docstring\"\"\"\n    if n == 0:\n        return 0\n    return 0\n"
    feedback = get_feedback(code, GOALS)
    assert feedback == "does not reject negative input"

def test_get_feedback_missing_n_zero_check():
    code = "def binary_gap(n):\n    \"\"\"Docstring\"\"\"\n    if n < 0:\n        raise ValueError()\n    return 0\n"
    feedback = get_feedback(code, GOALS)
    assert feedback == "does not handle n == 0"

def test_get_feedback_all_met():
    code = "def binary_gap(n):\n    \"\"\"Docstring\"\"\"\n    if n < 0:\n        raise ValueError()\n    if n == 0:\n        return 0\n    return 0\n"
    feedback = get_feedback(code, GOALS)
    assert feedback == "all goals satisfied"
