import pandas as pd

def main():
    customers = pd.read_csv("customers.csv")
    df = pd.DataFrame(customers)
    cc = df[['FirstName', 'LastName', 'Country']]
    cc.to_csv('customer_country.csv')

main()