import pytest


def always_returns_true():
    if False:
        return True
    elif True:
        return False


def test_always_returns_true():
    assert always_returns_true()
