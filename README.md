# Molekule

'''

Description: Extract and transform data from a publicly accessible API
Considerations
API Credentials
Preferred Languages: Python
Reusability of code - could we leverage code for other APIs?
No need to spend more than 3 hours on project
Have fun with the project

Steps
1. Access API with credentials
2. Extract raw data into staging table
3. Propose data schema based on available data

'''

Since the beginning of 2020, the outbreak of COVID-19 has been constantly reorienting people's relationship to the outside world. This project provides a small example of the trend of this world pandemic with the help of the API provided by Gramzivi (https://rapidapi.com/Gramzivi/api/covid-19-data/endpoints). This API collects information from several reliable sources, like Johns Hopkins CSSE, CDC, WHO and a few others. 

![Test Image 2](/api.png)

It has several endpoints and the one that I chose is 'the latest daily report all countries'.

appkey = "3cc7e29631msh7cee92aae021fbfp15ff33jsn261ecaba7473"
url = "https://covid-19-data.p.rapidapi.com/report/country/all"
headers = {
    'x-rapidapi-key': appkey,
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

After fetching the data, I filtered the data to include only the first three months of the outbreak in the USA (between 2020-03-01 to 2020-05-31). 

![Test Image 3](/time_filter.png)

There are 9 columns in the dataframe: country, province, number of confirmed, number of recovered, number of  deaths, number of active, latitude, longitude and date. 

It is transformed into a dataframe and is also written out to a csv file. 
It occured to me that it would be super interested if we can use the latitude and longitude provided here to do some GIS analysis. 

![Test Image 4](/df.png)

I put the file into a S3 bucket and read it with a PySpark Script in order to save it as a table. 

Schema:

![Test Image 1](/schema.png)

The table:

![Test Image 5](/table.png)

Some simple queries:

This query shows that at the beginning of the outbreak, Washington surely went through dark times. 
https://www.statnews.com/2020/02/29/new-covid-19-death-raises-concerns-about-virus-spread-in-nursing-homes/
![Test Image 6](/query1.png)
Above is data of 2020-03-02

However, after only one month, New York and New Jersey have become even worse. 
![Test Image 7](/query2.png)
Above is data of 2020-05-14
    
Hope everyone stays safe and healthy! Hope we can all meet after this pandemic :)!

Please kindly let me know if you have any questions. Thank you so much.






