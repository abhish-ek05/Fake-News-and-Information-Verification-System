from authentication import register, login
from news_module import submit_news
from analyzer import analyze_news, view_analysis

while True:

    print("\n===== FAKE NEWS DETECTION SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Submit News")
    print("4. Analyze News")
    print("5. View Analysis")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        submit_news()

    elif choice == "4":
        analyze_news()

    elif choice == "5":
        view_analysis()

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")