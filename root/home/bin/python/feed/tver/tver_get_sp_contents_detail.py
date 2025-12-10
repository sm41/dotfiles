from os import getenv, path
import tver_tool
import sys
from feedgen.feed import FeedGenerator

rrr = tver_tool.get_uid_and_token()
platform_uid   = rrr.platform_uid
platform_token = rrr.platform_token

# special_sub_id = sys.argv[1]
special_sub_id = "all25_1129"
url = f"https://platform-api.tver.jp/service/api/v1/callSpecialContentsDetail/{special_sub_id}?platform_uid={platform_uid}&platform_token={platform_token}&sort_key=recommend&require_data=mylist%2Clater"

post_header = {
  "x-tver-platform-type": "web"
}

json_data = tver_tool.request_get(url, headers=post_header)
iso_time_now  = tver_tool.time_iso()

json_content  = json_data['result']['contents']['content']
sp_main_id    = json_content['specialMainID']
sp_main_title = json_content['specialMainTitle']
list          = json_content['contents']

fg = FeedGenerator()
fg.id("https://tver.jp/")
fg.title(sp_main_title)
fg.updated(iso_time_now)
# fg.link("https://tver.jp/")
# fg.link(href="https://tver.jp/")
fg.author({
  "name": "John Doe",
  "email": "john@example.com"
  }
)

for iii in reversed(list):
  series_title = iii['content']['title']
  series_id    = iii['content']['id']

  sss = tver_tool.get_description(series_id)
  sss.request_get()

  lb = tver_tool.line_break()
  lb.disable_line_break(sss.data['description'])

  fe = fg.add_entry()
  fe.id(f"https://tver.jp/series/{series_id}")
  fe.title(series_title)
  fe.updated(iso_time_now)
  fe.content(lb.dis_lb_str)
  fe.link(href=f"https://tver.jp/series/{series_id}")
# f"https://image-cdn.tver.jp/images/content/thumbnail/series/xlarge/{series_id}.jpg"

atom_xml = fg.atom_str(pretty=True)

home_dir  = getenv("HOME")
atomname  = f"sp_[{sp_main_id}]_[{special_sub_id}].atom"
atom_path = path.join(home_dir, "server", atomname)

with open(atom_path, "wb") as f:
    f.write(atom_xml)