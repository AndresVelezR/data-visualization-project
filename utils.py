import read_csv

data = read_csv.read_csv('./app/data.csv')
south_america_data = list(filter(lambda country: country['Continent'] == 'South America', data))
population_years = [2022, 2020, 2015, 2010, 2000, 1990, 1980, 1970]

def select_country(country_name):
    country_name = country_name.title().strip()
    selected_country = list(filter(lambda country : country['Country/Territory'] == country_name, data))
    return selected_country

def get_selected_pupulation(selected_country):
    total_population = {}
    for year in population_years:
        population = list(map(lambda country: country[f'{year} Population'],selected_country))
        population_number = int(population[0])
        total_population[f'{year}'] = population_number
    return total_population

def get_population_percentage(data_list):
    percentage = list(map(lambda country : country['World Population Percentage'] , data_list))
    country_territory = list(map(lambda country: country['Country/Territory'], data_list))
    iterable = list(zip(country_territory, percentage))
    country_percentage_dict = {key:value for key,value in iterable}

    return country_percentage_dict




