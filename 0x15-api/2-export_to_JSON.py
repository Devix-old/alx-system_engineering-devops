#!/usr/bin/python3
"""
Export tasks data for a given USER_ID from JSONPlaceholder API
and save it in a JSON file with the format USER_ID.json.
Usage: ./script.py USER_ID
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} USER_ID".format(argv[0]))
    else:
        user_id = argv[1]

        # Fetch user data
        user_response = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{user_id}')
        user_data = user_response.json()

        # Fetch tasks data for the given user ID
        tasks_response = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
        tasks_data = tasks_response.json()

        # Prepare the JSON structure
        json_data = {
            user_id: [
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": user_data["username"]
                } for task in tasks_data
            ]
        }

        # Write to JSON file
        with open(f'{user_id}.json', 'w') as json_file:
            json.dump(json_data, json_file)
