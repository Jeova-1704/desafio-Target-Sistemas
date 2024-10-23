def inverter_string(palavra):
    return palavra[::-1]


def inverter_string_2(palavra):
    invertida = (palavra[i] for i in range(len(palavra) - 1, -1, -1))
    return "".join(invertida)


if __name__ == "__main__":
    palavra = "Python"
    palavra2 = "Python é a melhor linguagem de programação"
    print(inverter_string(palavra))
    print(inverter_string(palavra2))
    print(inverter_string_2(palavra))
    print(inverter_string_2(palavra2))
    