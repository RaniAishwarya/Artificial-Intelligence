# Define the knowledge base
knowledge_base = {
    "parent": {
        "Alice": ["Bob"],  # Alice is the parent of Bob
        "Bob": ["Charlie"]  # Bob is the parent of Charlie
    },
    "married": {
        "Alice": "David"  # Alice is married to David
    }
}

# Define helper functions
def is_parent(parent, child):
    """Check if a person is a parent of a given child."""
    return child in knowledge_base["parent"].get(parent, [])

def get_children(parent):
    """Retrieve all children of a given parent."""
    return knowledge_base["parent"].get(parent, [])

def are_siblings(person1, person2):
    """Check if two people are siblings."""
    for parent, children in knowledge_base["parent"].items():
        if person1 in children and person2 in children:
            return True
    return False

# Hypothesis: "Charlie is a sibling of Bob"
hypothesis = are_siblings("Charlie", "Bob")

# Solve and print the result
if hypothesis:
    print("The hypothesis 'Charlie is a sibling of Bob' is TRUE.")
else:
    print("The hypothesis 'Charlie is a sibling of Bob' is FALSE.")
