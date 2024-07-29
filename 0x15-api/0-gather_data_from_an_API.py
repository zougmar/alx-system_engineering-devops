#!/usr/bin/python3
""" This script consumes API to retrieve todos by user ID """
import requests
from sys import argv

if __name__ == '__main__':
    """ Get user ID from command line arguments and use HTTP GET method """
    user_id = argv[1]
    todo_params = {'userId': user_id}
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    todo_response = requests.get(todo_url, params=todo_params)
    todo_data = todo_response.json()
    
    completed_count = 0
    completed_todos = []
    
    for todo in todo_data:
        if todo['completed']:
            completed_todos.append(todo['title'])
            completed_count += 1
    
    user_params = {'id': user_id}
    user_url = 'https://jsonplaceholder.typicode.com/users'
    user_response = requests.get(user_url, params=user_params)
    user_data = user_response.json()[0]
    user_name = user_data['name']
    
    print("Employee {} is done with tasks({}/{}):".format(user_name, completed_count, len(todo_data)))
    for title in completed_todos:
        print('\t {}'.format(title))

