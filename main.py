from fastapi import FastAPI
from ytmusicapi import YTMusic

app = FastAPI()
yt = YTMusic()

@app.get("/")
def read_root():
    return {"status": "success", "message": "My Custom YT Music API is Running! 🚀"}

@app.get("/api/search")
def search_songs(query: str):
    try:
        results = yt.search(query=query, filter="songs", limit=15)
        
        # Agar YouTube khali list bhejta hai
        if not results:
            return {"status": "empty", "message": "YouTube Music returned no results for this query."}
            
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
        # Agar YouTube API ki taraf se koi block ya crash hua, toh yahan exact error dikhega
        return {"status": "error", "message": str(e)}
