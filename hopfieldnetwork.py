zero = [
  [0, 0, 1, 1, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 1, 0],
  [1, 1, 0, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 0, 0, 0, 0, 1, 1],
  [1, 1, 0, 0, 0, 0, 0, 1, 1],
  [0, 1, 1, 1, 1, 1, 1, 1, 0],
  [0, 0, 1, 1, 1, 1, 1, 0, 0],
]

one = [
  [0, 0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 1, 1, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 1, 1, 1, 0],
  [0, 0, 1, 1, 1, 1, 1, 1, 0],
]

two = [
  [0, 0, 1, 1, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 1, 0],
  [1, 1, 0, 0, 0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0, 1, 1, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0, 0],
  [0, 0, 1, 1, 0, 0, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
]

test = [
  [1, 0, 0, 0, 0, 1, 0, 0, 1],
  [1, 0, 0, 1, 0, 1, 0, 0, 1],
  [1, 1, 1, 1, 0, 1, 0, 0, 1],
  [0, 0, 0, 0, 0, 1, 0, 0, 1],
  [0, 0, 0, 0, 0, 1, 0, 0, 1],
  [0, 0, 0, 0, 0, 1, 0, 0, 1],
  [0, 0, 1, 0, 0, 1, 0, 0, 1],
  [0, 0, 1, 1, 0, 1, 0, 1, 1],
  [0, 0, 1, 1, 0, 1, 0, 1, 1],
]

test2 = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 1, 0, 0, 0, 0, 0, 1, 1],
  [0, 1, 1, 1, 1, 1, 1, 1, 0],
  [0, 0, 1, 1, 1, 1, 1, 0, 0],
]

test3 = [
  [0, 0, 1, 1, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 1, 0],
  [1, 1, 0, 0, 0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0, 1, 1, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0, 0],
  [0, 0, 1, 1, 0, 0, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
]

def flatten(M):
  m = []
  for row in M:
    for x in row:
      m.append(x)
  return m

def outer_prod(A, B):
  result = []
  a = flatten(A)
  b = flatten(B)

  for ai in a:
    row = []
    for bj in b:
      row.append(ai * bj)
    result.append(row)

  return result

def print_matrix(m):
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == 1:
        print("# ", end="")
      else:
        print(". ", end="")
    print()

def turn_bipolar(x: list):
  m = []
  for i in range(len(x)):
    row = []
    for j in range(len(x[i])):
      curr = 1
      if x[i][j] == 0:
        curr = -1
      row.append(curr)
    m.append(row)
  return m

def train(patterns):
  n = len(flatten(patterns[0]))
  W = []
  for i in range(n):
    W.append([0] * n)

  for p in patterns:
    bp = turn_bipolar(p)
    op = outer_prod(bp, bp)
    for i in range(n):
      for j in range(n):
        if i != j:
          W[i][j] += op[i][j]
  return W

def recall(W, probe):
  s = flatten(turn_bipolar(probe))
  changed = True
  while changed:
    changed = False
    for i in range(len(s)):
      h = 0
      for j in range(len(s)):
        h += W[i][j] * s[j]
      new = s[i]
      if h > 0:
        new = 1
      elif h < 0:
        new = -1
      if new != s[i]:
        s[i] = new
        changed = True
  return s

def to_matrix(v):
  m = []
  for i in range(0, len(v), 9):
    row = []
    for j in range(i, i + 9):
      if v[j] == 1:
        row.append(1)
      else:
        row.append(0)
    m.append(row)
  return m


W = train([zero, one, two])

print("Inputs:")
print_matrix(zero)
print_matrix(one)
print_matrix(two)

print("Caso 1:")
print("Input:")
print_matrix(test)

print("\nOutput:")
print_matrix(to_matrix(recall(W, test)))

print("Caso 2:")
print("Input:")
print_matrix(test2)

print("\nOutput:")
print_matrix(to_matrix(recall(W, test2)))
print("El input contiene un patron que tiene similitud a los inputs zero y two. Ambos patrones se solapan en W (crosstalk), así que la red converge a una mezcla de los dos en vez de un patron definido.")

print("Caso 3:")
print("Input:")
print_matrix(test3)

print("\nOutput:")
print_matrix(to_matrix(recall(W, test3)))