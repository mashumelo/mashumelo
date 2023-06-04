import random

greetings = ["Hello!", "What's up?", "Howdy!", "Greetings!"]
goodbyes = ["Bye!", "Goodbye!", "See you later!", "See you soon!"]

keywords = ["music", "pet", "book", "game"]
responses = ["Music is so relaxing!", "Dog's are a man's best friend.", "I know a lot about books.", "I play many different types of video games."]

print(random.choice(greetings))
user = input("Say something (or type bye to quit): ")
user = user.lower()

while (user != "bye"):
    keyword_found = False

    for index in range(len(keywords)):
        if (keywords[index] in user):
            print("Bot: " + responses[index])
            keyword_found = True

    if (keyword_found == False):
        new_keyword = input("I'm not sure how to respond. What should I respond to? ")
        keywords.append(new_keyword)
        new_response = input("How should I respond to " + new_keyword + "? ")
        responses.append(new_response)

    user = input("Say something (or type bye to quit): ")
    user = user.lower()

print (random.choice(goodbyes))