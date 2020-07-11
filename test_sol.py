import os
import pytest
from sol import show_excitement

result = "Hello World"

@pytest.mark.parametrize('x,result', [(2, result)])
def test_maxblock(x, result):
  assert show_excitement() == result
