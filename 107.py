def getMatrix(filename):
	rv = []
	with open(filename, 'r') as file:
		for line in file:
			line = line.strip()
			cleanLine = []
			for n in line.split(','):
				cleanLine.append(float('inf') if n == '-' else int(n))
			rv.append(cleanLine)
	return rv


def extractMin(Q):
	# @TODO: improve by writing a binary min heap with decreaseKey
	Q.sort(key=lambda u: u.key)
	return Q.pop(0)


def mstPrim(G, w, r):
	for u in G.V:
		u.key = float('inf')
		u.p = None
	r.key = 0
	Q = list(G.V)
	while Q:
		u = extractMin(Q)
		for v in G.adj(u):
			if v in Q and w(u, v) < v.key:
				v.p = u
				v.key = w(u, v)


def printMatrix(matrix):
	for row in matrix:
		for n in row:
			print('%s\t' % n, end='')
		print()
	print()


class GraphNode(object):
	def __init__(self, v):
		self.v = v
		self.key = float('inf')
		self.p = None

	def __str__(self):
		return '<GraphNode %s %s %s>' % (
			self.v,
			self.key,
			self.p.v if self.p else None
		)


class Graph(object):
	def __init__(self, M):
		self.M = M
		self.V = list(map(GraphNode, range(len(M))))

	def adj(self, u):
		for n, v in enumerate(self.M[u.v]):
			if v < float('inf'):
				yield self.V[n]


def main(filename):
	matrix = getMatrix(filename)
	g = Graph(matrix)
	w = lambda u, v: matrix[u.v][v.v]
	mstPrim(g, w, GraphNode(0))
	preWeight = sum(n for row in matrix for n in row if n < float('inf')) // 2
	postWeight = sum(v.key for v in g.V if v.key < float('inf'))
	return preWeight - postWeight

if __name__ == '__main__':
	print(main('107.txt'))  # 259679
