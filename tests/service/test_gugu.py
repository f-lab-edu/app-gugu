import pytest

from service.gugu import Gugu


def test_calculate_with_default_range():
    gugu = Gugu()
    result = gugu.calculate(2)
    expected = [(2, i, 2 * i) for i in range(1, 10)]
    assert result == expected


def test_calculate_with_custom_range():
    gugu = Gugu((3, 5))
    result = gugu.calculate(2)
    expected = [(2, i, 2 * i) for i in range(3, 6)]
    assert result == expected


def test_stringified_results_format():
    results = [(2, 1, 2), (2, 2, 4), (2, 3, 6)]
    output = Gugu.get_stringified_results(results)
    expected = "2 * 1 = 2\n2 * 2 = 4\n2 * 3 = 6"
    assert output == expected


def test_between_property():
    gugu = Gugu((4, 7))
    assert gugu.between == (4, 7)


def test_valid_between():
    result = Gugu._validate_between((1, 9))
    assert result == (1, 9)


def test_not_a_tuple():
    with pytest.raises(
        ValueError, match="between은 2개의 정수로 이루어진 튜플이어야 합니다."
    ):
        Gugu([1, 9])


def test_tuple_length_not_two():
    with pytest.raises(
        ValueError, match="between은 2개의 정수로 이루어진 튜플이어야 합니다."
    ):
        Gugu((1,))  # 요소가 하나만 있음


def test_non_integer_elements():
    with pytest.raises(TypeError, match="between의 각 요소는 정수여야 합니다."):
        Gugu((1, "a"))


def test_first_greater_than_second():
    with pytest.raises(
        ValueError, match="between의 첫 번째 값은 두 번째 값보다 작거나 같아야 합니다."
    ):
        Gugu((5, 2))


@pytest.mark.parametrize(
    "invalid_input",
    [
        "2",
        2.0,
        None,
        [2],
        {"n": 2},
    ],
)
def test_invalid_non_integer_input(invalid_input):
    gugu = Gugu((1, 3))
    with pytest.raises(TypeError, match="n은 정수여야 합니다."):
        gugu.calculate(invalid_input)
