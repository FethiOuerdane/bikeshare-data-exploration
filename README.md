# Documentation
>This is a Documentation for the US Bikeshare Project of the Udacity **Programming for Data Science with Python** Nanodegree course.

![image](https://journalistsresource.org/wp-content/uploads/2015/05/Bikeshare-station-.jpg)

### Date created
Monday, September 6, 2021. 10:40AM

### Project Title
GitHub Project: Explore US Bikeshare Data

### Description
In this project, you will explore data related to bike share systems for three major cities in the United States: Chicago, New York City, and Washington.

The project contains a Python program that allows the user to explore an US bikeshare system database and retrieve statistics information from the database. The user is able filter the information by city, month and weekday, in order to visualize statistics information related to a specific subset of data. The user is also able to chose to view raw data and to sort this data.

### Files used
- **bikeshare.py**.
- **chicago.csv** - Dataset containing all bikeshare information for the city of Chicago provided by Udacity.
- **new_york_city.csv** - Dataset containing all bikeshare information for the city of New York provided by Udacity.
- **washington.csv** - Dataset containing all bikeshare information for the city of Washington provided by Udacity. Note: This does not include the 'Gender' or 'Birth Year' data.

(_these **csv** files are not included in this repo but can be downloaded from the material provided in the course_) .

## Program Details:

The program takes user input for one of the 3 cities mentioned earlier (e.g. Chicago), month for which the user wants to filter the data (e.g. January), and day for which the user wants to filter data (e.g. Monday).

#### Program Requirements:
+ Language: Python 3.8 or above
+ Libraries: [pandas](https://pandas.pydata.org/), [numpy](http://www.numpy.org/), [time](https://docs.python.org/2/library/time.html), [tabulate](https://pypi.org/project/tabulate)


### Credits
Here are some links to websites and blogposts I consulted:

+ [I Used the code provided here to convert duration time from seconds to Hour/minutes/Seconds](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html)
+[This code helped to check if Column exist in a DataFrame](https://stackoverflow.com/a/39371897)
+[This Python library helped me display the statistics calculated in a pretty way](https://pypi.org/project/tabulate/).

Other helpful links:
+ https://www.geeksforgeeks.org/ways-to-filter-pandas-dataframe-by-column-values/
+ https://stackoverflow.com/questions/60339049/weekday-name-from-a-pandas-dataframe-date-object

Also credit to [adam-p/markdown-here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) in helping in the styling of this Documentation
