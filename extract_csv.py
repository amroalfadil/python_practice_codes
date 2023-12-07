#read 1 csv file from the website
import pandas as pd
df_housing_charter = pd.read_csv('https://www.housingregulator.gov.scot/media/1771/arc_export_legacy_201314_201819.csv')
# showing dataframe
print(df_housing_charter)
#rename columns
df_housing_charter.rename(columns = {'Name of approver':'Name_of_approver'}, inplace = True)
#show data frame
print(df_housing_charter)