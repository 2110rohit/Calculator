import random


print("Love Calculator: Find Your Perfect Match!")
name1 =input("Enter name1: ")
name2 =input("Enter name2: ")

result = random.randint(0,99)


if name1.lower()[:7] == "navroop":
    name1 = name1[:7] 

if name2.lower()[:7] == "navroop":
    name2 = name2[:7] 



if name1.lower()[:5] == "rohit":
    name1 = name1[:5] 

if name2.lower()[:5] == "rohit":
    name2 = name2[:5] 

if name1.lower()[:4] == "roro":
    name1 = name1[:4] 

if name2.lower()[:4] == "roro":
    name2 = name2[:4] 


if (name1.lower() in ["navroop", "navi"] and name2.lower() not in ["rohit", "roro"]) or (name2.lower() in ["navroop", "navi"] and name1.lower() not in ["rohit", "roro"]):
    result = 0
    print(result)
elif (name1.lower() in ["navroop","navi"] and name2.lower() in ["rohit","roro"]) or (name2.lower() in ["navroop","navi"] and name1.lower() in ["rohit","roro"]):
    result=100
    print(result)
else:
    print(result)


love_quotes = [
    "You're my favorite place to go to when my mind searches for peace.",
    "Every love story is beautiful, but ours is my favorite.",
    "Together is a wonderful place to be.",
    "You and me make a wonderful 'We.'",
    "In you, I've found the love of my life and my closest, truest friend.",
    "Love is not just something. It's everything.",
    "You are my sun, my moon, and all my stars.",
    "Life is better when we're laughing together.",
    "You're the peanut butter to my jelly.",
    "I love you more than yesterday, but less than tomorrow.",
    "My heart is perfect because you are in it.",
    "Forever is a long time, but I wouldn't mind spending it by your side.",
    "You're the reason I believe in love.",
    "I'm much more me when I'm with you.",
    "Love is not about how many days, months, or years you have been together. Love is about how much you love each other every single day.",
    "You're the missing piece I never knew I needed.",
    "You had me at 'Hello.'",
    "Love is being stupid together.",
    "Home is wherever I'm with you.",
    "I choose you. And I'll choose you over and over and over. Without pause, without a doubt, in a heartbeat. I'll keep choosing you.",
    "Love is not finding someone to live with; it's finding someone you can't imagine living without.",
    "You are the best thing that ever happened to me.",
    "You're not just my love, you're my life.",
    "Two souls with but a single thought, two hearts that beat as one.",
    "I love you more than words can show, I think about you more than you could ever know.",
    "Being deeply loved by someone gives you strength, while loving someone deeply gives you courage.",
    "When I say I love you more, I don't mean I love you more than you love me. I mean I love you more than the bad days ahead of us, I love you more than any fight we will ever have.",
    "You are the answer to every prayer I've offered.",
    "Your hand fits in mine like it's made just for me.",
    "In your arms is my favorite place to be."
]

random_quote = random.choice(love_quotes)
print(random_quote)