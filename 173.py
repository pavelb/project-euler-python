def p173(tiles): return sum(tiles / 4 / k - k for k in range(1, int(tiles ** 0.5) / 2))
print(p173(10 ** 6))
