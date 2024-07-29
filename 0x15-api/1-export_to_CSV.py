#!/usr/bin/python3
""" This script consumes API to retrieve todos by user id and exports data to csv"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    """ get user id by argv use HTTP GET method """
    user_id = argv[1]
    todo_params = {'userId': user_id}
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    res_todo = requests.get(url_todo, params=todo_params)
    todos = res_todo.json()
    user_params = {'id': user_id}
    url_user = 'https://jsonplaceholder.typicode.com/users'
    res_user = requests.get(url_user, params=user_params)
    user = res_user.json()[0]
    username = user['username']
    list_rows = []
    for todo in todos:
        row = list([user_id, username, str(todo['completed']), todo['title']])
        list_rows.append(row)
    with open('{}.csv'.format(user_id), 'wt') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writerows(list_rows)

