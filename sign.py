from enum import Enum


class Sign(Enum):
    Aries = (0, "牡羊座")
    Taurus = (1, "牡牛座")
    Gemini = (2, "双子座")
    Cancer = (3, "蟹座")
    Leo = (4, "獅子座")
    Virgo = (5, "乙女座")
    Libra = (6, "天秤座")
    Scorpio = (7, "蠍座")
    Sagittarius = (8, "射手座")
    Capricorn = (9, "山羊座")
    Aquarius = (10, "水瓶座")
    Pisces = (11, "魚座")

    def __init__(self, idx, jap):
        self.index = idx
        self.japanese = jap

    @classmethod
    def find_sign(cls, idx: int) -> 'Sign':
        for sign in cls:
            if sign.value[0] == idx:
                return sign
        raise ValueError(f"Invalid index: {idx}")

    @classmethod
    def find_sign_from_degree(cls, degree: float) -> 'Sign':
        idx = calc_degree(degree)
        return cls.find_sign(idx)


class Modalities(Enum):
    Cardinal = (0, "活動宮")
    Fixed = (1, "不動宮")
    Mutable = (2, "柔軟宮")

    def __init__(self, idx, modal):
        self.index = idx
        self.modal = modal


class Elements(Enum):
    Fire = (0, "火")
    Earth = (1, "土")
    Air = (2, "風")
    Water = (3, "水")

    def __init__(self, idx, elm):
        self.index = idx
        self.elm = elm


def calc_degree(degree: float):
    idx = int(degree / 30)
    return idx


def find_modalities_from_degree(degree: float):
    idx = calc_degree(degree) % 3
    for modalities in Modalities:
        if modalities.value[0] == idx:
            return modalities
    raise ValueError(f"Invalid index: {idx}")


def find_element_from_degree(degree: float):
    idx = calc_degree(degree) % 4
    for element in Elements:
        if element.value[0] == idx:
            return element
    raise ValueError(f"Invalid index: {idx}")


def main():
    degree = 158.2859
    sign = Sign.find_sign_from_degree(degree)
    modalities = find_modalities_from_degree(degree)
    elements = find_element_from_degree(degree)
    print(sign.japanese, modalities.modal, elements.elm)


if __name__ == '__main__':
    main()
