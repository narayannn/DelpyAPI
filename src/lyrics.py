import requests


def lyrics(query):
    try:
        url = f"https://lrclib.net/api/search?q={query}"
        response = requests.get(url)
        data = response.json()

        plain = data[0]["plainLyrics"] or ""
        synced = data[0]["syncedLyrics"] or ""
        artist = data[0]["artistName"] or ""
        track = data[0]["trackName"] or ""

        return {
            "status": "success",
            "status_code": response.status_code,
            "artist": artist,
            "track_name": track,
            "lyrics": [{"plain": plain, "synced": synced}],
        }

    except requests.exceptions.HTTPError as http_err:
        return {
            "status": "faild",
            "error": http_err 
        }
    except requests.exceptions.Timeout:
        return {
            "status": "faild",
            "error": "the request timed out" 
        }
    except requests.exceptions.RequestException as err:
        return {
            "status": "faild",
            "error": err
        }

