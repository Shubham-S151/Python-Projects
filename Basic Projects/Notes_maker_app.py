"""
Project Title: Python Notes Maker (Console Application)

Project Description:
This is a simple command-line notes management application built using Python.
The program allows users to create, view, read, edit, and delete notes organized
by topics. Each topic can have multiple notes, and each note consists of a title
and content. Users can navigate through topics and notes using numbered selections.

Concepts Used:
- Variables
- Dictionaries (for storing topics, note titles, and content)
- Functions
- While loops
- For loops
- If–Else conditions
- User input (input function)
- Basic error handling and validation

The program continuously displays a menu for the user to select actions. It ensures
that topic names and note titles are not empty and prevents duplicate note titles
under the same topic.
"""

"""
Notes Dictionary Structure:

notes = { 
    "topic1": {
        "title1": "content1",
        "title2": "content2"
    },
    "topic2": {
        "title1": "content1",
        "title2": "content2"
    }
}
"""

# Code Structure
'''
main while loop
   ├── menu
   │     ├── create_note
   │     ├── view_notes
   │     ├── read_note
   │     ├── edit_note
   │     └── delete_note
   ├── helper functions
   │     ├── select_topic
   │     └── select_note
   └── notes dictionary
         └── stores all topics and notes
'''

# Notes dictionary: {topic: {title: content}}
notes = {}

# Function to create a note
def create_note():
    topic = input("Enter new topic: ").strip()
    while topic.strip() == "":
        print("Invalid Topic Name please try again")
        topic = input("Enter new topic: ").strip()
    
    while True:
        title = input("Enter note title: ").strip()
        if not title:
            print("Invalid Title Name, please try again.")
            continue
        if topic in notes and title in notes[topic]:
            print("A note with this title already exists under this topic.\n")
            continue
        break 

    content = input("Enter note content: ").strip()

    if topic not in notes:
        notes[topic] = {}

    notes[topic][title] = content
    print("Note created successfully!\n")

# Function to view all notes
def view_notes():
    if not notes:
        print("No Notes Available!")
        return 
    
    print("\nList of all notes by topic:")
    for topic,topic_notes in notes.items():
        print(f"Topic: {topic}")
        for i,title in enumerate(topic_notes):
            print(f"    {i+1}. {title}")
    print()

# Helper function: select a topic
def select_topic():
    if not notes:
        print("No topics available!\n")
        return None
    
    topic_list = list(notes.keys())
    print("\nAvailable Topics: ")
    for i,topic in enumerate(topic_list):
        print(f"{i+1}. {topic}")
    topic_index = int(input("Select the topic number: "))
    if topic_index < 1 or topic_index > len(topic_list):
        print("Invalid topic number!\n")
        return None
    return topic_list[topic_index-1]

# Helper function: select a note under a topic
def select_note(topic):
    title_list = list(notes[topic].keys())
    for i, title in enumerate(title_list):
        print(f"{i+1}. {title}")
    title_index = int(input("Enter the title number: "))
    if title_index < 1 or title_index > len(title_list):
        print("Invalid topic number!\n")
        return None
    return title_list[title_index-1]

# Function to read a note
def read_note():
    topic = select_topic()
    if not topic:
        return
    title  = select_note(topic)
    if not title:
        return
    print(f"\nTopic: {topic}")
    print(f"Title: {title}")
    print(f"Content: {notes[topic][title]}\n")

# Function to edit a note
def edit_note():
    topic = select_topic()
    if not topic:
        return
    title  = select_note(topic)
    if not title:
        return
    
    new_content = input("Enter new content: ").strip()
    notes[topic][title] = new_content
    print("Note updated successfully!\n")

# Function to delete a note
def delete_note():
    topic = select_topic()
    if not topic:
        return
    title = select_note(topic)
    if not title:
        return
    
    del notes[topic][title]
    if not notes[topic]:
        del notes[topic]
    
    print("Note deleted successfully!\n")

# Menu system
def menu():
    while True:
        print("===== NOTES MAKER =====")
        print("1. Create Note")
        print("2. View Notes")
        print("3. Read Note")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_note()
        elif choice == 2:
            view_notes()
        elif choice == 3:
            read_note()
        elif choice == 4:
            edit_note()
        elif choice == 5:
            delete_note()
        elif choice == 6:
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")

menu()