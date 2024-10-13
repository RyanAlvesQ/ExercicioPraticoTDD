class SalaryCalculator:
    def calculate_net_salary(self, employee):
        role = employee.role.upper()
        salary = employee.base_salary

        if role == "DESENVOLVEDOR":
            return salary * 0.8 if salary >= 3000 else salary * 0.9
        elif role == "DBA" or role == "TESTADOR":
            return salary * 0.75 if salary >= 2000 else salary * 0.85
        elif role == "GERENTE":
            return salary * 0.7 if salary >= 5000 else salary * 0.8
        else:
            raise ValueError(f"Cargo {employee.role} não é reconhecido.")
