"""
Placeholder for the train API client.
"""

def get_train_service(service_id: str) -> dict:
    """
    Returns a hardcoded, sample train data structure for the given service ID.
    """
    return {
        "service_id": "C12345",
        "std": "06:36",
        "etd": "On time",
        "origin": "Kettering",
        "destination": "St Pancras"
    }
