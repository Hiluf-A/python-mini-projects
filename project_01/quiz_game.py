print("=============== WELLCOME TO THE GAME ==============")

playing  = input("Do you want to play the quizz game? ")

if playing.strip().lower()!= "yes":
    quit()

print("===== Okay! Let's play :) =====")

acronyms = {
    "AI": "Artificial Intelligence",
    "API": "Application Programming Interface",
    "CPU": "Central Processing Unit",
    "GPU": "Graphics Processing Unit",
    "RAM": "Random Access Memory",
    "HTML": "HyperText Markup Language",
    "CSS": "Cascading Style Sheets",
    "URL": "Uniform Resource Locator",
    "HTTP": "HyperText Transfer Protocol",
    "PDF": "Portable Document Format",
    "USB": "Universal Serial Bus",
    "WiFi": "Wireless Fidelity",
    "GPS": "Global Positioning System",
    "NASA": "National Aeronautics and Space Administration",
    "UN": "United Nations",
    "EU": "European Union",
    "WHO": "World Health Organization",
    "GDP": "Gross Domestic Product",
    "ROI": "Return on Investment",
    "FAQ": "Frequently Asked Questions"
}

score = 0
for key, value in acronyms.items(): 
    answer = input(f"What does {key} stand for? ")
    if answer == value.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print(f"You got: {score} quesitons correct")
print(f"You got {int(score/20 * 100)}% correct")