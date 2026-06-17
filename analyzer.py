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

        line = line.strip()

        # Skip blank lines
        if line == "":
            continue

        # Check if the line has the correct format
        if "|" not in line:
            print("Invalid record skipped:", line)
            continue

        parts = line.split("|")

        # Ensure exactly 2 fields
        if len(parts) != 2:
            print("Invalid record skipped:", line)
            continue

        news_id, news_text = parts

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
            f"{news_id}|{score}|{result}\n"
        )

    news_file.close()
    analysis_file.close()

    print("Analysis Completed")

def view_analysis():

    try:
        file = open("data/analysis.txt", "r")

        for line in file:

            news_id, score, result = line.strip().split("|")

            print("--------------------")
            print("News ID :", news_id)
            print("Score   :", score)
            print("Result  :", result)

        file.close()

    except FileNotFoundError:
        print("No analysis data available")