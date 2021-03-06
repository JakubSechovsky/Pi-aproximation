import MonteCarloPi as mcp
from timeit import repeat

n_list = [
    10,
    50,
    100,
    500,
    1_000,
    5_000,
    10_000,
    50_000,
    100_000,
    500_000,
]

print("Testuji...")

for n in n_list:
    time = min(repeat("mcp.monte(n)", number=1, repeat=5, globals=globals()))
    print(f"Při {n} opakováních je čas:\t{time: .7f}s")

print("Testování ukončeno.")
