import pyfiglet
import termcolor
import requests
from random import choice

inp2 = input("Do you want to have a dad jokes? [yes/no] ")

website = "https://icanhazdadjoke.com/search"
opening = pyfiglet.figlet_format("DADJOKE2022")
coloropening = termcolor.colored(opening, "red")

print(coloropening)
while inp2 == "yes":
    try:
        inp1 = input("Let me tell you a joke. Give me a topic: ")
        req = requests.get(
            website, headers={"Accept": "application/json"}, params={"term": inp1}
        ).json()
        result = req["results"]

        print(
            f"I've got "
            + str(len(req["results"]))
            + " jokes about "
            + inp1
            + ". Here's one: "
        )
        print(choice(result)["joke"])
        inp2 = input("Do you want to try again? ")
    except IndexError:
        print("Sorry, there's no dad jokes for that")
        inp2 = input("Do you want to try again? ")
