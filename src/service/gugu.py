class Gugu:
    def __init__(self, between: tuple[int, int] = (1, 9)):
        self.__between = self._validate_between(between)

    @staticmethod
    def _validate_between(between: tuple[int, int]) -> tuple[int, int]:
        if not isinstance(between, tuple) or len(between) != 2:
            raise ValueError("between은 2개의 정수로 이루어진 튜플이어야 합니다.")
        min_range, max_range = between
        if not all(isinstance(x, int) for x in (min_range, max_range)):
            raise TypeError("between의 각 요소는 정수여야 합니다.")
        if min_range > max_range:
            raise ValueError("between의 첫 번째 값은 두 번째 값보다 작거나 같아야 합니다.")
        return min_range, max_range

    @property
    def between(self) -> tuple[int, int]:
        return self.__between

    def calculate(self, n: int) -> list[tuple[int, int, int]]:
        if not isinstance(n, int):
            raise TypeError("n은 정수여야 합니다.")

        min_range, max_range = self.between
        results: list[tuple[int, int, int]] = []
        for i in range(min_range, max_range + 1):
            results.append((n, i, n * i))
        return results

    @classmethod
    def get_stringified_results(cls, results: list[tuple[int, int, int]]) -> str:
        text = ""
        for op1, op2, result in results:
            text += f"{op1} * {op2} = {result}\n"
        return text.strip()
