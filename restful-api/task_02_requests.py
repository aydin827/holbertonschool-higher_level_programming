import requests
import csv


def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()

        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        data = response.json()

        clean_data = []

        for post in data:
            clean_data.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()

            for post in clean_data:
                writer.writerow(post)


# test (main fayl kimi işlətmək üçün)
fetch_and_print_posts()
fetch_and_save_posts()
