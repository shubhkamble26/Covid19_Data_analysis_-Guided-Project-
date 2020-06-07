#Plotting GDP vs maximum Infection rate
X=data["GDP per capita"]
y=data["max_infection_rates"]
sns.scatterplot(X,y)


#as scatterplot is not evenly distributed we apply log to y
sns.regplot(X,np.log(y))


#Plotting Social support vs maximum Infection rate
X=data["Social support"]
y=data["max_infection_rates"]
sns.scatterplot(X,np.log(y))


#Plotting Healthy life expectancy vs maximum Infection rate
X=data["Healthy life expectancy"]
y=data["max_infection_rates"]
sns.scatterplot(X,np.log(y))


#Plotting Freedom to make life choices vs maximum Infection rate
X=data["Freedom to make life choices"]
y=data["max_infection_rates"]
sns.scatterplot(X,np.log(y))