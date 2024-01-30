#!/usr/bin/python3
"""
Export tasks data for all employees from the JSONPlaceholder API
and save it in a JSON file with the format todo_all_employees.json.
Usage: ./script.py
"""

import json
import requests
from sys import argv


def export_tasks_all_employees():
    # Fetch user data for all employees
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users_data = users_response.json()

    # Prepare the dictionary to store all tasks
    all_tasks_data = {}

    # Iterate through each user and fetch their tasks
    for user in users_data:
        user_id = str(user["id"])
        username = user["username"]

        # Fetch tasks data for the current user ID
        tasks_response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
        tasks_data = tasks_response.json()

        # Prepare the tasks dictionary for the current user
        user_tasks = [{"username": username,
                       "task": task["title"],
                       "completed": task["completed"]} for task in tasks_data]

        # Add tasks to the overall dictionary
        all_tasks_data[user_id] = user_tasks

    # Write to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks_data, json_file)


if __name__ == "__main__":
    export_tasks_all_employees()
