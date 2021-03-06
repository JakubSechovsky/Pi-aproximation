from random import randint

n = 100_000


def monte(n):
    """
    Proměnné x a y jsou souřadnice bodu
    Simuluje vkreslování bodů do kruhu o poloměru 5000
    Pomocí poměru mezi kruhem a čtvercem, kterému je vepsán, počítá pí

    Časová složitost:
        nejlepší = nejhorší = průměrná = O(n)
    """
    n_in_circle = 0

    for _ in range(1, 5):
        for _ in range(n):
            x = randint(0, 10_000)
            y = randint(0, 10_000)
            if ((x - 5_000)**2 + (y - 5_000)**2) <= 25_000_000:
                n_in_circle += 1

    pi_aprox = float(n_in_circle / n)

    return pi_aprox


if __name__ == "__main__":
    print(monte(n))
