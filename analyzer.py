
#   MODULE : analyzer.py


NEWS_FILE     = "dataNews.txt"
ANALYSIS_FILE = "dataAnalysis.txt"

# Sets are used here because order doesn't matter and


HIGH_RISK_KEYWORDS = {
    "urgent", "forward immediately", "share now", "breaking",
    "guaranteed", "miracle", "100%", "exposed", "secret",
    "they don't want you to know", "shocking", "unbelievable",
    "going viral", "hoax", "conspiracy"
}

MEDIUM_RISK_KEYWORDS = {
    "claimed", "allegedly", "sources say", "rumour", "unverified",
    "anonymous", "insider", "leaked", "could be", "might be"
}

LOW_RISK_KEYWORDS = {
    "according to", "reported by", "confirmed", "official",
    "verified", "research shows", "study", "government", "published"
}


# ---------- helper: compute score for one piece of news ----------
def compute_score(text):
    """
    this modules checks if the risky words are present in the news
    or not , and scores them on the basis of above mentioned sets 
    """
    text_lower = text.lower()
    matched = []
    score = 0

    for word in HIGH_RISK_KEYWORDS:
        if word in text_lower:
            score += 3
            matched.append(word)

    for word in MEDIUM_RISK_KEYWORDS:
        if word in text_lower:
            score += 2
            matched.append(word)

    for word in LOW_RISK_KEYWORDS:
        if word in text_lower:
            score -= 1
            matched.append(f"-{word}")

    return score, matched


# ---------- helper: score → verdict (uses tuple for thresholds) ----------
def get_verdict(score):
    """
    Thresholds stored as tuple pairs.
    Tuple is used because thresholds are fixed / immutable constants.

    """
    thresholds = (
        (8,  "🔴 Likely Fake"),
        (4,  "🟠 Suspicious"),
        (1,  "🟡 Needs Verification"),
        (0,  "🟢 Low Risk"),
    )
    for min_score, verdict in thresholds: ## tuple unpacking , min_score gets the num values 
        if score >= min_score:
            return verdict
    return "🟢 Low Risk"

# ANALYZE — Scan all news and write results

def analyze_news():
    """Read dataNews.txt, score each entry, write results to dataAnalysis.txt."""
    print("\n--- ANALYZING NEWS ---")
    try:
        # Read news
        with open(NEWS_FILE, "r") as news_file:
            lines = news_file.readlines()

        if not lines:
            print("[i] No news records to analyze.")
            return

        analyzed = 0
        skipped  = 0

        with open(ANALYSIS_FILE, "w") as af:
            for line in lines:
                line = line.strip()
                if line == "":
                    continue

                if "|" not in line:
                    skipped += 1
                    continue

                parts = line.split("|")
                if len(parts) != 4:
                    skipped += 1
                    continue

                news_id, title, source, submitted_by = parts
                score, matched = compute_score(title)
                verdict = get_verdict(score)

                # Store matched keywords as a joined string
                keywords_str = ", ".join(matched) if matched else "none"

                af.write(f"{news_id}|{score}|{verdict}|{keywords_str}\n")
                analyzed += 1

        print(f"[✓] Analysis complete. Analyzed: {analyzed}  |  Skipped: {skipped}")
        print(f"    Results saved to '{ANALYSIS_FILE}'.")

    except FileNotFoundError:
        print("[!] No news file found. Please submit some news first.")
    except Exception as e:
        print(f"[ERROR] Analysis failed: {e}")


# ============================================================
# VIEW ANALYSIS — Display stored analysis results
# ============================================================
def view_analysis():
    """Read and display results from dataAnalysis.txt."""
    print("\n--- ANALYSIS RESULTS ---")
    try:
        with open(ANALYSIS_FILE, "r") as f:
            lines = f.readlines()

        if not lines:
            print("[i] No analysis data available. Run Analyze News first.")
            return

        print(f"\n{'='*65}")
        print(f"  {'News ID':<10} {'Score':<7} {'Verdict':<25} {'Matched Keywords'}")
        print(f"{'='*65}")

        for line in lines:
            line = line.strip()
            if line == "":
                continue

            parts = line.split("|")
            if len(parts) != 4:
                continue

            news_id, score, verdict, keywords = parts
            print(f"  {news_id:<10} {score:<7} {verdict:<25} {keywords}")

        print(f"{'='*65}")

    except FileNotFoundError:
        print("[!] No analysis file found. Please run 'Analyze News' first.")
    except Exception as e:
        print(f"[ERROR] Could not display analysis: {e}")
