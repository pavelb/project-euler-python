def minus(P, Q): return P[0] - Q[0], P[1] - Q[1]
def dot(P, Q): return P[0] * Q[0] + P[1] * Q[1]
def areUnique(A, B, C): return not (A == B or B == C or C == A)
def arePerpVectors(D, E, F): return dot(D, E) == 0 or dot(E, F) == 0 or dot(F, D) == 0
def arePerpPoints(A, B, C): return arePerpVectors(minus(A, B), minus(B, C), minus(C, A))

def p91(limit):
	count = 0
	O = [0, 0]
	for x1 in range(limit + 1):
		for x2 in range(limit + 1):
			for y1 in range(limit + 1):
				for y2 in range(limit + 1):
					X = [x1, x2]
					Y = [y1, y2]
					if areUnique(O, X, Y) and arePerpPoints(O, X, Y):
						count += 1
	return count // 2

print(p91(50))
