import csv


def read_csv(file):
    headers = []
    data = []
    with open(file) as f:
        reader = csv.reader(f)
        first_row = True
        for row in reader:
            if first_row:
                headers = row
                first_row = False
            else:
                person = {}
                for count, field in enumerate(row):
                    if field != "":
                        if headers[count] in person:
                            person[headers[count]] = f"{person[headers[count]]}, {field}"
                        else:
                            person[headers[count]] = field
                data.append(person)
    return data


def format_phone_number(person):
    if "Phone Number" in person:
        person["Phone Number"] = person["Phone Number"].replace(" ", "")


def format_date(person):
    if "Birthday" in person:
        if "/" in person["Birthday"]:
            person["Birthday"] = f'[[{person["Birthday"].replace("/", "-")}]]'


def save_person_to_file(person):
    f = open(f"output/{person['Name']}.md", "w")
    f.write(f"tags:: [[people]]\n")
    for field in list(person.keys())[1:]:
        if field == "Name":
            continue
        f.write(f"{field}:: {person[field]}\n")


data = read_csv("contacts.csv")
for person in data:
    format_phone_number(person)
    format_date(person)
    save_person_to_file(person)
