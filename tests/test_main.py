from unittest.mock import MagicMock, patch

from fastapi.testclient import TestClient


def test_health(mock_client: TestClient) -> None:
    # Given
    pass

    # When
    res = mock_client.get("/health")

    # Then
    assert res.status_code == 200
    assert res.json() == {"status": "ok", "is_error": False, "result": None}


def test_gugu_with_valid_numbers(mock_client: TestClient) -> None:
    # Given
    expected_gugu_calculate_results = (
        (3, 1, 3),
        (3, 2, 6),
        (3, 3, 9),
        (3, 4, 12),
        (3, 5, 15),
        (3, 6, 18),
        (3, 7, 21),
        (3, 8, 24),
        (3, 9, 27),
    )
    expected_gugu_calculate_stringified_result = "'3 * 1 = 3\n3 * 2 = 6\n3 * 3 = 9\n3 * 4 = 12\n3 * 5 = 15\n3 * 6 = 18\n3 * 7 = 21\n3 * 8 = 24\n3 * 9 = 27"

    mock_gugu_calculate = MagicMock(return_value=expected_gugu_calculate_results)
    mock_gugu = MagicMock()
    mock_gugu_get_stringified_results = MagicMock(return_value=expected_gugu_calculate_stringified_result)
    mock_gugu.calculate = mock_gugu_calculate

    with patch("main.Gugu", return_value=mock_gugu) as patched_gugu:
        # Given
        patched_gugu.get_stringified_results = mock_gugu_get_stringified_results

        # When
        res = mock_client.post("/gugu", json={"n": 3})
        print(res.json())

        # Then
        expected_json_output = {
            "status": "ok",
            "is_error": False,
            "result": expected_gugu_calculate_stringified_result,
        }

        patched_gugu.assert_called_once()
        mock_gugu_calculate.assert_called_once_with(3)
        mock_gugu_get_stringified_results.assert_called_once_with(expected_gugu_calculate_results)

        assert res.status_code == 200
        assert res.json() == expected_json_output
