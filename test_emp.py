from emp import employee_details
def test_employee_details():
    expected_output = (
        "Employee Name:chitra\n"
        "Employee ID:E1001\n"
        "Department:IT\n"
        "Salary:55000\n"
    )
    assert employee_details("chitra", "E1001", "IT", 55000) == expected_output