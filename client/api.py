import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000/api"

def analyze_resume(file_bytes, filename):
    try:
        files = {
            "file": (filename, file_bytes)
        }

        response = requests.post(
            f"{BASE_URL}/analyze",
            files=files,
            timeout=60
        )

        print(f"Response Status: {response.status_code}")
        print(f"Response Body: {response.text}")

        if response.status_code == 200:
            result = response.json()
            print(f"Parsed Result: {result}")
            return result
        else:
            error_msg = f"Server returned {response.status_code}: {response.text}"
            print(f"Error: {error_msg}")
            return {"error": error_msg}

    except requests.exceptions.ConnectionError as e:
        error_msg = f"Cannot connect to server at {BASE_URL}. Make sure backend is running."
        print(f"Connection Error: {error_msg}")
        return {"error": error_msg}
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(f"Exception: {error_msg}")
        return {"error": error_msg}