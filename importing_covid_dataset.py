corona_dataset_csv=pd.read_csv("Datasets/Covid19_Confirmed_dataset.csv")        #imported dataset
useless_cols=["Lat","Long"]
corona_dataset_csv.drop(useless_cols,axis = 1,inplace = True)        #drop useless columns
corona_dataset_aggregated=corona_dataset_csv.groupby("Country/region").sum()   #aggregate corona_dataset_csv by country or region



#visualising data related to countries like China,Spain,Italy
corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["Spain"].plot()
corona_dataset_aggregated.loc["Italy"].plot()
plt.legend()
