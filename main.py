import requests
import re
import json
import csv
import datetime
from typing import Any
def extract_param_from_html(html_content):
    """
    Extract the required parameter from the HTML content.
    Adjust the regular expression based on the actual HTML structure.
    """
    # Example regex pattern, adjust it to match the actual parameter in the HTML
    param_pattern = re.compile(r'param: "(.*?)"')
    match = param_pattern.search(html_content)
    if match:
        return match.group(1)
    else:
        return None

def get_html_content():
    """
    Perform a GET request to www.bonbast.com and return the HTML content.
    """
    get_url = "https://www.bonbast.com/"
    get_headers = {
        # Headers for the GET request
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Cookie": "cookieconsent_status=true; _ga=GA1.1.2026230781.1676205230; _ga_PZF6SDPF22=GS1.1.1677480963.5.1.1677483135.0.0.0; st_bb=0",
        "Dnt": "1",
        "Referer": "https://www.bonbast.com/",
        "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"macOS\"",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(get_url, headers=get_headers)
    if response.status_code == 200:
        return response.text
    else:
        return None

def post_data_with_param(param):
    """
    Perform a POST request to www.bonbast.com/json with the extracted parameter.
    """
    post_url = "https://www.bonbast.com/json"
    post_headers = {
           "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "cookieconsent_status=true; _ga=GA1.1.2026230781.1676205230; _ga_PZF6SDPF22=GS1.1.1677480963.5.1.1677483135.0.0.0; st_bb=0",
    "Dnt": "1",
    "Origin": "https://www.bonbast.com",
    "Referer": "https://www.bonbast.com/",
    "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }
    post_data = {
        "param": param
    }
    response = requests.post(post_url, headers=post_headers, data=post_data)
    if response.status_code == 200:
        # Get current datetime
        now = datetime.datetime.now()
        date_time = now.strftime("%m-%d-%Y_%H-%M-%S")

    # Save to CSV
        with open(f'{date_time}.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(response.text)

    # Save to JSON
        with open(f'{date_time}.json', 'w') as file:
            json.dump(response.text, file)
            print("Response Content:", response.text)
    
    else:
        print("Failed to send POST request")
def loopp():
    html_content = get_html_content()
    if html_content:
        param_value = extract_param_from_html(html_content)
        if param_value:
        post_data_with_param(param_value)
        else:
        print("Failed to extract parameter from HTML content")
    else:
        print("Failed to retrieve HTML content")
        loopp()
# Main execution flow

loopp()
