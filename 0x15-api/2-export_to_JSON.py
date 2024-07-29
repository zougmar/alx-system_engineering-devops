#!/usr/bin/python3
""" This script consumes API to retrieve todos by user id and exports data to json"""
from collections import OrderedDict
import json
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
    list_tasks = []
    for todo in todos:
        dict_task = {
            'task': todo['title'],
            'completed': todo['completed'],
            'username': username}
        list_tasks.append(OrderedDict(dict_task))
    result = {user_id: list_tasks}
    with open('{}.json'.format(user_id), 'w') as f:
        f.write(json.dumps(result))

