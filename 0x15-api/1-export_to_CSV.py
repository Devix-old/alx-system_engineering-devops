#!/usr/bin/python3
"""
Fetch user and task data from JSONPlaceholder API and print completed task info
Usage: python script_name.py <user_id>
"""
import csv
import requests as r
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = r.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = r.get(url + "todos/", params={"userId": user_id}).json()
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        w = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [w.writerow([user_id, username, todo.get("completed"),
                     todo.get("title")])for todo in todos]
