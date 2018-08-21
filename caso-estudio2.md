# Universidad EAFIT
# Curso Big Data - XM, 2018-1
# Profesor: Edwin Montoya M. – emontoya@eafit.edu.co

Explorar este sitio: http://blog.cloudera.com/blog/2015/10/how-to-use-hues-notebook-app-with-sql-and-apache-spark-for-analytics/

# 1. caso de estudio para: Bay Area Bike Share (BABS) system.

# 2. descargar los datasets de: http://www.bayareabikeshare.com/datachallenge

# 3. Cargar los datos en ../datasets

# 4. crear las tablas vía wizard e importar los datos en las tablas SQL:

# 5. Responder la pregunta: top 10 most popular start stations based on the trip data:

    SELECT startterminal, startstation, COUNT(1) AS count 
    FROM trips 
    GROUP BY startterminal, startstation 
    ORDER BY count DESC LIMIT 10

>> visualice datos en barras

Insight: It seems that the San Francisco Caltrain (Townsend at 4th) was by far the most common start station. Let’s determine which end stations, for trips starting from the SF Caltrain Townsend station, were the most popular.

# 6. Georeferenciación de estaciones:

We’ll fetch the latitude and longitude coordinates so that we can visualize the results on a map.

    SELECT
    s.station_id,
    s.name,
    s.lat,
    s.long,
    COUNT(1) AS count
    FROM trips t
    JOIN stations s ON s.station_id = t.endterminal
    WHERE t.startterminal = 70
    GROUP BY s.station_id, s.name, s.lat, s.long
    ORDER BY count DESC LIMIT 10

Coloque en google maps esta información.

# 7. Pregunta: Let’s say we wanted to dig further into the trip data for the SF Caltrain station and find the total number of trips and average duration (in minutes) of those trips, grouped by hour.

Since the trip data stores startdate as a STRING, we’ll need to apply some string-manipulation to extract the hour within an inline SQL query. The outer query will aggregate the count of trips and the average duration.

    SELECT
        hour,
        COUNT(1) AS trips,
        ROUND(AVG(duration) / 60) AS avg_duration
    FROM (
        SELECT
            CAST(SPLIT(SPLIT(t.startdate, ' ')[1], ':')[0] AS INT) AS hour,
            t.duration AS duration
        FROM trips t
        WHERE
            t.startterminal = 70
            AND
            t.duration IS NOT NULL
        ) r
    GROUP BY hour
    ORDER BY hour ASC;
