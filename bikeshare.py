import time
import pandas as pd
import numpy as np
import datetime
from tabulate import tabulate

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities_list = ['chicago','new york city','washington']
month_list = ['january','february','march','april','may','june']
day_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    month, day,filter_type = "" ,"",""

    print('-'*100)
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:

        # get user input for city (chicago, new york city, washington)
        city = promptUser("Which city would you like to see Data for?",["Chicago","New york city","Washington"])
        if city in cities_list:
            break
    # get user input for month (all, january, february, ... , june)
    while True:
        print('-'*100)
        response_list= ["Month", "Day", "Both","No filter"]
        filter_type = promptUser("How would you like to filter data by?",response_list)
        if (filter_type in map(str.lower, response_list)):
            break
    if filter_type == "month" or filter_type == "both":
        while True:
            print('-'*100)
            month = promptUser("Which month would you like to filter data with?",map(lambda str: str.title(),month_list))
            if (month in month_list):
                break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    if filter_type == "day" or filter_type == "both":
        while True:
            print('-'*100)
            day = promptUser("Which day would you like to filter data with?",map(lambda str: str.title(),day_list))
            if day in day_list:
                break


    print('-'*40)
    return city, month, day,filter_type

def load_data(city):
    """
    Load Data for the specified city without any filter
    Args:
        (str) city - name of the city to analyze
    Returns:
        df - Pandas DataFrame containing city data with no filter applied
    """
    df = pd.read_csv(CITY_DATA[city])

    return df
def filter_data(df,month, day,filter_type):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df['Start Time'] = pd.to_datetime(df['Start Time'])
     # First we extract the month , day of the week and hour from Start Time into a seperate column:
    df['Month'] = df['Start Time'].dt.month
    # ------- For Python version 3.8.8 I used [ day_name ] instead of [ weekday_name ]
    df['day_of_the_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if filter_type.lower() == "both" or filter_type.lower() == "month" :
        df = df[df['Month'] == (month_list.index(month)+1)]
    if filter_type.lower() == "both" or filter_type.lower() == "day":
        df = df[df['day_of_the_week'] == day.title()]

    return df
def Convert_time(trip_duration):

    """ Convert trip duration time from Seconds to Hours/minutes/Seconds
        Parameters:
            (str) trip_duration - (in seconds)
        returns:
            (str) duration - (00 h 00 min 00 sec)
    """
    duration = ""
    hour = int(trip_duration) // 3600
    minutes = (int(trip_duration) % 3600)//60
    seconds = int(trip_duration) - (minutes*60) -(hour*3600)
    if hour == 0 and minutes > 0 and seconds > 0:
        duration = "{} min and {} sec".format(minutes,seconds)
    elif hour == 0 and minutes > 0 and seconds == 0:
         duration = "{} min".format(minutes)
    else:
         duration = "{} hour {} min and {} sec".format(hour,minutes,seconds)
    return duration
def display_raw_data(DataFrame,city,filter_type):
    """ Displays the raw data for selected city by interveral of 5 """
    if set(['Users Age','Age Group']).issubset(DataFrame.columns):
        df_new = DataFrame.drop([DataFrame.columns[0],DataFrame.columns[2],'Users Age','Age Group','Trip Duration','hour','day_of_the_week','Month'],axis = 1)
    else:
        df_new = DataFrame.drop([DataFrame.columns[0],DataFrame.columns[2],'Trip Duration','hour','day_of_the_week','Month'],axis = 1)

    # Trip Duration will be converted from seconds to Hour/minutes/seconds
    DataFrame['Trip Duration'] = DataFrame.apply(lambda row: Convert_time(row['Trip Duration']), axis=1)
    df_new.insert(3,'Trip Duration',DataFrame['Trip Duration'])
    df_display_idx = 0;
    while True:
        user_response = promptUser("Would you like to display raw data from {}?".format(city.title()),["Yes","No"])

        if user_response == 'yes':
            #Display General info about data and current row interval on display
            print(tabulate({"City": [city.title()],"Filter":[filter_type],"Rows":["From {} to {}".format(df_display_idx,df_display_idx+4)]}, headers='keys', tablefmt="fancy_grid"))
            #Display 5 rows from raw data for the city selected
            print(tabulate(df_new[df_display_idx:df_display_idx+5],headers="keys", tablefmt='psql'))
            df_display_idx +=5
        if user_response == 'no':
            break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    # Convert the Start Time to Date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
     # First we extract the month , day of the week and hour from Start Time into a seperate column:
    df['Month'] = df['Start Time'].dt.month
    # ------- For Python version 3.8.8 I used [ day_name ] instead of [ weekday_name ]
    df['day_of_the_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # Calculate the most common month
    popular_month = month_list[df['Month'].mode()[0]-1].title()


    # Calculate the most common day of week
    popular_dayoftheweek = df['day_of_the_week'].mode()[0]


    # Calculate the most common start hour
    popular_hour = df['hour'].mode()[0]

    #Display the Data calculated above in a Table form
    print(tabulate([['Most Common Month is:', popular_month],["Most Frequent day of the week:",popular_dayoftheweek],["Most Frequent Start Hour:",popular_hour]], tablefmt='grid'))

def promptUser(question,possibleResponses):
    """ Prompt the user with a question and possible Responses set from function arguments
        Args:
         (str) - Question to ask the user
         (list) - the list of possible answer the user can choose
        Returns:
            (str)- the chosen response
    """

    print("\n" + tabulate({"Prompt":[question],"Possible responses":possibleResponses},headers="keys", tablefmt="presto"))
    response = input('\nAnswer: ').strip().lower()
    return response


def station_stats(df,filter_type):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Calculate most commonly used start station
    popular_starstation = df['Start Station'].mode()[0]
    count_pop_station = max(df['Start Station'].value_counts().tolist())

    # Calculate most commonly used end station
    popular_endstation = df['End Station'].mode()[0]
    count_pop_endstation = max(df['End Station'].value_counts().tolist())


    # Calculate most frequent combination of start station and end station trip
    popular_end_start_trip = (df['Start Station'] + ', ' + df['End Station']).mode()[0]
    count_pop_trip = max((df['Start Station'] + ', ' + df['End Station']).value_counts().tolist())

    #Display the Data calculated above in a Table form
    print(tabulate([["Most Popular Start Station",popular_starstation,count_pop_station,filter_type],["Most Popular End Station",popular_endstation,count_pop_endstation,filter_type],["Most Popular Start to End Station trip",popular_end_start_trip,count_pop_trip,filter_type]],headers = ["","","Count","Filter"], tablefmt='psql'))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculate total travel time
    total_travel_time = Convert_time(df['Trip Duration'].sum())

    # Calculate mean travel time
    average_travel_time = Convert_time(df['Trip Duration'].mean())

    #Display the Data calculated above in a Table form
    print(tabulate([['Total travel time is:', total_travel_time],["Average travel time is:",average_travel_time]], tablefmt='grid'))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city,filter_type):
    """Displays statistics on bikeshare users.

    Keyword arguments:
            df -- the DataFrame for the city chosen
            city -- the city chosen by user
            filter_type -- Type of the filter used on the data
    """




    user_response = promptUser("Would you like to check User Statistcs for {}?".format(city.title()),["Yes","No"])

    if user_response == "yes":
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Calculate counts of user types
        user_types_count = df['User Type'].value_counts().to_frame('')
        user_types_count["Filter"] = filter_type
        print("\nThe Number of Users for each User Type: \n")
        print(tabulate(user_types_count, headers=['User Type','Count','Filter'], tablefmt='psql'))

        # Calculate counts of gender
        if city.lower() != 'washington':
            gender_counts = df['Gender'].value_counts().to_frame('')
            gender_counts["Filter"] = filter_type.title()
            print("The Number of users for each gender: \n")
            print(tabulate(gender_counts, headers=['Gender','Count',"Filter"], tablefmt='github'))

        # Calculate earliest, most recent, and most common year of birth
        if city.lower() != 'washington':
            most_recent_birth_year = df['Birth Year'].max()
            earliest_brith_year = df['Birth Year'].min()
            common_birth_year = df['Birth Year'].mode()[0]
            print("\nBirth Year statistics for {}\n".format(city.title()))
            print(tabulate([['Most Recent Birth Year', most_recent_birth_year,filter_type],["Earliest Brith Year",earliest_brith_year,filter_type],["Most Common Birth Year",common_birth_year,filter_type]],headers =["","Year","Filter"], tablefmt='github'))

            #Calculate Age Group of users and their usage
            df["Users Age"] = df.apply(lambda row: datetime.datetime.now().year - row['Birth Year'],axis=1)
            bins= [0,12,20,35,49,74,130]
            labels = ['[0-12]','[13-20]','[21-35]','[36-49]','[50-74]','+75']
            df['Age Group'] = pd.cut(df['Users Age'], bins=bins, labels=labels, right=False)
            age_group_counts= df['Age Group'].value_counts().to_frame('')
            age_group_counts["Filter"] = filter_type
            print("\nThe Number of users for each Age Group: \n")
            print(tabulate(age_group_counts, headers=['Age Groups','Count',"Filter"], tablefmt='github'))

            #Stations with highest number of Subscribed users
            print("\nStations with highest number of Subscribed users: \n")
            subset_df = df[df['User Type']== "Subscriber"]
            start_station_count = subset_df['Start Station'].value_counts(sort =True).nlargest(6).to_frame()
            start_station_count["Filter"] = ""

            #Display the Data calculated above in a Table form
            print(tabulate(start_station_count, headers=['Start Station','N° of Subscribed Users',"Filter = {}".format(filter_type)], tablefmt='github'))
            print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*100)


def main():
    while True:
        try:
            city, month, day, filter_type = get_filters()
            df = load_data(city)
            print("\nThis is General Statistics for the city of {}".format(city.title()))

            #Check filter type
            if filter_type.lower() != "no filter":
                df = filter_data(df,month,day,filter_type)

            print("\n" + tabulate({"City":[city.title()],"Year":["2017"],"Filter":[filter_type.title()],"N° of Results":[df.size]},headers="keys", tablefmt="fancy_grid"))
            time_stats(df)
            station_stats(df,filter_type.title())
            trip_duration_stats(df)
            user_stats(df,city,filter_type.title())
            display_raw_data(df,city,filter_type.title())

            restart = promptUser("\nWould you like to restart?\n".format(city.title()),["Yes","No"])
            if restart != 'yes':
                break

        #Error Handeling part of the program        
        except KeyboardInterrupt:
            print("\n You chose to Exit the Program, stopping Now... \n")
            break
        except KeyError as e:
            print("Hmm, There seem to be an error somewhere \n")
            print("\n Try double check with:  ", e)
            print("\nThe program will stop now\n")
            break
        except Exception as excp:
            print("\nThe program will stop now\n")
            break
if __name__ == "__main__":
	main()
