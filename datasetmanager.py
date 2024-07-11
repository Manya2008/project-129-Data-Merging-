import pandas as pd

df = pd.read_csv('dwarf_stars.csv')
#print(df)
final_data = df.dropna()
#print(final_data)
final_data["Radius"] = final_data["Radius"].astype(float)
final_data["Mass"] = final_data["Mass"].astype(float)
final_data["Radius"] *= 0.102763
final_data["Mass"] *= 0.000954588
#print(final_data)

final_data.to_csv("final_data.csv", index=True)