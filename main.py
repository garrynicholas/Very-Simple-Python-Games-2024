'''
Developed by: Twizzyson Engine
Date: 7/15/2024

(Social Media)
Instagram: @twizzyson_engine
Tiktok: @Twizzyson Engine
Youtube: Twizzyson

Support me by sending me a drink in:
Kofi (USD Currency): https://ko-fi.com/twizzyson_engine
Trakteer (IDR Currency): teer.id/twizzyson_engine
'''

import random

# Random names, occupations, backstories, clues

names = ["Mandix", "Verica", "Kamrin", "Sandux", "Fruta", "Pontra", "Pentrix", "Zenica", "Cosmic", "Hanmon",
         "Quandro", "Kalix", "Dromse", "Asmer", "Lauder", "Luxxy", "Frexmy", "Jaume", "Erska", "Younx", "Wander",
         "Casmix", "Fremeta", "Vandem", "Ioden"]

occupations = [
    "Journalist", "University Professor", "Security Consultant", "Chef", "Software Developer",
    "Taxi Driver", "Nurse", "Architect", "Street Performer", "Lawyer",
    "Retired Military Officer", "Artist", "IT Technician"
]

backstories = [
    "I've been a journalist for over a decade, recently published an article critical of the president's policies. I've been receiving threats because of that.",
    "I have been actively participating in political rallies and had a public argument with a presidential aide last month.",
    "I was officially off duty during the incident, but I stayed to watch the debate. My expertise is in identifying security risks.",
    "Worked as a private chef for a high-profile politician who was a rival of the president.",
    "Developed a controversial app that was recently banned by the government.",
    "Picked up a mysterious passenger who was in a hurry to reach the debate venue.",
    "Worked at a hospital where several high-profile political figures were treated.",
    "Designed the debate venue and had access to all the security plans.",
    "Frequently performed at political rallies and had a history of radical political statements.",
    "Represented several high-profile criminals who were recently pardoned by the president.",
    "Was publicly critical of the president’s policies on military spending.",
    "Created politically charged artworks that criticized the president.",
    "Was responsible for setting up the audio-visual equipment for the debate.",

]

clues = [
    "You found a crumpled piece of paper in my pocket with a contact number for an activist group.",
    "In my bag, you found an unusual recording device. It’s sophisticated and seems out of place for a professor.",
    "In my vehicle, you found a map of the city with several locations circled, including security checkpoints and escape routes.",
    "Found a receipt for a large quantity of kitchen knives purchased a day before the debate.",
    "Found a hidden folder on their laptop with encrypted messages discussing the debate.",
    "Found a small bag in the car with a disassembled firearm.",
    "Found a syringe and a vial of an unknown substance in their bag.",
    "Found blueprints of the venue with certain areas marked in red.",
    "Found a fake ID and a disguise kit in their bag.",
    "Found a list of names and dates in their briefcase, with the president's name highlighted.",
    "Found a military-grade GPS device with recent coordinates leading to the debate venue.",
    "Found sketches of the debate venue with detailed annotations of security positions.",
    "Found a remote control device capable of interfering with electronic signals.",

]

# Generate random suspect (Either 1, 2, or 3)

suspects = []

for i in range(3):
    name = random.choice(names)
    # this is important to not randomize the same name again
    names.remove(name)
    occupation = random.choice(occupations)
    backstory = random.choice(backstories)
    clue = random.choice(clues)
    suspects.append({
        "name": name,
        "occupation": occupation,
        "backstory": backstory,
        "clue": clue,
    })

# randomly select the real suspect
# from lowest possible (0) to higher possible (2)
real_suspect = random.randint(0, 2)


def display_introduction():
    print("===================================================================================================================================================")
    print("=================================                            THE JUDGECTIVE                         ===============================================")
    print("===================================================================================================================================================")
    print("= In the bustling city of Caulin, within the nation of Ventarnia, a tragic event unfolds.                                                         =")
    print("= During a heated debate speech, the president is assassinated. The city is in turmoil, and the responsibility falls on you to uncover the truth. =")
    print("= As a judge with the sharp instincts of a detective, you must interrogate the suspects and determine who is guilty.                              =")
    print("= Three individuals have been identified as close criminal suspects in the assassination. You must choose one to begin your interrogation.        =")
    print("===================================================================================================================================================\n")


def display_suspects():
    for i, suspect in enumerate(suspects):
        print(f"Person {i + 1}: {suspect['name']}")


def interrogate_suspect(suspect):
    print(f"\nInterrogating {suspect['name']}")
    print("Choose one only information to be asked:")
    print("1. Occupation")
    print("2. Backstory")
    print("3. Clue")
    choice = input("Enter your choice: (1, 2, or 3): ")
    if choice == "1":
        print(f"Occupation: {suspect['occupation']}")
    elif choice == "2":
        print(f"Backstory: {suspect['backstory']}")
    elif choice == "3":
        print(f"Clue: {suspect['clue']}")
    else:
        print("Invalid choice!")

# main function

def main():
    display_introduction()
    display_suspects()

    # user only has 3 question to be asked
    question_left = 3
    while question_left > 0:
        # - 1 means that always a index start from 0, so if user type 2 it would still entered as 2 instead of 3 (0, 1, 2)
        person_choice = int(input("\nChoose a Person to Interrogate (1, 2, or 3): ")) - 1
        interrogate_suspect(suspects[person_choice])
        # substracting question_left
        question_left -= 1
        if question_left > 0:
            start_decision = input("\nStart Decision? [Y/N]: ")
            if start_decision.lower() == "y":
                break

    print("\nChoose Decision of Suspect")
    print("1. Person 1")
    print("2. Person 2")
    print("3. Person 3")
    decision = int(input("Enter your choice (1, 2, or 3): ")) - 1

    if decision == real_suspect:
        print(f"\nYou are right. The suspect was a Person {decision + 1}, {suspects[decision]['name']}")
    else:
        print("\nNone of the suspect you selected were guilty. Some others say you are a corrupt authority. You were about to get imprisoned for several years....")
    print("Game Over")


if __name__ == "__main__":
    main()