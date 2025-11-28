"""Tests simples de calcul avec pytest."""


def test_calc_addition():
    """Test que 2 + 4 = 6."""
    output = 2 + 4
    assert output == 6


def test_calc_subtraction():
    """Test que 2 - 4 = -2."""
    output = 2 - 4
    assert output == -2


def test_calc_multiply():
    """Test que 2 * 4 = 8."""
    output = 2 * 4
    assert output == 8


def test_coucou():
    """Test que la chaîne est bien 'hello'."""
    output = "hello"
    assert output == "hello"
