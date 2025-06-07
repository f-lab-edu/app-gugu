class Gugu:
    def __init__(self, between: tuple[int, int] = (1, 9)):
        self.__between = between

    @property
    def between(self) -> int:
        return self.__between

    def calculate(self, n: int) -> list[tuple[int, int, int]]:
        min_range, max_range = self.between
        results: list[tuple[int, int, int]] = []
        for i in range(min_range, max_range + 1):
            results.append((n, i, n * i))
        return results

    @classmethod
    def get_stringified_results(cls, results: list[tuple[int, int, int]]) -> None:
        text = ""
        for op1, op2, result in results:
            text += f"{op1} * {op2} = {result}\n"
        return text.strip()
