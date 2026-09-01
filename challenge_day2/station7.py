def solution_station_7(n):
    values = {"a": 3, "b": -1, "c": 4, "d": 7, "e": 0.5}

    def calculate(expr):
        terms = expr.replace(" ", "").split("+")
        total = 0
        for term in terms:
            factors = term.split("*")
            product = 1
            for f in factors:
                product *= values[f]
            total += product
        return total

    for i in range(n):
        expr = input().strip()
        result = calculate(expr)
        print(f"Result {i+1}: {result}")