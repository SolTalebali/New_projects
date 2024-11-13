websites = ["mimo.com", "coding.com", "food.org"]
def add_https(site):
  without_https = [website for website in websites if "https" not in website.split(":")]
  auto_add = []
  for webs in without_https:
    auto_add.append("https://"+webs)
  print(auto_add)

add_https(websites)