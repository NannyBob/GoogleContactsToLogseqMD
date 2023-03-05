from tkinter import filedialog
from tkinter import *
import tkinter as tk


def extract_name(filename):
    return filename[filename.rfind('/') + 1:-3]


def main():
    people = filedialog.askopenfilenames()
    relationship = input("Please input the relationship between these people\n").strip()
    for person in people:
        person_file = open(person, 'a')  # Open file in append mode
        for other_person in people:
            if person == other_person:
                continue
            person_file.write(f"\n- {relationship} - [[{extract_name(other_person)}]]")
        person_file.close()

root = tk.Tk()
root.withdraw()
main()
