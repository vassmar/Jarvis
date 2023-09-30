import webbrowser
from colorama import Fore
from plugin import plugin

@plugin("youtube")
def youtube(jarvis,s):
    jarvis.say("    Type 1 to open YouTube homepage.", Fore.BLUE)
    jarvis.say("    Type 2 to see whats trending on YouTube today.", Fore.BLUE)
    jarvis.say("    Type 3 to open your YouTube history.", Fore.BLUE)
    jarvis.say("    Type 4 to open your YouTube library.", Fore.BLUE)
    jarvis.say("    Type 5 to search something on Youtube.", Fore.BLUE)
    jarvis.say("    Type 6 to quit.", Fore.BLUE)
    choice=jarvis.input("You chose: ", Fore.GREEN)

    if choice == '1':
        URL = "https://www.youtube.com/"
        webbrowser.open(URL)
        return None
    
    elif choice == '2':
        URL = "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl"
        webbrowser.open(URL)
        return None
    
    elif choice == '3':
        URL = "https://www.youtube.com/feed/history"
        webbrowser.open(URL)
        return None
    
    elif choice == "4":
        URL = "https://www.youtube.com/feed/library"
        webbrowser.open(URL)
        return None
    
    elif choice == "5":
        URL = "https://www.youtube.com/results?search_query="
        search = jarvis.input("Tell me what you want to search:", Fore.GREEN)
        seperate_words = search.split(' ')
        if len(seperate_words)<1:
            jarvis.say("Error. No input")
        elif len(seperate_words == 1):
            for word in seperate_words:
                URL = URL + word
            webbrowser.open(URL)
        else:
            first_word = True
            for word in seperate_words:
                if first_word:
                    URL = URL + word
                    first_word = False
                else:
                    URL = URL + '+' + word
            webbrowser.open(URL)
        return None
    
    elif choice == "6":
        jarvis.say("Closed", Fore.RED)
        return None
    
    else:
        jarvis.say("Wrong Input", Fore.RED)
        return None
        