import os
from alphavantage_mcp_server.server import serve_http

if __name__ == "__main__":
    # Pulls Render's assigned port variable or defaults to 10000
    port = int(os.environ.get("PORT", 10000))
    serve_http(host="0.0.0.0", port=port)
