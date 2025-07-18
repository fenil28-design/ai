#write a program to identify the type  of (narow,genral,super) based  on user input

while True:

    description = input("Describe the AI system: ").lower()

    if "specific task" in description or "one task" in description:
        print("This  is Narrow AI (ANI)")
    elif "multi-task" in description or "human-like" in description:
        print("This is General AI (AGI)")
    elif "superior to human" in description:
        print("This is super AI (ASI)")
    else:
        print("Type of AI could not be determined.")