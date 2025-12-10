from os import getenv, path
import tver_tool
import time
from feedgen.feed import FeedGenerator

home_dir = getenv("HOME")
atomname = "special_main.atom"
atom_path = path.join(home_dir, "server", atomname)

rrr = tver_tool.get_uid_and_token()
platform_uid   = rrr.platform_uid
platform_token = rrr.platform_token

url_1 = "https://service-api.tver.jp/api/v1/callSpecial"

post_header = {
  "x-tver-platform-type": "web"
}

json_data = tver_tool.request_get(url_1, headers=post_header)
iso_time_now  = tver_tool.time_iso()

fg = FeedGenerator()
fg.id("https://tver.jp/")
fg.title("特集")
fg.updated(iso_time_now)
# fg.link("https://tver.jp/")
fg.author({
  "name": "John Doe",
  "email": "john@example.com"
  }
)

contents_1 = json_data['result']['contents']

def get_sp_sub_id(special_id):

  url_2 = f"https://platform-api.tver.jp/service/api/v1/callSpecialContents/{special_id}?platform_uid={platform_uid}&platform_token={platform_token}&require_data=later"

  kkk = tver_tool.request_get(url_2, post_header)
  special_sub_id = kkk['result']['specialContents'][0]['content']['id']
  return special_sub_id

def yyy():
  for item in reversed(contents_1):
    # type               = item['type']
    special_main_id    = item['content']['id']
    special_main_title = item['content']['title']
    special_sub_id     = get_sp_sub_id(special_main_id)
    link               = f"https://tver.jp/specials/{special_main_id}/{special_sub_id}"

    sss = tver_tool.get_description(special_sub_id)
    sss.request_get()

    lb = tver_tool.line_break()
    lb.disable_line_break(sss.data['description'])

    fe = fg.add_entry()
    fe.id(link)
    fe.title(special_main_title)
    fe.updated(iso_time_now)
    fe.content(lb.dis_lb_str)
    fe.link(href=link)


def main():
  yyy()

  atom_xml = fg.atom_str(pretty=True)

  with open(atom_path, "wb") as f:
    f.write(atom_xml)


if __name__ == '__main__':
  start = time.perf_counter()
  main()
  end = time.perf_counter()

  print(f"処理時間: {end - start:.3f} 秒")