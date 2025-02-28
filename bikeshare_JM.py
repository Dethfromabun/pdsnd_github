import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        try:
            city = input('Which city would you like to see data for?').lower()
            if (city == 'chicago') | (city == 'new york city') | (city == 'washington'):
                break
            else:   raise ValueError
        except: ValueError
        print("That is not a valid choice.  Please enter a city.")      

    # get user input for month (all, january, february, ... , june)

    while True:
        try: 
            month = input('Which month would you like to see? For all months, enter All.').lower()
            if (month == 'january') | (month == 'february') | (month == 'march') | (month == 'april'):
                break
            elif (month == 'may') | (month == 'june') | (month == 'all'):
                break
            else: raise ValueError
        except: ValueError
        print('That is not a valid choice.  Please enter all or a month.')        

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        try: 
            day = input('Enter a day of the week.  For all days, enter All.').lower()
            if (day == 'monday') | (day == 'tuesday') | (day == 'wednesday') | (day == 'thursday'): 
                break
            elif (day == 'friday') | (day == 'saturday') | (day == 'sunday') | (day == 'all'):
                break
            else: raise ValueError
        except: ValueError
        print('That is not a valid choice.  Please enter all or a day of the week.')            

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    """Pulling in correct city file and then changing start time to datetime to use with
    filters from the get filters function"""
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    """Taking filters from get filters and applying them to the df to make a new df"""
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    """Changing start time to datetime and extracting month, weekday and hour to be able to find the mode"""
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['dow'] = df['Start Time'].dt.weekday_name
    df['Start Hour'] = df['Start Time'].dt.hour


    # display the most common month
    """Getting the most common month with the mode method"""
    most_common_month = df['month'].mode()[0]

    # display the most common day of week
    """Getting the most common day of the week with the mode method"""
    most_common_dow = df['dow'].mode()[0]

    # display the most common start hour
    """Getting the most common hour with the mode method"""
    most_common_start_hour = df['Start Hour'].mode()[0]
    """Displaying resulting data to user"""
    print('The most common month of trips is: ')
    print(most_common_month)
    print('The most common day of the week of trips is: ')
    print(most_common_dow)
    print('The most common hour that trips start is: ')
    print(most_common_start_hour)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # display most commonly used start station
    """Using mode method to get most common stations"""
    most_used_station_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ')
    print(str(most_used_station_start))

    # display most commonly used end station

    most_used_station_end = df['End Station'].mode()[0]
    print('The most commonly used end station is: ')
    print(str(most_used_station_end))

    # display most frequent combination of start station and end station trip

    most_used_station_pairs = (df['Start Station'] + ' & ' + df['End Station']).mode()[0]
    print('The most used combination of start and end stations is: ')
    print(str(most_used_station_pairs))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    """Sum method to get total travel time in df"""
    total_travel_time = df['Trip Duration'].sum()

    # display mean travel time
    """Mean method to get average travel time in df"""
    mean_travel_time =  df['Trip Duration'].mean()
    
    print("Total travel time of all trips is: ")
    print(total_travel_time)
    print("The average travel time per trip is: ")
    print(mean_travel_time)      
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    """Value Counts method to count number of each type"""
    count_custs = df['User Type'].value_counts().get('Customer', 0)
    count_subs = df['User Type'].value_counts().get('Subscriber', 0)
    
 
    print('The number of users of type Subscriber are: ')
    print(count_subs)
    print('The number of users of type Customer are: ')
    print(count_custs)

    # Display counts of gender
    df['Gender'] = df.get('Gender',)
    """Value counts method to get counts of each value"""
    count_male = df['Gender'].value_counts().get('Male', 0)
    count_female = df['Gender'].value_counts().get('Female', 0)
    """Handling if there is no data in df for this column"""
    if count_male + count_female  == 0:   
        print('There is no gender data for this city.')
    else: 
    # Display counts of gender
        print("The number of males is: ")
        print(count_male)
        print("The number of females is: ")
        print(count_female)


    """Checking for Birth Year Column and creating one with a default value if it doesn't exist"""
    if 'Birth Year' not in df:
        df['Birth Year'] = 0
    
    earliest_birth_year = df['Birth Year'].min()
    latest_birth_year = df['Birth Year'].max()
    most_common_birth_year = df['Birth Year'].mode()
    if earliest_birth_year + latest_birth_year == 0:
        print('There is no birth year data for this city.')
        """Handling the case of no data in this column for a city"""    
    else:  
     # Display earliest, most recent, and most common year of birth    
        print('The earliest birth year is: ')
        print(int(earliest_birth_year))
        print('The most recent birth year is: ')
        print(int(latest_birth_year))
        print('The most common birth year is: ')
        print(int(most_common_birth_year))
    
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data_output(df):
    """Iterating over the data"""
    for start in range(0, len(df), 5):    
        try:
            """Getting input from user and displaying data or ending data display"""
            raw_data_query = input('Would you like to see some raw data?').lower()
            if raw_data_query == 'yes':
                print(df.iloc[start:start + 5])
            elif raw_data_query != 'yes':
                print('Ending data display')
                break
            else:  
                print('No more data to display') 
                break
        except Exception as e:
            print("Exception occurred: {}".format(e))

        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_output(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()