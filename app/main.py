import utils
import read_csv
import charts
import pandas as pd

def run():
  """
  Solucion sin pandas
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
  """

  # Solución con pandas
  df = pd.read_csv('data.csv')
  df2 = df[df['Continent'] == 'Africa'] 
  # Se busca en el data frame df en la columna Continent donde sea igual a sur america
  countries = df2['Country'].values # metodo de pandas para obtener valores
  percentages = df2['World Population Percentage'].values # metodo de pandas para obtener valores

  # Parte del código que sirve en los dos metodos
  charts.generate_pie_chart(countries, percentages)
  
  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)


if __name__ == '__main__':
  run()