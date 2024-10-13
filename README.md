# Calculadora de Salário

Este projeto implementa uma calculadora de salário para funcionários com diferentes cargos e regras de desconto. O sistema foi desenvolvido utilizando a técnica de Test Driven Development (TDD) em Python, com testes automatizados usando o framework `unittest`.

## Estrutura do Projeto

```
Exercícios Práticos de TDD 2 - Ryan Alves/
│
├── src/
│   ├── __init__.py
│   ├── employee.py
│   └── salary_calculator.py
│
└── tests/
│   ├── __init__.py
│   └── test_salary_calculator.py
│
└── README.md
│
└──requirements.txt
```

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/RyanAlvesQ/ExercicioPraticoTDD.git
   cd https://github.com/RyanAlvesQ/ExercicioPraticoTDD.git
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Para executar os testes, utilize o comando:
   ```bash
   pytest
   ```

5. Como gerar relatório de cobertura de testes:
   Se quiser verificar a cobertura de código, utilize o `coverage`:
   ```bash
   coverage run -m unittest discover -s tests
   coverage report -m
   ```

## Regras de Cálculo

As regras para o cálculo do salário líquido são as seguintes:

- **DESENVOLVEDOR**:
  - 20% de desconto se o salário for maior ou igual a R$ 3.000,00.
  - 10% de desconto se o salário for menor que R$ 3.000,00.

- **DBA**:
  - 25% de desconto se o salário for maior ou igual a R$ 2.000,00.
  - 15% de desconto se o salário for menor que R$ 2.000,00.

- **TESTADOR**:
  - 25% de desconto se o salário for maior ou igual a R$ 2.000,00.
  - 15% de desconto se o salário for menor que R$ 2.000,00.

- **GERENTE**:
  - 30% de desconto se o salário for maior ou igual a R$ 5.000,00.
  - 20% de desconto se o salário for menor que R$ 5.000,00.
