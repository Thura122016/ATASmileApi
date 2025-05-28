from ATAConfig import *
import hashlib
import time
import requests

def send_json_request(url: str, payload: dict) -> dict:
    print(url,payload)
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
    }
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
    return response.json()

def create_fullUrl(apiKey: str,region: str = "global") -> str:
    if region == "global":
        return SMILE_URL+SMILE_API.get(apiKey)
    else:
        return SMILE_URL+"/"+region+SMILE_API.get(apiKey)

def create_fullData(postData: dict) -> dict:
    postData["time"] = str(int(time.time()))
    postData["email"] = SMILE_EMAIL
    postData["uid"] = SMILE_UID
    postData["sign"] = encrypted_sign(postData)
    return postData

def encrypted_sign(postData: dict) -> str:
    sorted_data = dict(sorted(postData.items()))
    query_str = '&'.join(f"{k}={v}" for k, v in sorted_data.items())
    query_str += '&' + SMILE_KEY
    return hashlib.md5(hashlib.md5(query_str.encode()).hexdigest().encode()).hexdigest()