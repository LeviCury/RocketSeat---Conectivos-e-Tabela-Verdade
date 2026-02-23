# Conectivos Lógicos e Tabelas Verdade

**Aluno:** Levi Cury  
**Instituição:** Faculdade de Tecnologia Rocketseat  
**Disciplina:** Lógica de Programação  
**Data:** Fevereiro/2026

---

## Sobre o Projeto

Resolução dos 10 exercícios práticos de lógica proposicional propostos pela Rocketseat. O programa identifica os conectivos lógicos de cada frase, define as proposições, monta a expressão formal e gera a tabela verdade correspondente com todas as combinações possíveis de V (verdadeiro) e F (falso).

## Conectivos Utilizados

| Conectivo | Símbolo | Regra |
|-----------|---------|-------|
| **E** (conjunção) | `^` | V apenas se **ambas** forem V |
| **OU** (disjunção) | `v` | V se **pelo menos uma** for V |
| **SE...ENTÃO** (condicional) | `->` | F **somente** quando p=V e q=F |
| **SE E SOMENTE SE** (bicondicional) | `<->` | V quando ambas têm o **mesmo valor** |

## Exercícios

| # | Frase | Conectivo | Expressão |
|---|-------|-----------|-----------|
| 1 | Eu estudei para a prova **e** fiz todos os exercícios | E | `p ^ q` |
| 2 | Eu vou ao cinema **ou** fico em casa assistindo séries | OU | `p v q` |
| 3 | **Se** eu acordar cedo, **então** conseguirei pegar o ônibus | SE...ENTÃO | `p -> q` |
| 4 | **Se** eu estudar muito, **então** passarei na prova **e** ganharei um presente | SE...ENTÃO + E | `p -> (q ^ r)` |
| 5 | Eu vou jogar videogame **ou** vou estudar lógica de programação | OU | `p v q` |
| 6 | Eu comi pizza **e** tomei refrigerante | E | `p ^ q` |
| 7 | **Se** eu tiver dinheiro, **então** viajarei nas férias | SE...ENTÃO | `p -> q` |
| 8 | Eu lerei um livro **se e somente se** terminar meu trabalho | SE E SOMENTE SE | `p <-> q` |
| 9 | **Se** estiver sol, **então** irei à praia **ou** ao parque | SE...ENTÃO + OU | `p -> (q v r)` |
| 10 | Eu farei um bolo **se e somente se** comprar os ingredientes | SE E SOMENTE SE | `p <-> q` |

## Como Executar

**Pré-requisito:** Python 3.6+

```bash
python tabelas_verdade.py
```

## Exemplo de Saída

```
+------------------------------------------------------------+
|     DESAFIO: CONECTIVOS LOGICOS E TABELAS VERDADE           |
+------------------------------------------------------------+
|  Aluno:        Levi Cury                                     |
|  Instituicao:  Faculdade de Tecnologia Rocketseat            |
|  Disciplina:   Logica de Programacao                         |
+------------------------------------------------------------+

==============================================================
  Exercicio 1
==============================================================
  Frase: "Eu estudei para a prova E fiz todos os exercicios."
  Conectivo(s): E (^)
  p: Eu estudei para a prova
  q: Fiz todos os exercicios
  Expressao: p ^ q

|     p      |     q      |   p ^ q    |
|------------|------------|------------|
|     V      |     V      |     V      |
|     V      |     F      |     F      |
|     F      |     V      |     F      |
|     F      |     F      |     F      |
```

## Estrutura

```
logica-proposicional/
├── README.md
└── tabelas_verdade.py
```

## Tecnologias

- **Python 3** — sem dependências externas, usa apenas a biblioteca padrão (`itertools`)

---

> Atividade prática da Faculdade de Tecnologia Rocketseat — Lógica de Programação.
