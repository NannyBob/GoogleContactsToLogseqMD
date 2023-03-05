import sqlite3
import tkinter.filedialog
import tkinter as tk
from os.path import exists
from sqlite3 import *

db_file_name = tkinter.filedialog.askopenfilename()
connection = connect(db_file_name)
cursor = connection.cursor()
#print(rows)
logseq_dir = tkinter.filedialog.askdirectory()
def does_name_exist():
    entities = [i[0] for i in cursor.execute("SELECT Names.Name FROM Names").fetchall()]
    print(entities)
    for entity in entities:
        if not exists(f"{logseq_dir}/{entity}.md"):
            reply = input(f"Why does {entity} not exist? want me to make it (y/n)")
            if reply =="y":
                f = open(f"{logseq_dir}/{entity}.md", "x")
                f.close()

def aliases():
    count={}
    rows = cursor.execute("SELECT EntityID,N.Name FROM Entities LEFT JOIN Names N on Entities.ID = N.EntityID").fetchall()
    for i in rows:
        if i[0] in count.keys():
            print(f"{count[i[0]]}, {i[1]}")
        count[i[0]] = i[1]

def import_relationships():
    relationships = cursor.execute("SELECT Relationships.Description,n1.Name,n2.Name FROM Relationships INNER JOIN Names n1 on Relationships.Start = n1.EntityID INNER JOIN Names n2 on Relationships.End = n2.EntityID WHERE n1.PrimaryName = 1 AND n2.PrimaryName=1").fetchall()
    for relationship in relationships:
        entity1 = relationship[1]
        entity2 = relationship[2]
        if exists(f"{logseq_dir}/{entity1}.md") and exists(f"{logseq_dir}/{entity2}.md"):

            message = f"- {relationship[0]} - [[{entity2}]]"
            print(f"Writing {message} to {entity1}")
            person_file = open(f"{logseq_dir}/{entity1}.md", 'a')  # Open file in append mode
            person_file.write(f"\n{message}")
            person_file.close()

            message = f"- {relationship[0]} - [[{entity1}]]"
            print(f"Writing {message} to {entity2}")
            person_file = open(f"{logseq_dir}/{entity2}.md", 'a')  # Open file in append mode
            person_file.write(f"\n{message}")
            person_file.close()
        else:
            print(f"Failed to write relationship {relationship}")

import_relationships()
