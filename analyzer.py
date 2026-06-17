## this checks weather the news is fake or real , although its not accurate , it just checks according to logic

def analyze_news():

    keywords = [
        "urgent",
        "forward",
        "share",
        "breaking",
        "guaranteed"
    ]

    news_file = open("dataNews.txt", "r")
    analysis_file = open("dataAnalysis.txt", "w")

    for line in news_file:

        news_id, news_text = line.strip().split("|")

        score = 0

        news_text_lower = news_text.lower()

        for word in keywords:
            if word in news_text_lower:
                score += 2

        if score >= 6:
            result = "Likely Fake"

        elif score >= 2:
            result = "Suspicious"

        else:
            result = "Low Risk"

        analysis_file.write(
            news_id + "|" + str(score) + "|" + result + "\n"
        )

    news_file.close()
    analysis_file.close()

    print("Analysis Completed")


def view_analysis():

    try:
        file = open("dataAnalysis.txt", "r")

        for line in file:

            news_id, score, result = line.strip().split("|")

            print("--------------------")
            print("News ID :", news_id)
            print("Score   :", score)
            print("Result  :", result)

        file.close()

    except FileNotFoundError:
        print("No analysis data available")