import time
import pandas as pd
import numpy as np
import datetime

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
    while True:
        city = input('Select a city to explore the bike share data. Chicago, New York City, or Washington?\n').lower()
        if city in CITY_DATA.keys():
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Specify the month of data to explore. All, January ,February, March, April, May, or June?\n').lower()
        if month in ['all', 'january', 'february', 'march','april', 'may', 'june']:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Specify the day of data to explore. All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday?\n').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday']:
            break

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

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
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

    # TO DO: display the most common month
    print('\nMost Common Month of Travel:')
    print(df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('\nMost Common Day of Travel:')
    print(df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('\nMost Common Start Hour of Travel:')
    print(df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nMost Common Start Station:')
    print(df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('\nMost Common End Station:')
    print(df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost Frequency Start & Stop Combination')
    print(df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal Travel Time:')
    print(datetime.timedelta(seconds=int(df['Trip Duration'].sum())))

    # TO DO: display mean travel time
    print('\nMean Travel Time:')
    print(datetime.timedelta(seconds=int(df['Trip Duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of User Types:')
    print(df['User Type'].value_counts())
        

    # TO DO: Display counts of gender
    print('\nCounts of Genders:')
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())
    else:
        print('No Gender Data')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nEarliest, Latest & Most Common Date of Birth:')
        print('Earliest: {}\nLatest: {}\nMost Common: {}'.format(df['Birth Year'].min(), df['Birth Year'].max(),df['Birth Year'].mode()[0]))
    else:
        print('No Birth Year Data')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """
    Display contents of the CSV file to the display as requested by
    the user.
    """

    start_loc = 0
    end_loc = 5
    display = input("Do you want to see the raw data?: ").lower()
    
    if display == 'yes':
        while end_loc <= df.shape[0] - 1:
            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5
            end_display = input("Do you wish to continue?: ").lower()
            if end_display == 'no':
                break
                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
