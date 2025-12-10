from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from os      import getenv, path
import re
import time
import tver_tool
from feedgen.feed import FeedGenerator

url = "https://service-api.tver.jp/api/v1/callNewerDetail/drama"

headers = {
  "x-tver-platform-type": "web"
}

data = tver_tool.request_get(url, headers)
iso_time_now = tver_tool.time_iso()

fg = FeedGenerator()
fg.id("https://tver.jp/")
fg.title("新着/ドラマ")
fg.updated(iso_time_now)
# fg.link("https://tver.jp/")
fg.author({
  "name": "John Doe",
  "email": "john@example.com"
  }
)

contents = data['result']['contents']['contents']

def check_conditions(item):
  c = item['content']

  return {
    "ribbon"  : (c['ribbonID'] != 0),
    "bs"      : bool(re.match('(BS|ＢＳ)', c['productionProviderName'])),
    "year"    : bool(re.match('[0-9]{4}年', c['broadcastDateLabel'])),
    "ck"      : bool(re.match('(中国|.?韓)', c['seriesTitle'])),
    "comment" : bool(re.search('解説放送', c['title'])),
  }


def call_new():
  month_day_items = []
  blocked_items  = []
  year_items   = []

  for item in reversed(contents):

    conds = check_conditions(item)  # ← 全部の True/False を取る

    if conds['ck'] or conds['bs'] or conds['ribbon'] or conds['comment']:
        blocked_items.append({
            "item": item,
            "conditions": conds,
        })
        continue

    if conds['year']:
      year_items.append({
        "item": item,
        "conditions": conds,
      })

    if not conds['year']:
        month_day_items.append({
            "item": item,
            "conditions": conds,
        })

    # else:
    #     month_day_items.append({
    #         "item": item,
    #         "conditions": conds,
    #     })

  return blocked_items, month_day_items, year_items


def process_items(lilili:list):

  home_dir  = getenv("HOME")

  for ddd in lilili:

    for key, value in ddd.items():

      for item in value:
        # print(item)
        series_title             = item['item']['content']['seriesTitle']
        series_id                = item['item']['content']['seriesID']
        # episode_title            = item['item']['content']['title']
        episode_id               = item['item']['content']['id']
        # broadcast_date           = item['item']['content']['broadcastDateLabel']
        # production_provider_name = item['item']['content']['productionProviderName']
        # ribbon_id                = item['item']['content']['ribbonID']
        start_at                 = datetime.fromtimestamp(item['item']['startAt'], ZoneInfo("Asia/Tokyo")).isoformat()
        # end_at                   = datetime.fromtimestamp(item['item']['endAt'], ZoneInfo("Asia/Tokyo")).isoformat()

        sss = tver_tool.get_description(series_id)
        sss.request_get()

        eee = tver_tool.get_description(episode_id)
        eee.request_get()

        lb = tver_tool.line_break()
        # lb.disable_line_break(sss.data['description'])
        # sdf = lb.dis_lb_str

        lb.disable_line_break(eee.data['description'])
        ert = lb.dis_lb_str

        fe = fg.add_entry()
        fe.id(f"https://tver.jp/episodes/{episode_id}")
        fe.title(series_title)
        fe.updated(start_at)
        fe.content(ert)
        fe.link(href=f"https://tver.jp/episodes/{episode_id}")

      atom_xml = fg.atom_str(pretty=True)

      atomname  = f"new_[{key}].atom"
      atom_path = path.join(home_dir, "server", atomname)
      # print(atom_path)

      with open(atom_path, "wb") as f:
        f.write(atom_xml)


# print("=== month_day_items データ ===")
# for x in month_day_items:
#     print(f"https://tver.jp/episodes/{x['item']['content']['id']}", x["item"]["content"]["broadcastDateLabel"], x["conditions"], x["item"]["content"]['seriesTitle'])


# print("=== year_items データ ===")
# for x in year_items:
#     print(f"https://tver.jp/episodes/{x['item']['content']['id']}", x["item"]["content"]["broadcastDateLabel"], x["conditions"], x["item"]["content"]['seriesTitle'])

# print("=== blocked_items データ ===")
# for x in blocked_items:
#     print(f"https://tver.jp/episodes/{x['item']['content']['id']}", x["item"]["content"]["broadcastDateLabel"], x["conditions"], x["item"]["content"]['seriesTitle'])


def main():
  blocked_items, month_day_items, year_items = call_new()

  ready = [
    {"month_day_items" : month_day_items},
    {"year_items" : year_items}
  ]

  process_items(ready)



if __name__ == '__main__':
  # start = time.perf_counter()
  main()
  # end = time.perf_counter()

  # print(f"処理時間: {end - start:.3f} 秒")