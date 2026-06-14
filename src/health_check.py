from src.config import GOOGLE_API_KEY


def run_health_check():
    checks = {
        'google_api_key': bool(GOOGLE_API_KEY)
    }

    return checks
