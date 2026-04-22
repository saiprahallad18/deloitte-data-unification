import json

def convertFromFormat1(jsonObject):
    parts = jsonObject["location"].split("/")

    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],
        "location": {
            "country": parts[0],
            "city": parts[1],
            "area": parts[2],
            "factory": parts[3],
            "section": parts[4]
        },
        "data": {
            "status": jsonObject["operationStatus"],
            "temperature": jsonObject["temp"]
        }
    }

from datetime import datetime

def convertFromFormat2(jsonObject):
    # Convert ISO timestamp → milliseconds
    dt = datetime.fromisoformat(jsonObject["timestamp"].replace("Z", "+00:00"))
    timestamp_ms = int(dt.timestamp() * 1000)

    return {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": timestamp_ms,
        "location": {
            "country": jsonObject["country"],
            "city": jsonObject["city"],
            "area": jsonObject["area"],
            "factory": jsonObject["factory"],
            "section": jsonObject["section"]
        },
        "data": {
            "status": jsonObject["data"]["status"],
            "temperature": jsonObject["data"]["temperature"]
        }
    }
    
# Test runner (only for data-1)
def main():
    with open("data-1.json", encoding="utf-8") as f:
        data1 = json.load(f)

    with open("data-2.json", encoding="utf-8") as f:
        data2 = json.load(f)

    with open("data-result.json", encoding="utf-8") as f:
        expected = json.load(f)

    result1 = convertFromFormat1(data1)
    result2 = convertFromFormat2(data2)

    print("Format1 Match:", result1 == expected)
    print("Format2 Match:", result2 == expected)


if __name__ == "__main__":
    main()
    