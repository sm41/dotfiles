from os import getenv, path
import tver_tool
import time
from feedgen.feed import FeedGenerator

rrr = tver_tool.get_uid_and_token()
platform_uid   = rrr.platform_uid
platform_token = rrr.platform_token

series_id="srm706pd6g"
url_1 = f"https://platform-api.tver.jp/service/api/v1/callSeriesSeasons/{series_id}?platform_uid={platform_uid}&platform_token={platform_token}&require_data=later"

post_header = {
  "x-tver-platform-type": "web"
}

json_data_1 = tver_tool.request_get(url_1, headers=post_header)

season_id = json_data_1['result']['contents'][0]['content']['id']
url_2 = f"https://platform-api.tver.jp/service/api/v1/callSeasonEpisodes/{season_id}?platform_uid={platform_uid}&platform_token={platform_token}&require_data=later"

json_data_2 = tver_tool.request_get(url_2, headers=post_header)
iso_time_now    = tver_tool.time_iso()

title = json_data_2['result']['contents'][0]['content']['seriesTitle']


fg = FeedGenerator()
fg.id("https://tver.jp/")
fg.title(title)
fg.updated(iso_time_now)
# fg.link("https://tver.jp/")
fg.author({
  "name": "John Doe",
  "email": "john@example.com"
  }
)

contents = json_data_2['result']['contents']

for item in reversed(contents):

  episode_id    = item['content']['id']
  episode_title = item['content']['title']

  if not episode_id.startswith("ep"):
    continue

  eee = tver_tool.get_description(episode_id)
  eee.request_get()

  lb = tver_tool.line_break()
  lb.disable_line_break(eee.data['description'])
  ert = lb.dis_lb_str

  fe = fg.add_entry()
  fe.id(f"https://tver.jp/episodes/{episode_id}")
  fe.title(episode_title)
  fe.updated(iso_time_now)
  fe.content(ert)
  fe.link(href=f"https://tver.jp/episodes/{episode_id}")

atom_xml = fg.atom_str(pretty=True)

home_dir  = getenv("HOME")
atomname  = f"sr_[{series_id}]_[{season_id}].atom"
atom_path = path.join(home_dir, "server", atomname)

with open(atom_path, "wb") as f:
  f.write(atom_xml)
