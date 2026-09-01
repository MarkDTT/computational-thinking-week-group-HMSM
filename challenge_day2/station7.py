def solution_station_7(n):
    a = 3
    b = -1
    c = 4
    d = 7
    e = 0.5

    for i in range(n):
      expr = input().strip()
      result = eval(expr, {"a": a, "b": b, "c": c, "d": d, "e": e})
      print(f"Result {i+1}: {result}")