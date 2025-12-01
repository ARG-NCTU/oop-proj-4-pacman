import os

import pygame
import pytest

from ghost import ScriptedGhost


@pytest.fixture(autouse=True)
def stub_pygame_surfaces(monkeypatch):
    """Avoid loading actual assets during unit tests."""
    os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
    pygame.init()
    pygame.display.set_mode((1, 1))
    surface = pygame.Surface((10, 10), pygame.SRCALPHA)

    def fake_load(_):
        return surface.copy()

    def fake_scale(_, size):
        return pygame.Surface(size, pygame.SRCALPHA)

    monkeypatch.setattr(pygame.image, "load", fake_load)
    monkeypatch.setattr(pygame.transform, "scale", fake_scale)
    yield
    pygame.display.quit()
    pygame.quit()


def test_scripted_ghost_consumes_moves_when_available():
    ghost = ScriptedGhost("pink", 0, 0, 0, 0, move_script=[0, 3])

    ghost.set_dir(next_step=2, canMove=[1, 1, 1, 1])
    assert (ghost.dx, ghost.dy) == (0, -2)

    ghost.set_dir(next_step=0, canMove=[1, 1, 1, 1])
    assert (ghost.dx, ghost.dy) == (2, 0)


def test_scripted_ghost_falls_back_to_algorithm_when_blocked():
    ghost = ScriptedGhost("pink", 0, 0, 0, 0, move_script=[2], algorithm="bfs")

    ghost.set_dir(next_step=0, canMove=[1, 1, 0, 1])

    assert (ghost.dx, ghost.dy) == (0, -2)
    assert ghost._script_index == 0


def test_scripted_ghost_can_loop_script():
    ghost = ScriptedGhost("pink", 0, 0, 0, 0, move_script=[1], loop_script=True)

    ghost.set_dir(next_step=2, canMove=[1, 1, 1, 1])
    first_move = (ghost.dx, ghost.dy)

    ghost.set_dir(next_step=2, canMove=[1, 1, 1, 1])
    second_move = (ghost.dx, ghost.dy)

    assert first_move == (0, 2)
    assert second_move == first_move
