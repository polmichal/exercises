from weather import Weather, Unit
import matplotlib.pyplot as plt
import numpy as np

weather = Weather(unit=Unit.CELSIUS)
# id`s miejscowosci: http://woeid.rosselliot.co.nz/lookup/olsztyn
olsztyn = 510583

obserwacja = weather.lookup(olsztyn)
pogoda = obserwacja.condition
prognoza = obserwacja.forecast

print('Today is',pogoda.date)
print(pogoda.temp, 'st.C.', pogoda.text)

temp_max_na_tydzien =[]
temp_min_na_tydzien =[]
daty = []

for forecast in prognoza:
    daty.append(forecast.date)
    maksymalna = int((forecast.high))
    minimalna = int((forecast.low))
    srednia = (maksymalna+minimalna)/2
    temp_max_na_tydzien.append(maksymalna)
    temp_min_na_tydzien.append(minimalna)
skrocone =[]
for d in daty:
    skrocone.append(d[0:2])

dwie_temp = np.array([temp_max_na_tydzien]+[temp_min_na_tydzien])
srednia = np.average(dwie_temp, axis=0)

def plot_wykres():
    plt.plot(skrocone, srednia,'C1', linewidth=2, )
    plt.title('Prognoza pogody w Olsztynie')
    plt.xlabel('Data')
    plt.ylabel('Temperatura')
    plt.grid()
    # Opcjonalne tło na wykresie:
    #tlo = plt.gca()
    #tlo.set_facecolor('tab:blue')
    plt.show()

def plot_bar():
    p1 =plt.bar(skrocone, temp_max_na_tydzien, color=(0.1, 0.2, 0.5, 0.3))
    p2 =plt.bar(skrocone, temp_min_na_tydzien, color=(0.1, 0.2, 0.5))
    p3, = plt.plot(srednia, 'C1', linewidth=2)
    plt.legend((p1[0], p2[0], p3), ('temp. max', 'temp. min', 'temp. średnia'))
    # opcjonalnie plt.grid - siatka
    #plt.grid()
    plt.title('Prognoza pogody w Olsztynie')
    plt.xlabel('Data')
    plt.ylabel('Temperatura')
    plt.show()

# Wykres w dwóch postaciach:
plot_wykres()
plot_bar()