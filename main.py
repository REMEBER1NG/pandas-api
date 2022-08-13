"""
If you have any suggestions of how i could make
the code cleaner, please hit me up because i want
to improve, also if you want me to make you a customized
version of this program don't be afraid to email me: 
> lonelyrl@protonmail.com - thank you: enjoy :)
"""

import httpx
import pandas as pd

# api to be requested
website = 'https://randomuser.me/api/'

# the number of requests to be made
requests = 5

users = []
usernames = []
emails = []
genders = []


def request(api: str) -> dict:
    """makes a requests to the passed website"""
    with httpx.Client() as client:
        # open a requests session
        try:
            r = client.get(api)        
        except httpx.ConnectError:
            print('unable to connect!')
    return r.json()


def get_data() -> None:
    """this methods parses the request data"""
    for _ in range(requests):
        users.append(request(website))
    for user in users:
        fullnames = user['results'][0]['name']['first'] + ' ' + user['results'][0]['name']['last']
        usernames.append(fullnames)
        emails.append(user['results'][0]['email'])
        genders.append(user['results'][0]['gender'])
    export()


def export() -> None:
    """method to organize all data into a '.csv' file"""
    columns = {'name': usernames, 'email': emails, 
        'gender': genders}
    dataframe = pd.DataFrame(columns)
    # save data to a csv file @ .\data\user_info.csv
    dataframe.to_csv('data/user_info.csv')
    # print(dataframe) uncomment this is if you want to print the data
    print('done')


if __name__ == '__main__':
    get_data()
