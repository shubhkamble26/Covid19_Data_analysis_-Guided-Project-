#importing happiness report and finding corrrelation between infection_rate and happiness
happiness_report_csv = pd.read_csv("worldwide_happiness_report.csv")
#preprocessing

useless_cols=[""]
happiness_report_csv.drop(useless_cols,axis=1,inplace  = True)      #dropping useless colmns

#setiing countries as index
happiness_report_csv.set_index("Country or region",inplace=True)

#join corona data and happiness_report_csv
data=corona_report.join(happiness_report_csv,how=inner)


#finding correlations btw different colmns of data
data.corr()