import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def getData():
    dataCsv = pd.read_csv(
        "data/country_vaccinations.csv",
        usecols=["country","iso_code","date","total_vaccinations","people_vaccinated","people_fully_vaccinated","daily_vaccinations_raw","daily_vaccinations","total_vaccinations_per_hundred","people_vaccinated_per_hundred","people_fully_vaccinated_per_hundred","daily_vaccinations_per_million","vaccines"],
        parse_dates=["date"],
        na_values=[".", "???",""],
        sep=",",
        index_col="iso_code"
        )
    dataCsv = dataCsv.fillna(0)
    dfCovid = pd.DataFrame(data=dataCsv)
    return dfCovid


dfData = getData()

fig = plt.figure()

"""ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
#ax3 = fig.add_subplot(1, 1, 3)

#Cantidad personas vacunadas por pais

dataMundial = dfData[dfData["date"] == "2021-12-05"]
dfPaisesSort = dataMundial.sort_values("people_vaccinated",ascending=True)
ax1.bar(dfPaisesSort["country"],dfPaisesSort["people_vaccinated"])
plt.title("Cantidad de vacunas diarias en Chile", fontsize=20, color="b")
plt.xlabel('cantidad de vacunados', fontsize=14)
plt.ylabel('Pais', fontsize=14)



#Cantidad personas vacunadas de chile por fecha

dataChile = dfData[dfData["country"] == "Chile"]
ax2.plot(dataChile["date"],dataChile["daily_vaccinations_raw"])
plt.title("Cantidad de vacunas diarias en Chile", fontsize=20, color="b")
plt.ylabel('cantidad de vacunados', fontsize=14)
plt.xlabel('Tiempo', fontsize=14)"""




grouped = dfData.groupby('country').agg('vaccines')
grouped = grouped.set_index(['country','vaccines'])
second = grouped.join(dfData.set_index(['country', 'vaccines']))
print(second)
plt.show()