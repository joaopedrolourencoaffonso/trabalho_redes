import math
import matplotlib.pyplot as plt
import sys
from distfit import distfit
import numpy

arquivo = str(sys.argv[1]);
#media = int(sys.argv[2]);
#arquivos = ["dns_18-19_18-11-2020.txt","dns_19-20_18-11-2020.txt", "dns_20-21_18-11-2020.txt", "dns_06-07_20-11-2020.txt"]
arquivos = [arquivo + "_18-19_18-11-2020.txt", arquivo + "_19-20_18-11-2020.txt", arquivo + "_20-21_18-11-2020.txt",  arquivo + "_06-07_20-11-2020.txt"]
lista = [];

print("           nome             | variancia | desvio_padrao");

somatorio = 0;
medidas = 0;
num = 0;
soma = 0;

for z in arquivos:
        file = open(z, 'r');
        lines = file.readlines();
        size = len(lines);
        x = range(2, size - 6);

        for i in x:
                temp = lines[i].split();
                if "limite" in temp:
                        continue;
                else:
                        temp = temp[4].split("=");
                        temp = temp[1].split("ms");
                        temp = int(temp[0]);
                        num = num + 1;
                        soma = soma + temp;

media = soma / num;
                        

for z in arquivos:
        file = open(z, 'r');
        lines = file.readlines();
        size = len(lines);
        x = range(2, size - 6);

        for i in x:
                temp = lines[i].split();
                if "limite" in temp:
                        continue;
                else:
                        medidas = medidas + 1;
                        temp = temp[4].split("=");
                        temp = temp[1].split("ms");
                        temp = int(temp[0]);
                        somatorio = somatorio + (temp - media)*(temp - media);
                        lista.append(temp);
                        #print(str(temp) + " " + str(medidas) + " " + str(temp - media_total)*());

        variancia = somatorio / medidas;
        variancia = round(variancia, 2);
        desvio_padrao = math.sqrt(variancia);
        desvio_padrao = round(desvio_padrao, 2);

print( "dns: " + str(variancia) + " | " + str(desvio_padrao));

############

dist = distfit()
x = numpy.array(lista, dtype=numpy.float32)
dist.fit_transform(x);
print(dist.summary);
print(dist.model);


#############

plt.title('Distribuição total do DNS', fontsize=20)
plt.xlabel('Intervalos', fontsize=15)
plt.ylabel('Número de Pacotes por intervalo', fontsize=15)
plt.tick_params(labelsize=15)
plt.hist(lista, bins=[0, 29.6, 59.2, 88.8, 118.4, 148.0, 177.6, 207.2, 236.8, 266.4], rwidth=0.9);
plt.show();                   





