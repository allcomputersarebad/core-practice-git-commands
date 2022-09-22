import pytest


def always_returns_true():
    return not False


def test_always_returns_true():
    assert always_returns_true()
