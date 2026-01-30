def add_strints(x: str, y: str) -> str:
    """
    Add two nonnegative integer strings by converting to int.
    This method can be rewritten as a sum/carry adder for a
    single digit addition, pulling characters from the
    input strings. For simplicity now, we just convert the
    whole string to integer, do the addition, and then
    convert the number back to string.
    """
    return str(int(x) + int(y))

def simple_recursive_multiplication(x: str, y: str) -> str:
    """
    Recursive multiplication for nonnegative integer strings.
    Assumptions:
      - len(x) == len(y)
      - len(x) is a power of two
      - x and y contain only digits
    Uses:
      xy = ac*10^n + (ad+bc)*10^(n/2) + bd
    """
    # Number of digits in x, y
    n = len(x)
    # Base case
    if n == 1:
        return str(int(x) * int(y))
    # Middle of x, y for splitting them in left/right halves
    m = n // 2
    # Divide x, y into left/right halves
    a = x[:m]
    b = x[m:]
    c = y[:m]
    d = y[m:]
    # Compute the partial solution
    ac = simple_recursive_multiplication(a, c)
    ad = simple_recursive_multiplication(a, d)
    bc = simple_recursive_multiplication(b, c)
    bd = simple_recursive_multiplication(b, d)
    # Conquer the partial solutions
    ad_plus_bc = add_strints(ad, bc)
    # Multiply by powers of 10 via appending zeros (string shift).
    term1 = ac + ("0" * n)
    term2 = ad_plus_bc + ("0" * m)
    # Final sum (Using int conversion for addition to keep things simple)
    return str(int(term1) + int(term2) + int(bd))

def next_power_of_two(n: int) -> int:
    p = 1
    while p < n:
        p *= 2
    return p


def karatsuba_multiplication(x: str, y: str) -> str:
    """
    Karatsuba multiplication for nonnegative integer strings.
    """

    n = max(len(x), len(y))
    n2 = next_power_of_two(n)
    x = x.zfill(n2)
    y = y.zfill(n2)

    def karat(a: str, b: str) -> str:
        n = len(a)
        if n == 1:
            return str(int(a) * int(b))

        m = n // 2
        a1, a0 = a[:m], a[m:]
        b1, b0 = b[:m], b[m:]

        ac = karat(a1, b1)
        bd = karat(a0, b0)

        s1 = str(int(a1) + int(a0))
        s2 = str(int(b1) + int(b0))

        k = max(len(s1), len(s2))
        k2 = next_power_of_two(k)
        s1 = s1.zfill(k2)
        s2 = s2.zfill(k2)

        ab_cd = karat(s1, s2)

        ad_plus_bc = str(int(ab_cd) - int(ac) - int(bd))

        term1 = ac + ("0" * n)
        term2 = ad_plus_bc + ("0" * m)
        res = str(int(term1) + int(term2) + int(bd))

        return res

    return str(int(karat(x, y)))

tests = [
    ("12", "34"),
    ("99", "99"),
    ("0123", "0456"),
    ("1234", "5678"),
    ("0000", "0000"),
    ("1111", "0001"),
    ("1234567890123456", "9876543210123456"),
    ("12345678901234561234567890123456", "12345678901234561234567890123456"),
    ("1234567890123456123456789012345612345678901234561234567890123456",
     "1234567890123456123456789012345612345678901234561234567890123456"),
]

for x, y in tests:
    got = karatsuba_multiplication(x, y)
    want = str(int(x) * int(y))
    print(f"{x} * {y} = {got}  (ok={got == want})")
    
import time

print("--------------------TIME--------------------")
print("")

def next_pow2_str(s: str) -> str:
    n2 = next_power_of_two(len(s))
    return s.zfill(n2)

def make_number(n: int) -> str:
    out = ""
    for i in range(n):
        if i == 0:
            out += "1"
        else:
            out += str((7 * i) % 10)
    return out


sizes = [8, 16, 32, 64, 128, 256]

print("digits | simple_time | karatsuba_time ")
for n in sizes:
    x = make_number(n)
    y = make_number(n)

    xs = next_pow2_str(x)
    ys = next_pow2_str(y)

    # time simple
    t0 = time.time()
    simple_recursive_multiplication(xs, ys)
    t1 = time.time()

    # time karatsuba
    t2 = time.time()
    karatsuba_multiplication(x, y)
    t3 = time.time()

    print(f"{n:5d} | {t1 - t0:.6f}  | {t3 - t2:.6f}")

