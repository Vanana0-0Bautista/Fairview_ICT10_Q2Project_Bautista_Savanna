from pyscript import document, display

#PAGE1
Creator = [
    "Savanna Bautista"
]

def submit_form(e):

    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    full_name = first_name + " " + last_name

    is_creator = full_name in Creator

    messages = {
        True: f"Welcome {full_name}! Welcome Creator!",
        False: f"Sorry {full_name}, you are not the creator of this project."
    }

    if is_creator:
        document.getElementById("navigation").style.display = "block"

    document.getElementById("result").innerHTML = messages[is_creator]


    creator_info = {
    "HOBBY": ("drawing", "listening to music", "and being sporty"),
    
}

#PAGE#2
#Non-metals
#Dictionary with information about Non-metals
#Non-metal name: non-metal details, order from non-metal, and # of non-metals

Non_metals = {
    "H": ("Hydrogen", 1, 1),
    "He": ("Helium", 2, 4),
    "C": ("Carbon", 6, 12),
    "N": ("Nitrogen", 7, 14),
    "O": ("Oxygen", 8, 16),
    "F": ("Fluorine", 9, 19),
    "Ne": ("Neon", 10, 20),
    "P": ("Phosphorus", 15, 31),
    "S": ("Sulfur", 16, 32),
    "Cl": ("Chlorine", 17, 35),
    "Ar": ("Argon", 18, 40),
    "Se": ("Selenium", 34, 79),
    "Br": ("Bromine", 35, 80),
    "Kr": ("Krypton", 36, 84),
    "I": ("Iodine", 53, 127),
    "Xe": ("Xenon", 54, 131),
    "Rn": ("Radon", 86, 222)
}

#create a function to search a non-metal

def search_element(e):
    # get the input value from HTML
    Element1 = document.getElementById("nonmetal1").value.strip().capitalize()

    # retrieve information from the dictionary
    result = Non_metals.get(Element1, ("Element not found", "-", "-"))

    # display the result
    document.getElementById("code").innerText = Element1
    document.getElementById("name").innerText = result[0]
    document.getElementById("order").innerText = result[1]
    document.getElementById("count").innerText = result[2]

#PAGE3
from pyscript import document, display

grade7 = {'John Fartalot', 'Mary Harpy', 'Jacquavius Martin', 'Savanna Lacuesta'}
grade8 = {'Samantha Bautista', 'Nathan Lacuesta', 'Samantha Ladion', 'Maria Edmond'}
grade9 = {'Seana Urbano', 'Therion James', 'Euan Adreen', 'Mon Teresa'}
grade10 = {'Mon Erin', 'John Jacquavion', 'Martin Luther', 'Donald Trump'}

# Combine all grades into a base set
all_students = grade7.union(grade8, grade9, grade10)


def verify_candidate(e):
    first_name = document.getElementById("first_name").value.strip().capitalize()
    last_name = document.getElementById("last_name").value.strip().capitalize()
    full_name = f"{first_name} {last_name}"

    if first_name and last_name:
        all_students.add(full_name)

    total_members = len(all_students)

    student_list = "".join(
        f'<li style="background-color: #e8c5ce; font-weight: bold;">{student}</li>'
        if student == full_name
        else f"<li>{student}</li>"
        for student in sorted(all_students)
    )

    
    document.getElementById("result").innerHTML = f"""
        <h4>List of Students</h4>
        <ul class="student-list">
            {student_list}
        </ul>
        <h5>Total Number of Students: {total_members}</h5>
    """
