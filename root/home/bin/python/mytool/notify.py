from plyer import notification

def ntfy(result, text):
  if result.returncode == 0:
    notification.notify(title = "✅ Success", message = text)
  else:
    notification.notify(title = "⚠️ failed", message = text)