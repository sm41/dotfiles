import json
import urllib.request


def main():
    OWNER = "OWNER"
    REPO = "REPO"
    WORKFLOW = "deploy.yml"
    TOKEN = "YOUR_TOKEN"

    url  = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/workflows/{WORKFLOW}/dispatches"
    data = { "ref": "main" }

    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req) as res:
            print(res.status)  # 成功なら204
    except urllib.error.HTTPError as e:
        print("HTTP Error:", e.code)
        print(e.read().decode())