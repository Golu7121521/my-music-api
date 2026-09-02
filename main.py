from fastapi import FastAPI
from ytmusicapi import YTMusic

app = FastAPI()
yt = YTMusic()

@app.get("/")
def read_root():
    return {"status": "success", "message": "My Custom YT Music API is Running! 🚀"}

# 1. Search API (Gaane search karne ke liye)
@app.get("/api/search")
def search_songs(query: str):
    try:
        # filter="songs" taaki sirf gaane aayein, videos nahi
        results = yt.search(query=query, filter="songs", limit=15)
        
        # Data ko thoda clean format mein Android ke liye bhejna
        clean_results = []
        for item in results:
            clean_results.append({
                "videoId": item.get("videoId"),
                "title": item.get("title"),
                "artist": item["artists"][0]["name"] if item.get("artists") else "Unknown",
                "thumbnail": item["thumbnails"][-1]["url"] if item.get("thumbnails") else "",
            })
        return {"status": "success", "data": clean_results}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# 2. Trending API (Home screen banner ke liye)
@app.get("/api/trending")
def get_trending():
    try:
        # India (IN) ke top charts nikalna
        charts = yt.get_charts(country='IN')
        trending_songs = charts.get('trending', {}).get('items', [])
        
        clean_trending = []
        for item in trending_songs:
            clean_trending.append({
                "videoId": item.get("videoId"),
                "title": item.get("title"),
                "artist": item["artists"][0]["name"] if item.get("artists") else "Unknown",
                "thumbnail": item["thumbnails"][-1]["url"] if item.get("thumbnails") else "",
            })
        return {"status": "success", "data": clean_trending}
    except Exception as e:
        return {"status": "error", "message": str(e)}

