import func, analyse
from plyer import notification

def main():

  method    = analyse.website()
  yaml_path = func.get_yaml_path()
  newest_list = []

  site_method = func.get_function_names(method)
  sorted_site = sorted(site_method)

  for method_name in sorted_site:
    func.generate_method(method, method_name)

    newest_state = {
      method_name: {
        "website": method.website,
        "url"    : method.url,
        "article": method.article,
        "page"   : method.page
      }
    }

    dict_of_local = func.isexist_dict(method_name, yaml_path)

    if   dict_of_local is None:
      newest_list.append(newest_state)

    elif dict_of_local[method_name] != newest_state[method_name]:
      newest_list.append(newest_state)
      notification.notify(title = f"✅ {method.website}", message = method.url)

    elif dict_of_local[method_name] == newest_state[method_name]:
      newest_list.append(dict_of_local)

  func.rewrite_dict(yaml_path, newest_list)

