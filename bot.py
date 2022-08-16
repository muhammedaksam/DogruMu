import json
import praw
from os import environ
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

api_key = os.environ['API_KEY']
client_id = os.environ['REDDIT_CLIENT_ID']
secret = os.environ['REDDIT_SECRET']
password = os.environ['REDDIT_PW']
username = os.environ['BOT_USERNAME']

reddit = praw.Reddit(client_id=client_id,
                     client_secret=secret,
                     password=password,
                     user_agent='DogruMu - Dogruluk Kontrol Botu v 1.0.0 by u/XanelaOw',
                     username=username)

MAX_CLAIMS = 3
EMPTY_QUERY_ERROR = "İddiaların filtreleneceği bir sorgu sağlamadınız!\n\n"
MONITORED_SUBS = "Turkey+TurkeyDogrulama+TarihTarih+TarihiSeyler+TurkeyJerky+trpolitics"
API_ERROR = "Sorgunuza dayalı olan iddialar alınırken bir hata oluştu. :( Lütfen daha sonra tekrar deneyin."
replyHeader = "Sorgunuza dayalı olarak doğrulanmış 3 adete kadar ilgili iddiayı iletiyorum. Mobilde, tabloyu yana kaydırın:\n\n"
replyFooter = "\n\n_Google'ın [Doğruluk Kontrolü](https://developers.google.com/search/docs/advanced/structured-data/factcheck) araştırma aracını kullanan bir botum. Şu anda r/Turkey,  r/TurkeyDogrulama, r/TarihTarih, r/TarihiSeyler, r/TurkeyJerky, r/trpolitics subredditlerini izliyorum.  \n\n^[Kod/Dökümantasyon](https://github.com/muhammedaksam/DogruMu)"

def main():
    # monitor comment streams for relevant subreddits
    for comment in reddit.subreddit(MONITORED_SUBS).stream.comments(skip_existing=True):
        if comment.body.lower().find("!dogrumu") != -1:
            userQuery = comment.body.lower().split("!dogrumu")[1].strip(" ")
            if (len(userQuery) == 0):
                try:
                    comment.reply(body = EMPTY_QUERY_ERROR + replyFooter)
                except praw.exceptions.APIException as e:
                    print(e)
                    continue
            else:
                try:
                    # attemt call to Google's fact check API 
                    factCheckService = build("factchecktools", "v1alpha1", developerKey=api_key)
                    request = factCheckService.claims().search(query=userQuery)
                    response = request.execute()
                # TODO more specifically handle problems with Google's API
                except HttpError as err:
                    print (err)
                    try:
                        comment.reply(body = API_ERROR + replyFooter)
                    except praw.exceptions.APIException as e:
                        print(e)
                        continue
                else:
                    reply = buildMessage(response)
                    try:
                        comment.reply(body = reply)
                    except praw.exceptions.APIException as e:
                        print (e)
                        print ("Possibly rate limited!")
                        continue

def buildTableRow(claim):
    review = claim["claimReview"][0]
    publisher = ""
    rating = ""
    url = ""
    claimText = ""
    # make sure keys are present, since API documentation is uncertain
    if ("publisher" in review):
        publisher = review["publisher"]["name"]
    if ("textualRating" in review):
        rating = review["textualRating"]
    if ("url" in review):
        url = review["url"]
    if ("text" in claim):
        claimText = claim["text"]
    return "| _" + claimText + "_ | **" + rating + "** | " + "[" + publisher + "](" + url + ") |\n"

# build bot comment based on response from fact check API
def buildMessage(res):
    if "claims" in res.keys() and len(res["claims"]) > 0:
        reply = replyHeader + "| İddia | Değerlendirme | Kaynak |\n|:-|:-|:-|\n"
        for x in range(MAX_CLAIMS):
            if x == len(res["claims"]):
                break
            reply += buildTableRow(res["claims"][x])
        return reply + replyFooter
    else:
        return "Sorgunuzla ilgili kayda değer bir iddia bulamadım! Aramanızı gözden geçirmeyi deneyin." + replyFooter

if __name__ == "__main__":
    main()
