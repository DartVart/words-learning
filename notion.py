import json
from copy import deepcopy

import requests

TITLE = "Words Learning"


def get_headers(token):
    return {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2022-02-22"
    }


def bolded_to_rich_text(text):
    rich_text = []
    item_template = {
        "type": "text",
        "text": {
            "content": "",
        },
        "annotations": {
            "bold": False,
        },
    }
    for i, text_part in enumerate(text.split('**')):
        new_item = deepcopy(item_template)
        new_item["text"]["content"] = text_part
        if i % 2 == 1:
            new_item["annotations"]["bold"] = True
        rich_text.append(new_item)
    return rich_text


def get_page_id(date, database_id, token):
    read_url = f"https://api.notion.com/v1/databases/{database_id}/query"
    res = requests.request("POST", read_url, headers=get_headers(token))
    data = res.json()
    pages = data["results"]
    try:
        page = next(
            p for p in pages if
            (p["properties"]["Date"]["date"]["start"] == date and
             p["properties"]["Name"]["title"][0]["text"]["content"] == TITLE)
        )
        return page["id"]
    except StopIteration:
        return None


def create_page(date, database_id, token):
    create_url = 'https://api.notion.com/v1/pages'
    new_page_data = {
        "parent": {"database_id": database_id},
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": TITLE
                        }
                    }
                ]
            },
            "Date": {
                "date": {
                    "start": date,
                }
            },
        }
    }
    data = json.dumps(new_page_data)
    res = requests.request("POST", create_url, headers=get_headers(token), data=data)
    return res.json()["id"]


def add_sentence(sentence, datetime_obj, database_id, token):
    date = datetime_obj.strftime('%Y-%m-%d')
    page_id = get_page_id(date, database_id, token)
    if page_id is None:
        page_id = create_page(date, database_id, token)

    update_url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    new_block = {
        "children": [
            {
                "object": "block",
                "type": "numbered_list_item",
                "numbered_list_item": {
                    "rich_text": bolded_to_rich_text(sentence),
                }
            }
        ]
    }
    data = json.dumps(new_block)
    return requests.request("PATCH", update_url, headers=get_headers(token), data=data)
