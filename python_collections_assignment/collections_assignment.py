# Python Collections Assignment
# Author: saman

def working_with_lists():
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print("Original list:", fruits)
    fruits.append('fig')
    print("After adding a fruit:", fruits)
    fruits.remove('apple')
    print("After removing a fruit:", fruits)
    print("Reversed list:", fruits[::-1])

def exploring_dictionaries():
    info = {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }
    info["favorite color"] = "Blue"
    info["city"] = "San Francisco"
    print("Keys:", ", ".join(info.keys()))
    print("Values:", ", ".join(str(v) for v in info.values()))

def using_tuples():
    favorites = ('Inception', 'Bohemian Rhapsody', '1984')
    print("Favorite things:", favorites)
    try:
        favorites[0] = 'Interstellar'
    except TypeError:
        print("Oops! Tuples cannot be changed.")
    print("Length of tuple:", len(favorites))

def main():
    print("Welcome to the Python Collections Assignment by saman!")
    working_with_lists()
    print("\n")
    exploring_dictionaries()
    print("\n")
    using_tuples()

if __name__ == "__main__":
    main()
