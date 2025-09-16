import func, analyse
from plyer import notification
from sys import exit

def main():

  method  = analyse.hoge()
  yaml_path = func.get_yaml_path()
  newest_list = []

  # analyse.py の中のメソッド名を取得して、ソート
  site_method = func.get_function_names(method)
  sorted_site = sorted(site_method)

  # それぞれのメソッドを実行して、情報を取得
  for method_name in sorted_site:
    func.generate_method(method, method_name)

    func.check_status(method.url)


    newest_state = {
      method_name: {
        "website": method.website,
        "url"    : method.url,
        "article": method.article,
        "page"   : method.page
      }
    }

    # state.yamlが存在しなければ新規作成
    # 存在していたら、内容を読み込んで、現在の状態と比較
    dict_of_local = func.isexist_dict(method_name, yaml_path)

    if   dict_of_local is None:
      newest_list.append(newest_state)

    elif dict_of_local[method_name] != newest_state[method_name]:
      newest_list.append(newest_state)
      notification.notify(title = f"✅ {method.website}", message = method.url)

    elif dict_of_local[method_name] == newest_state[method_name]:
      newest_list.append(dict_of_local)

  func.rewrite_dict(yaml_path, newest_list)

