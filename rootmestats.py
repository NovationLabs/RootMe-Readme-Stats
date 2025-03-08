from flask import Flask, request, render_template, Response
import requests

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def get_rootme_stats():
    username = request.args.get("username")
    if not username:
        return "Error : Please give a valid username in the URL", 400
    
    url = f"https://rootmeapi.vercel.app/api?username={username}"

    datas = requests.get(url).json()
    for key, value in datas.items():
        if value == "Unknown":
            if key == "userName":
                datas[key] = "Not Found"
            elif key == "userPercent":
                datas[key] = "0%"
            else:
                datas[key] = "-"

    svg_content = render_template("rootmestats.html", data=datas)
    return Response(svg_content, mimetype="image/svg+xml")

if __name__ == "__main__":
    app.run(debug=True)
