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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please choose a city: chicago, new york city, washington? ')
    valid_cities = ['chicago', 'new york city', 'washington']

    while city.lower() not in valid_cities:
        city = input('Invalid inputs. Please enter a city:\nchicago, new york city, washington. ')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Would you like to filter the data by a month or not at all? \nEnter "month" or "all". ')
    valid_months = ['month', 'all']
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    while month.lower() not in valid_months:
        month = input('Invalid inputs, please try again: month or all. ')

    if month.lower() != 'all':
        month = input('Please choose a month\njanuary, february, march, april, may, june: ')
        while month.lower() not in months:
            month = input('Invalid inputs, Please enter a valid month\njanuary, february, march, april, may, june: ')
    else:
        month = 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Would you like to choose to filter data by day? \nEnter "day" for filtering or "all" for no day filter. ')
    valid_days = ['all', 'day']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    while day.lower() not in valid_days:
        day = input('Invalid inputs, Please enter "day" or "all". ')

    if day.lower() != 'all':
        day = input('Please choose a day:\nmonday, tuesday, wednesday, thursday, friday, saturday, sunday: ')
        while day.lower() not in days:
            day = input('Invalid inputs, Please enter a day\nmonday, tuesday, wednesday, thursday, friday, saturday, sunday: ')
    else:
        day = 'all'

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
    df = pd.read_csv(CITY_DATA[city.lower()])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour


    if month.lower() != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1


    if day.lower() != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day.lower()) + 1


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month is: ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day is: ', popular_day)


    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_s_station = df['Start Station'].mode()[0]
    print('Most commonly used start station is: ', popular_s_station)

    # TO DO: display most commonly used end station
    popular_e_station = df['End Station'].mode()[0]
    print('Most commonly used end station is: ', popular_e_station)

    # TO DO: display most frequent combination of start station and end station trip
    group_stations = df.groupby(['Start Station','End Station'])
    popular_compination_station = group_stations.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of start station and end station trip is: ', popular_compination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is: ', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time: ', mean_travel_time)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if city.lower() != 'washington':
        counts_gender = df['Gender'].value_counts()
        print('Gender stats: ', counts_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_birth = df['Birth Year'].min()
        print('Earliest Year: ', earliest_year_birth)

        recent_year_birth = df['Birth Year'].max()
        print('Recent year of birth is: ', recent_year_birth)

        common_year_birth = df['Birth Year'].mode()[0]
        print('Most common year of birth is: ', common_year_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def table_show(df):
    """Displays data table on bikeshare users."""

    print('\nShowing Data Table...\n')
    start_time = time.time()

    check_data = input('Would you like to check the data table? Enter yes or no. ').lower()
    acc_ans = ['yes', 'no']
    index = df.index
    total_rows = len(index)

    while check_data not in acc_ans:
        check_data = input('Invalid inputs, please try again: Enter yes or no. ').lower()

    if check_data == 'yes':
        first_rows = 5
        print(df.head(first_rows))

        while first_rows <= total_rows:
            more_data = input('Do you need to check more data? Enter yes or no. ').lower()
            if more_data == 'yes':
                first_rows += 5
                print(df.head(first_rows))
            else:
                break

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        table_show(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
