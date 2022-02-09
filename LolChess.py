import requests
from bs4 import BeautifulSoup

class LolChessPage:
  def __init__(self, user):
    self.username = user
    self.url = "https://lolchess.gg/profile/na/" + self.username

  def send_elo(self):
    # create requests and get the response
    response = requests.get(self.url)
    content = response.content

    # parse the HTML and pull data we want
    soup = BeautifulSoup(content, "html.parser")

    res = "```=== " + soup.title.text + " ===\n\n"

    result = soup.find_all("div", class_="profile__tier__summary")

    for i in result:
      tier = i.find("span", class_="profile__tier__summary__tier")
      lp = i.find("span", class_="profile__tier__summary__lp")
      percent = i.find("span", class_="top-percent")
      rank = i.find("span", class_="rank-region")
      res = res + "Tier: " + tier.text.strip() + "\n" + lp.text.strip() + "\n" + percent.text.strip() + "\n" + rank.text.strip() + "\n```"

    return res