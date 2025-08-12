"""
CSV Analysis -> PDF report
Usage: python analyze.py input.csv output.pdf
"""
import sys
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

def analyze(infile, outfile):
    df = pd.read_csv(infile)
    # simple cleaning
    df = df.dropna()
    # assume columns: date, product, sales, quantity
    if 'sales' in df.columns:
        with PdfPages(outfile) as pdf:
            plt.figure()
            df.groupby('product')['sales'].sum().sort_values().plot(kind='bar')
            plt.title('Sales by product')
            plt.tight_layout()
            pdf.savefig()
            plt.close()

            plt.figure()
            df.groupby('date')['sales'].sum().plot()
            plt.title('Sales over time')
            plt.tight_layout()
            pdf.savefig()
            plt.close()
    else:
        print("CSV must contain a 'sales' column")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python analyze.py input.csv output.pdf")
    else:
        analyze(sys.argv[1], sys.argv[2])
