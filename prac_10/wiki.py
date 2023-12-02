import wikipedia

user_search = input("Enter what you want to search: ")
while user_search != "":
    print(wikipedia.summary(user_search))
    print(wikipedia.page(title=user_search, auto_suggest=False))
    user_search = input("Enter what you want to search: ")
