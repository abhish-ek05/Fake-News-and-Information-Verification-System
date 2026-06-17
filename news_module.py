def submit_news():
    news_id = input("Enter News ID: ")

    with open("dataNews.txt", "a+") as file:
        file.seek(0)

        for line in file:
            existing_id = line.strip().split("|")[0]

            if existing_id == news_id:
                print("News ID already exists!")
                return

        title = input("Enter News Title: ")
        file.write(f"{news_id}|{title}\n")

    print("News Submitted Successfully")

submit_news()