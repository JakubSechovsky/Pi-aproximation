import MonteCarloPi as mcp

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

print("Pí je přibližně 3.14159\n\nAproximace pí při:\n")

for n in n_list:
    if n <= 5_000:
        print(f"\t {n} pokusech:\t\t{mcp.monte(n)}")
    else:
        print(f"\t {n} pokusech:\t{mcp.monte(n)}")
