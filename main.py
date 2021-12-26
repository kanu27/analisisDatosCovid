import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def getData():
    dataCsv = pd.read_csv(
        "data/csv/country_vaccinations.csv",
        usecols=["country", "iso_code", "date", "total_vaccinations", "people_vaccinated", "people_fully_vaccinated", "daily_vaccinations_raw", "daily_vaccinations",
                 "total_vaccinations_per_hundred", "people_vaccinated_per_hundred", "people_fully_vaccinated_per_hundred", "daily_vaccinations_per_million", "vaccines"],
        parse_dates=["date"],
        na_values=[".", "???", ""],
        sep=",",
        index_col="iso_code"
    )
    dataCsv = dataCsv.fillna(0)
    dfCovid = pd.DataFrame(data=dataCsv)
    return dfCovid
 
# 1 Cantidad de personas vacunadas a la fecha para cada país, ordenados de menor a mayor (people_vaccinated) (1.5 pt.)
def personVacunXPais():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    dataMundial = dfData[dfData["date"] == "2021-12-05"]
    dfPaisesSort = dataMundial.sort_values("people_vaccinated", ascending=True)
    ax.bar(dfPaisesSort["country"], dfPaisesSort["people_vaccinated"])
    plt.xticks(rotation=90)
    plt.title("Cantidad de personas vacunadas a la fecha para cada país", fontsize=20, color="b")
    plt.xlabel('Pais', fontsize=14)
    plt.ylabel('cantidad de vacunados', fontsize=14)

# 2 Cantidad de vacunas diarias en Chile, desde la primera fecha hasta la última (daily_vaccinations_raw) (2.0 pt.)
def personVacunEnChile():
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(1, 1, 1)
    dataChile = dfData[dfData["country"] == "Chile"]
    ax1.plot(dataChile["date"], dataChile["daily_vaccinations_raw"])
    plt.title("Cantidad de vacunas diarias en Chile", fontsize=20, color="b")
    plt.ylabel('cantidad de vacunados', fontsize=14)
    plt.xlabel('Tiempo', fontsize=14)

# 3 Mostrar porcentualmente y en bruto (en un mismo gráfico) el porcentaje/cantidad de tipos de vacuna (vaccines) (2.5 pt.)
def porcentajeValor(pct, todosLosValores): 
    absoluto = int(pct / 100*np.sum(todosLosValores))
    return "{:.1f}%\n({:d})".format(pct, absoluto) 

def TipoDeVacunas():
    vacunasDict = dict()
    vacunasList = list()
    vacunasPorPais = dfData.groupby('country').agg('vaccines').unique()
    for vacunas in vacunasPorPais:
        vacunas = vacunas[0].replace(' ', '')
        listaDeVacunasPorPais = vacunas.split(',')
        for vacuna in listaDeVacunasPorPais:
            vacunasList.append(vacuna)
            vacunasDict[vacuna] = 0
        for vacuna in vacunasList:
            vacunasDict[vacuna] += 1
    listaKeys = list()
    listaData = list()
    for key in vacunasDict:
        listaKeys.append(key)
        listaData.append(vacunasDict[key])
    fig3, ax3 = plt.subplots()
    wedges, texts, autotexts = ax3.pie(listaData,
                                      autopct=lambda pct: porcentajeValor(pct, listaData),
                                      labels=listaKeys,
                                      shadow=True,
                                      startangle=90,
                                      textprops=dict(color="white"))
    ax3.legend(wedges, listaKeys,
              title="Tipos de Vacunas",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=8, weight="bold")
    ax3.set_title("Vacunas presentes paises")

#4 Cantidad de días que ha durado el proceso de vacunación para cada país (date) (2.0 pt.)
def CantDeDiasXPais():    
    fig4 = plt.figure()
    ax4 = fig4.add_subplot(1, 1, 1)
    vacunasPorPais = dfData.groupby(['country'])
    fechaList = list()
    paisList = list()
    for a in vacunasPorPais:
        paisList.append(a[0])
        diff = str(a[1]['date'][len(a[1]['date'])-1] - a[1]['date'][0])
        fechaList.append(int(diff.split(' ')[0]))
    df = pd.DataFrame(list(zip(paisList,fechaList)), columns = ['Pais','CantDias'])
    ax4.barh(df['Pais'],df['CantDias'])
    plt.title("Duracion del proceso de vacunacion", fontsize=20, color="b")
    plt.ylabel('Pais', fontsize=14)
    plt.xlabel('cantidad de dias', fontsize=14)    
    
#5 Cantidad de vacunados diarios para los países: Chile, Argentina y Brasil en un mismo gráfico (daily_vaccinations_raw) (2.0 pt.) 
def CanVacunChArBr():
    dataChile = dfData[dfData["country"] == "Chile"]
    dataArgentina = dfData[dfData["country"] == "Argentina"]
    dataBrazil = dfData[dfData["country"] == "Brazil"]
    fig5 = plt.figure()
    ax5 = fig5.add_subplot(1, 1, 1)
    ax5.plot(dataChile['date'],dataChile['daily_vaccinations_raw'],color="r", label="Chile")
    plt.plot(dataArgentina['date'],dataArgentina['daily_vaccinations_raw'],color="b",label="Argentina")
    plt.plot(dataBrazil['date'],dataBrazil['daily_vaccinations_raw'],color="g",label="Brazil")
    plt.legend(loc="best", facecolor="w", fontsize=16)
    plt.ylabel('Cantidad de Vacunado', fontsize=14)
    plt.xlabel('Tiempo', fontsize=14)   
    plt.title("Vacunados Diarios segun Pais", fontsize=20, color="b")

dfData = getData()
personVacunXPais()
personVacunEnChile()
TipoDeVacunas()
CantDeDiasXPais()
CanVacunChArBr()
plt.show()