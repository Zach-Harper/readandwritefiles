import pandas as pd

def main():
    employee = pd.read_csv('EmployeePay.csv')
    df = pd.DataFrame(employee)
    print(df)

main()