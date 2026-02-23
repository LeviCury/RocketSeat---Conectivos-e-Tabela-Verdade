"""
==========================================================
  Desafio: Conectivos Logicos e Tabelas Verdade
==========================================================
  Aluno:        Levi Cury
  Instituicao:  Faculdade de Tecnologia Rocketseat
  Disciplina:   Logica de Programacao
  Atividade:    Exercicios praticos - Conectivos Logicos
                e Tabelas Verdade
  Data:         Fevereiro/2026
==========================================================
"""

from itertools import product


def conjuncao(p, q):
    return p and q


def disjuncao(p, q):
    return p or q


def condicional(p, q):
    return (not p) or q


def bicondicional(p, q):
    return p == q


def vf(valor):
    return "V" if valor else "F"


def linha_tabela(valores, resultado, largura=12):
    colunas = [f"{vf(v):^{largura}}" for v in valores]
    colunas.append(f"{vf(resultado):^{largura}}")
    return "|" + "|".join(colunas) + "|"


def separador(n_colunas, largura=12):
    return "|" + "|".join(["-" * largura] * n_colunas) + "|"


def cabecalho(nomes, largura=12):
    colunas = [f"{n:^{largura}}" for n in nomes]
    return "|" + "|".join(colunas) + "|"


def titulo_exercicio(numero, frase, conectivo, props, expressao):
    print(f"\n{'='*62}")
    print(f"  Exercicio {numero}")
    print(f"{'='*62}")
    print(f'  Frase: "{frase}"')
    print(f"  Conectivo(s): {conectivo}")
    for nome, desc in props.items():
        print(f"  {nome}: {desc}")
    print(f"  Expressao: {expressao}")
    print()


def exercicio_simples(numero, frase, conectivo, prop_p, prop_q, expressao, operacao):
    titulo_exercicio(
        numero, frase, conectivo,
        {"p": prop_p, "q": prop_q},
        expressao,
    )
    print(cabecalho(["p", "q", expressao]))
    print(separador(3))
    for p, q in product([True, False], repeat=2):
        print(linha_tabela([p, q], operacao(p, q)))


def exercicio_1():
    exercicio_simples(
        1,
        "Eu estudei para a prova E fiz todos os exercicios.",
        "E (^)", "Eu estudei para a prova", "Fiz todos os exercicios",
        "p ^ q", conjuncao,
    )


def exercicio_2():
    exercicio_simples(
        2,
        "Eu vou ao cinema OU fico em casa assistindo series.",
        "OU (v)", "Eu vou ao cinema", "Fico em casa assistindo series",
        "p v q", disjuncao,
    )


def exercicio_3():
    exercicio_simples(
        3,
        "SE eu acordar cedo, ENTAO conseguirei pegar o onibus.",
        "SE...ENTAO (->)", "Acordar cedo", "Conseguirei pegar o onibus",
        "p -> q", condicional,
    )


def exercicio_4():
    titulo_exercicio(
        4,
        "SE eu estudar muito, ENTAO passarei na prova E ganharei um presente.",
        "SE...ENTAO (->) e E (^)",
        {"p": "Estudar muito", "q": "Passarei na prova", "r": "Ganharei um presente"},
        "p -> (q ^ r)",
    )
    print(cabecalho(["p", "q", "r", "q ^ r", "p->(q^r)"]))
    print(separador(5))
    for p, q, r in product([True, False], repeat=3):
        q_e_r = conjuncao(q, r)
        resultado = condicional(p, q_e_r)
        colunas = [f"{vf(v):^12}" for v in [p, q, r, q_e_r]]
        colunas.append(f"{vf(resultado):^12}")
        print("|" + "|".join(colunas) + "|")


def exercicio_5():
    exercicio_simples(
        5,
        "Eu vou jogar videogame OU vou estudar logica de programacao.",
        "OU (v)", "Jogar videogame", "Estudar logica de programacao",
        "p v q", disjuncao,
    )


def exercicio_6():
    exercicio_simples(
        6,
        "Eu comi pizza E tomei refrigerante.",
        "E (^)", "Comi pizza", "Tomei refrigerante",
        "p ^ q", conjuncao,
    )


def exercicio_7():
    exercicio_simples(
        7,
        "SE eu tiver dinheiro, ENTAO viajarei nas ferias.",
        "SE...ENTAO (->)", "Eu tiver dinheiro", "Viajarei nas ferias",
        "p -> q", condicional,
    )


def exercicio_8():
    exercicio_simples(
        8,
        "Eu lerei um livro SE E SOMENTE SE terminar meu trabalho.",
        "SE E SOMENTE SE (<->)", "Eu lerei o livro", "Terminar meu trabalho",
        "p <-> q", bicondicional,
    )


def exercicio_9():
    titulo_exercicio(
        9,
        "SE estiver sol, ENTAO irei a praia OU ao parque.",
        "SE...ENTAO (->) e OU (v)",
        {"p": "Estiver sol", "q": "Irei a praia", "r": "Irei ao parque"},
        "p -> (q v r)",
    )
    print(cabecalho(["p", "q", "r", "q v r", "p->(qvr)"]))
    print(separador(5))
    for p, q, r in product([True, False], repeat=3):
        q_ou_r = disjuncao(q, r)
        resultado = condicional(p, q_ou_r)
        colunas = [f"{vf(v):^12}" for v in [p, q, r, q_ou_r]]
        colunas.append(f"{vf(resultado):^12}")
        print("|" + "|".join(colunas) + "|")


def exercicio_10():
    exercicio_simples(
        10,
        "Eu farei um bolo SE E SOMENTE SE comprar os ingredientes.",
        "SE E SOMENTE SE (<->)", "Eu farei o bolo", "Comprar os ingredientes",
        "p <-> q", bicondicional,
    )


def main():
    print("+------------------------------------------------------------+")
    print("|     DESAFIO: CONECTIVOS LOGICOS E TABELAS VERDADE           |")
    print("+------------------------------------------------------------+")
    print("|  Aluno:        Levi Cury                                     |")
    print("|  Instituicao:  Faculdade de Tecnologia Rocketseat            |")
    print("|  Disciplina:   Logica de Programacao                         |")
    print("|  Data:         Fevereiro/2026                                |")
    print("+------------------------------------------------------------+")
    print("|  Regras dos conectivos:                                      |")
    print("|  ^ (E)            - V apenas se ambas forem V               |")
    print("|  v (OU)           - V se pelo menos uma for V               |")
    print("|  -> (SE...ENTAO)  - F apenas quando p=V e q=F               |")
    print("|  <-> (SE E S.SE)  - V quando ambas tem o mesmo valor        |")
    print("+------------------------------------------------------------+")

    exercicios = [
        exercicio_1, exercicio_2, exercicio_3, exercicio_4, exercicio_5,
        exercicio_6, exercicio_7, exercicio_8, exercicio_9, exercicio_10,
    ]

    for ex in exercicios:
        ex()

    print(f"\n{'='*62}")
    print("  Todos os 10 exercicios resolvidos com sucesso!")
    print("  Atividade concluida por Levi Cury - Rocketseat")
    print(f"{'='*62}\n")


if __name__ == "__main__":
    main()
