#Calculating Good Measure
corona_dataset_aggregated.loc["China"][:3].plot()     #Drawing plot for first 3 days of corona outbreak
corona_dataset_aggregated.loc["China"].diff().plot()    #drawing rate of spred of corona on china

corona_dataset_aggregated.loc["China"].diff().max()      #max number of corona cases found on



#to find maximum infection rate for all countries in our dataset
countries = list(corona_dataset_aggregated.index)
max_infection_rates=[]      #empty list
for country in countries:
	rates=corona_dataset_aggregated.loc[country].diff().max()
	max_infection_rates.append(rates)

corona_dataset_aggregated["max_infection_rates"]=max_infection_rates    #join max_infectionrate to corona dataset


#creating new DataFrame with max_infection_rates and countries
corona_dataset = pd.DataFrame(corona_dataset_aggregated["max_infection_rates"])
