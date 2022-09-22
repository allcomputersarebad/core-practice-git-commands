import pytest


def always_returns_true():
    return True and True


def test_always_returns_true():
    assert always_returns_true() == True
