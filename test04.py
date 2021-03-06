import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np



df = pd.read_csv("FuelConsumption.csv")
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]

msk = np.random.rand(len(df))< 0.8
# print(msk)
train = cdf[msk]
test = cdf[~msk]

#### Train data distribution
plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()