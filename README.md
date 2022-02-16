# Tips Prediction for Chicago dataset

### Data
https://data.cityofchicago.org/Transportation/Taxi-Trips/wrvz-psew/data

### Objective
The cost of a taxi ride is frequently a surprise, as it is determined by a variety of factors that cannot be predicted in advance. Customers tip in a variety of ways depending on a variety of factors.

In this research, the goal is to use this dataset to forecast the tip for a trip using just information available ahead of time.

### Data Description
1. (unique_key)
2. (taxi_id)
3. (trip_start_timestamp)   
4. (trip_endtimestamp)
5. (trip_seconds) 
6. (trip_miles) 
7. (pickup_census_tract) (Uniquely numbered in each county with a. numeric code)
8. (dropoff_census_tract) ((Uniquely numbered in each county with a. numeric code)
9. (pickup_community_Area)
10. (dropoff_community_Area)
11. (fare) 
12. (tips) 
13. (tolls) 
14. (extras) 
15. (trip_total)
          -- Fare + Tips + Tolls + Extras  
16. (payment_type)
17. (company)
          
18. (pickup_latitude) 
          
19. (pickup_longitude) 
          
20. (pickup_location)
         
21. (dropoff_latitude)
         
22. (dropoff_longitude)

23. (dropoff_location)

         
# Exploratory Data Analysis
I assume that a trip is considered valid if it has non zero miles.  
Found big number of observation having a distance of 0m. This is likely to be bad data, so have removed those rows. 

# Feature Selection
* Since we are restricting the problem data to that which can be obtained before taking a taxi, we are gonna drop all but those variables.

* We have two factors derived from the location: census and community area. Because for privacy reasons some census tracks are missing, we are not going to use that factor.

* As for the target variable, we are only considering the 'Tips'.