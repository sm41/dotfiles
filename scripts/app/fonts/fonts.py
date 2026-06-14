import json
import os
from urllib import request, parse


font = {
    # "Noto" : {
    #     "Noto_Sans"     : "https://github.com/google/fonts/tree/main/ofl/notosans",
    #     "Noto_Sans_JP"  : "https://github.com/google/fonts/tree/main/ofl/notosansjp",
    #     "Noto_Serif"    : "https://github.com/google/fonts/tree/main/ofl/notoserif",
    #     "Noto_Serif_JP" : "https://github.com/google/fonts/tree/main/ofl/notoserifjp",
    #     "Noto_Sans_Mono": "https://github.com/google/fonts/tree/main/ofl/notosansmono",
    # },

    "Roboto" : {
    #     "Roboto"      : "https://github.com/google/fonts/tree/main/ofl/roboto",
        "Roboto_Flex" : "https://github.com/google/fonts/tree/main/ofl/robotoflex",
    #     "Roboto_Mono" : "https://github.com/google/fonts/tree/main/ofl/robotomono",
    #     "Roboto_Serif": "https://github.com/google/fonts/tree/main/ofl/robotoserif",
    #     "Roboto_Slab" : "https://github.com/google/fonts/tree/main/apache/robotoslab",
    },

    # "JetBrains" : {
    #     "JetBrainsMono" : "https://github.com/JetBrains/JetBrainsMono/tree/master/fonts/variable"
    # }
}


def api_parser(url:str):
    parts     = parse.urlparse(url)
    domain    = parts.netloc
    hoge:list = parts.path.strip("/").split("/")

    owner  = hoge[0]
    repo   = hoge[1]
    # tree   = hoge[2]
    # branch = hoge[3]
    path   = "/".join(hoge[4:])

    header = {
        "User-Agent" : "python-urllib",
        "Accept"     : "application/vnd.github.v3+json"
    }

    req = request.Request(f"https://api.{domain}/repos/{owner}/{repo}/contents/{path}", headers=header)
    with request.urlopen(req) as response:
        return json.load(response)


def main():

    suffix = (".ttf", ".otf")

    download_base = os.getenv("XDG_DATA_HOME")
    download_dir  = "fonts"

    for vvv in font.values():
        for directry, repository in vvv.items():

            print(f"📦 {directry}")
            download_path = os.path.join(download_base, download_dir, directry)

            for meta_data in api_parser(repository):
                cond = [
                    meta_data['type'] == "file",
                    meta_data['name'].endswith(suffix)
                ]

                if all(cond):
                    os.makedirs(download_path, exist_ok=True)
                    file_path      = os.path.join(download_path, meta_data['name'])
                    contained_font = os.listdir(download_path)
                    # print(f"✅ {file_path}")

                    if meta_data['name'] in contained_font:
                        print(f"✴️  Already Downloaded {file_path}")
                    else:
                        with request.urlopen(meta_data['download_url']) as content:
                            with open(file_path, "wb") as f:
                                f.write(content.read())
                        print(f"💎  New Download {file_path}")


if __name__ == '__main__':
    main()