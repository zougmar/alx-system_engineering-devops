Ö#!/usr/bin/python3
""" This script consumes API to retrieve todos by user id and exports data to json"""
from collections import OrderedDict
import json
import requests

if __name__ == '__main__':
    """ get user id by argv use HTTP GET method """
    url_user = 'https://jsonplaceholder.typicode.com/users'
    res_user = requests.get(url_user)
    users = res_user.json()
    result = {}
    for user in users:
        username = user['username']
        user_id = user['id']
        list_tasks = []
        todo_params = {'userId': user_id}
        url_todo = 'https://jsonplaceholder.typicode.com/todos'
        res_todo = requests.get(url_todo, params=todo_params)
        todos = res_todo.json()
        for todo in todos:
            dict_task = {
                'task': todo['title'],
                'completed': todo['completed'],
                'username': username}
            list_tasks.append(OrderedDict(dict_task))
            result[user_id] = list_tasks
    with open('todo_all_employees.json', 'w') as f:
        f.write(json.dumps(result))

