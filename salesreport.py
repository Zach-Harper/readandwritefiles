import pandas as pd
import numpy as np

def main():
   
    sales = pd.read_csv('sales.csv')
    df = pd.DataFrame(sales)
    df.astype({'SubTotal':'float', 'TaxAmt':'float', 'Freight':'float'})
    col_list = ['SubTotal', 'TaxAmt', 'Freight']
    df['Total'] = df[col_list].sum(axis=1)
    grouped_df = df.groupby(['CustomerID'])
    sales_report = grouped_df['Total'].agg(sum)
    sales_report.to_csv('salesreport.csv')

main()