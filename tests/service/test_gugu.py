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
