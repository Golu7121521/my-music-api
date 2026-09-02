from fastapi import FastAPI
from ytmusicapi import YTMusic

app = FastAPI()
yt = YTMusic()

@app.get("/")
def read_root():
    return {"status": "success", "message": "My Custom YT Music API is Running! 🚀"}

@app.get("/api/search")
def search_songs(query: str = "Arijit"):
    return {"status": "success", "query_received": query}

# Ye route hame batayega ki server par kaun-kaun se URL active hain
@app.get("/debug/routes")
def get_routes():
    routes = []
    for route in app.routes:
        routes.append({"path": route.path, "name": route.name})
    return {"status": "success", "routes": routes}
