import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('AFE_Population.csv')

df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

plt.bar(X, Y, color='b')
plt.title("Africa East and South Population over the Years")
plt.xlabel("Years")
plt.ylabel("Population (x 10^6)")

plt.show()
