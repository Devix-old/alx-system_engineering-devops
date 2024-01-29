#!/usr/bin/python3
"""
Fetch user and task data from JSONPlaceholder API and print completed task info
Usage: python script_name.py <user_id>
"""

import json
import sys
import urllib.request


def get_user_name(user_data, user_id):
    """Get user name based on ID."""
    for user in user_data:
        if user["id"] == user_id:
            return user["name"]
    return None


def get_tasks(todo_data, user_id):
    """Get completed task information for a user."""
    tasks = {"completed": 0, "total_tasks": 0}
    for todo in todo_data:
        if todo["userId"] == user_id:
            tasks["total_tasks"] += 1
            if todo["completed"]:
                tasks["completed"] += 1
    return tasks


def print_completed_tasks(todo_data, user_id):
    """Print titles of completed tasks for a user."""
    for todo in todo_data:
        if todo["userId"] == user_id and todo["completed"]:
            print("\t " + todo["title"])


if __name__ == "__main__":
    user_id = int(sys.argv[1])

    # Fetch data from the API
    todos_data = urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/todos").read()
    users_data = urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users").read()

    # Parse JSON data
    todos = json.loads(todos_data.decode("utf-8"))
    users = json.loads(users_data.decode("utf-8"))

    # Get user name
    user_name = get_user_name(users, user_id)

    if user_name is not None:
        # Get tasks information
        tasks_info = get_tasks(todos, user_id)
        completed_tasks = tasks_info["completed"]
        total_tasks = tasks_info["total_tasks"]

        # Print the result
        print("Employee {} is done with tasks({}/{}):".format(
            user_name, completed_tasks, total_tasks))
        print_completed_tasks(todos, user_id)
