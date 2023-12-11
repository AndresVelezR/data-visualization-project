import utils 
import charts


def run_population_by_year():
    country_name = input('Please enter the name of a country')
    country = utils.select_country(country_name)
    if len(country) > 0:
        population_dict = utils.get_selected_pupulation(country)
        labels = list(population_dict.keys())
        values = list(population_dict.values())
        charts.generate_bar_chart(labels, values, country_name.title())
    else:
        print('The country you entered is not recognized, try again \n')
        run_population_by_year()

def run_population_percentage(x):
    percentage_dict = utils.get_population_percentage(x)
    labels = list(percentage_dict.keys())
    values = list(percentage_dict.values())
    charts.generate_pie_chart(labels, values)
    
    

if __name__ == '__main__':
    #run_population_by_year()
    while True: 
        print("_________________________________________________________________________")
        print("|1| Select option 1 for a pie chart of South America's population. \n")
        print("|2| Choose option 2 for a pie chart of the Global Population. \n")
        print("|3| Opt for option 3 to generate a bar chart of a specific country's population by year. \n")
        print("|4| Enter 4 to exit \n")
        print("_________________________________________________________________________")

        option = input("Please enter your option => ").strip()
            
        if option == '1':
            x = utils.south_america_data
            run_population_percentage(x)
        elif option == '2':
            x = utils.data
            run_population_percentage(x)
        elif option == '3':
            run_population_by_year()
        elif option == '4':
            break
        else:
            print('Invalid option, try again')
            
        

    
   


    