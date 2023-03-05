import tkinter.filedialog
import tkinter as tk
from os.path import exists


def main():
    directory = tkinter.filedialog.askdirectory()
    people = []
    while True:
        person = input("\nPlease enter a person to include in the relationship, be specific\n"
                       "type exit to exit\n")
        if person == "exit":
            break
        else:
            people.append(person)
    for person in people:
        if not exists(f"{directory}/{person}.md"):
            print("failde")
            return
    relationship = input("Please input the relationship between these people\n").strip()
    for person in people:
        person_filename = f"{directory}/{person}.md"
        person_file = open(person_filename, 'a')  # Open file in append mode
        for other_person in people:
            if person == other_person:
                continue
            person_file.write(f"\n- {relationship} - [[{person}]]")
        person_file.close()

root = tk.Tk()
root.withdraw()
main()
