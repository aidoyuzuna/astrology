from enum import Enum
from sign import Sign


class Planet(Enum):
    Sun = (0, "太陽")
    Moon = (1, "月")
    Mercury = (2, "水星")
    Venus = (3, "金星")
    Mars = (4, "火星")
    Jupiter = (5, "木星")
    Saturn = (6, "土星")
    Uranus = (7, "天王星")
    Neptune = (8, "海王星")
    Pluto = (9, "冥王星")

    def __init__(self, idx, jap):
        self.index = idx
        self.japanese = jap


def find_planet_sign(idx: int, degree: float):
    planet_data: int = 0
    sign_data: str = ""
    planet_sign: Sign = Sign.find_sign_from_degree(degree)
    for p in Planet:
        if p.value[0] == idx:
            planet_data = p.japanese

    for s in Sign:
        if s == planet_sign:
            sign_data = s.japanese
    return planet_data, sign_data


def main():
    planet = 4
    degree = 158.2859
    print(find_planet_sign(planet, degree))


if __name__ == '__main__':
    main()
