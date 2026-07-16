import os
from alphavantage_mcp.server import serve_http

if __name__ == "__main__":
    # Forces the server to bind globally to 0.0.0.0 using Render's assigned port variable
    port = int(os.environ.get("PORT", 10000))
    serve_http(host="0.0.0.0", port=port)
