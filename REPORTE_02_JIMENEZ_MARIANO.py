#Importamos pandas y los datos proporcionados.

import pandas as pd
from sqlalchemy import false 

#Creamos un dataframa con los datos proprcionados para poder trabajar con ellos
sldb= pd.read_csv('synergy_logistics_database.csv')

#Filtramos para las exportaciones y agrupamos por pais de origen, destino y modo de transporte para ver los valores
exports=sldb[sldb['direction']=="Exports"]
realexp=exports.groupby(['origin','destination','transport_mode']).sum().sort_values(by="total_value",ascending=False)
#Filtramos para las importaciones y agrupamos por pais de origen, destino y modo de transporte para ver los valores
imports=sldb[sldb['direction']=="Imports"]
realimp=imports.groupby(['origin','destination','transport_mode']).sum().sort_values(by="total_value", ascending=False)
#Guardamos la informacion obtenida en una nueva variable donde solo se muestra los top 10
exp=realexp.head(10)
imp=realimp.head(10)
#Agrupamos por transportacion mode y los ordenamos de mayor a menor
transpmode=sldb.groupby(["transport_mode"]).sum().sort_values(by="total_value",ascending=False)
transmodet3=transpmode.head(3)

#Agregamos una columna con los valores de porcentajes de las exportaciones 
exports['porcentaje']=exports['total_value']/exports['total_value'].sum()*100
#Agrupamos y sumamos para saber cuales son los paises que dejan mas en cuestion de valor
export80=exports.groupby(['origin']).sum().sort_values(by="porcentaje",ascending=False)

#Agregamos una columna con los valores de porcentajes de las importaciones 
imports['porcentaje']=imports['total_value']/imports['total_value'].sum()*100
#Agrupamos y sumamos para saber cuales son los paises que dejan mas en cuestion de valor
import80=imports.groupby(['origin']).sum().sort_values(by="porcentaje",ascending=False)

#Imprimimos los valores 
print("Las 10 rutas de exportacion mas demandas por su valor son:", exp)
print("Las 10 rutas de importacion mas demandas por su valor son:", imp)
print("Los 3 medios de transporte mas importante son: ", transmodet3)

print("Los paises que generan el 80 de las exportaciones es:", export80)
print("Los paises que generan el 80 de las importaciones es:", import80)
