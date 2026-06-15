## all the news is submitted through here 
## for news submission , each one has to put news id and title
def submit_news():
    news_id = input("Enter News ID: ")
    title = input("Enter News Title: ")
    file = open("data/news.txt", "a")
    file.write(news_id + "|" + title + "\n")
    file.close()

    print("News Submitted Successfully")