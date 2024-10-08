#!/usr/bin/env python3
import requests
import csv

def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(r.status_code)
    if r.status_code == 200:
        response_json = r.json()
        for post in response_json:
            print(post['title'])

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        response_json = r.json()
        with open('posts.csv', mode='w', encoding='utf-8', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()         
            for post in response_json:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})
