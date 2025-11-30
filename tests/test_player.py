import pygame
import pytest

from player import ScriptedPlayer


@pytest.fixture(scope="module", autouse=True)
def init_pygame():
    pygame.init()
    yield
    pygame.quit()


def test_scripted_player_advances_when_move_allowed():
    player = ScriptedPlayer(0, 0, 0, 0, move_script=[3, 2])

    changed = player.consume_scripted_move([0, 0, 1, 1])

    assert changed is True
    assert player.control == 3
    assert player.direction == 3

    changed = player.consume_scripted_move([0, 0, 1, 1])

    assert changed is True
    assert player.direction == 2


def test_scripted_player_waits_until_path_opens():
    player = ScriptedPlayer(0, 0, 0, 0, move_script=[0, 3])
    player.direction = 3

    changed = player.consume_scripted_move([0, 1, 1, 1])

    assert changed is False
    assert player.direction == 3
    assert player.control == 4

    changed = player.consume_scripted_move([1, 1, 1, 1])

    assert changed is True
    assert player.direction == 0


def test_scripted_player_repeats_script_when_looping():
    player = ScriptedPlayer(0, 0, 0, 0, move_script=[2], loop_script=True)

    assert player.consume_scripted_move([1, 1, 1, 1]) is True
    assert player.direction == 2

    assert player.consume_scripted_move([1, 1, 1, 1]) is True
    assert player.direction == 2
