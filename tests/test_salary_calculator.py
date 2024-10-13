import unittest
import sys
import os

# Adiciona o caminho do diretório src para o sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from employee import Employee
from salary_calculator import SalaryCalculator

class TestSalaryCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = SalaryCalculator()

    def test_developer_salary_above_3000(self):
        emp = Employee(name="Alice", email="alice@example.com", base_salary=3500, role="DESENVOLVEDOR")
        net_salary = self.calculator.calculate_net_salary(emp)
        self.assertEqual(net_salary, 3500 * 0.8)

    def test_developer_salary_below_3000(self):
        emp = Employee(name="Bob", email="bob@example.com", base_salary=2500, role="DESENVOLVEDOR")
        net_salary = self.calculator.calculate_net_salary(emp)
        self.assertEqual(net_salary, 2500 * 0.9)

    def test_dba_salary_above_2000(self):
        emp = Employee(name="Carol", email="carol@example.com", base_salary=2500, role="DBA")
        net_salary = self.calculator.calculate_net_salary(emp)
        self.assertEqual(net_salary, 2500 * 0.75)

    def test_dba_salary_below_2000(self):
        emp = Employee(name="Dan", email="dan@example.com", base_salary=1800, role="DBA")
        net_salary = self.calculator.calculate_net_salary(emp)
        self.assertEqual(net_salary, 1800 * 0.85)

    def test_tester_salary_above_2000(self):
        emp = Employee(name="Eve", email="eve@example.com", base_salary=2200, role="TESTADOR")
        net_salary = self.calculator.calculate_net_salary(emp)
        self.assertEqual(net_salary, 2200 * 0.75)

    def test_manager_salary_above_5000(self):
        emp = Employee(name="Frank", email="frank@example.com", base_salary=6000, role="GERENTE")
        net_salary = self.calculator.calculate_net_salary(emp)
        self.assertEqual(net_salary, 6000 * 0.7)

    def test_invalid_role(self):
        emp = Employee(name="Grace", email="grace@example.com", base_salary=4000, role="CEO")
        with self.assertRaises(ValueError):
            self.calculator.calculate_net_salary(emp)

if __name__ == '__main__':
    unittest.main()
