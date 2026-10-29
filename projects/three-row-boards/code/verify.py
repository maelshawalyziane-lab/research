"""Independent check: no three points of S form a right isosceles triangle.
Brute force over all triples; a triple {A,B,C} is right isosceles iff for some
vertex V the two edges from V are perpendicular and of equal length."""
import sys, itertools, ast

def is_right_isosceles(A, B, C):
    for V, P, Q in ((A, B, C), (B, A, C), (C, A, B)):
        u = (P[0]-V[0], P[1]-V[1]); w = (Q[0]-V[0], Q[1]-V[1])
        if u[0]*w[0] + u[1]*w[1] == 0 and u[0]**2 + u[1]**2 == w[0]**2 + w[1]**2 and u != (0,0):
            return True
    return False

def check(n, S):
    assert all(0 <= x < n and 0 <= y < n for x, y in S), "point outside grid"
    assert len(set(S)) == len(S), "duplicate points"
    for A, B, C in itertools.combinations(S, 3):
        if is_right_isosceles(A, B, C):
            return False, (A, B, C)
    return True, None

if __name__ == "__main__":
    n = int(sys.argv[1]); S = ast.literal_eval(open(sys.argv[2]).read().split("\n")[1]) if sys.argv[2].endswith(".txt") else None
    print(n, len(S), check(n, S))
