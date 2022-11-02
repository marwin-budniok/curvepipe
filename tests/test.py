import pytest

from src.curvepipe import CurvePipe


def test_create_curvepipe_instance():
    curvepipe = CurvePipe(x=[0, 1, 2], y=[2, 2, 5])
    assert type(curvepipe) == CurvePipe


def test_scale_x():
    curvepipe = CurvePipe(x=[0, 1, 2], y=[2, 2, 5])
    curvepipe.scale_x(0.5)
    assert curvepipe.get_x() == [0, 0.5, 1]


def test_offset_x():
    curvepipe = CurvePipe(x=[0, 1, 2], y=[2, 2, 5])
    curvepipe.offset_x(0.1)
    assert curvepipe.get_x() == [0.1, 1.1, 2.1]


def test_transform_x():
    curvepipe = CurvePipe(x=[0, 2, 3], y=[2, 2, 5])
    curvepipe.transform_x(lambda x: x ** 2)
    assert curvepipe.get_x() == [0, 4, 9]


def test_scale_y():
    curvepipe = CurvePipe(x=[0, 1, 2], y=[2, 2, 5])
    curvepipe.scale_y(3)
    assert curvepipe.get_y() == [6, 6, 15]


def test_offset_y():
    curvepipe = CurvePipe(x=[0, 1, 2], y=[2, 2, 5])
    curvepipe.offset_y(0.2)
    assert curvepipe.get_y() == [2.2, 2.2, 5.2]


def test_transform_y():
    curvepipe = CurvePipe(x=[0, 2, 3], y=[4, 9, 5])
    curvepipe.transform_y(lambda y: y - 0.5)
    assert curvepipe.get_y() == [3.5, 8.5, 4.5]


def test_scale_offset_and_transform():
    curvepipe = CurvePipe(x=[0, 1, 2, 3, 4], y=[4, 9, 5, 5, 6]) \
        .scale_x(2) \
        .transform_x(lambda e: e + 0.1) \
        .offset_x(20.1)
    assert curvepipe.get_x() == [20.2, 22.2, 24.2, 26.2, 28.2]

