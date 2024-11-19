import pandas as pd
import sweetviz as sv

df = pd.read_csv("results.csv")
my_report = sv.analyze(df)
my_report.show_html()