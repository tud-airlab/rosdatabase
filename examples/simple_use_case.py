from rosdatabase.yamldatabase import Database

# Example usage
if __name__ == "__main__":
    db = Database("example_db.yaml")
    db.add_entry("name", "John")
    db.add_entry("age", 30)
    print("Database:", db.data)
    db.remove_entry("age")
    print("Database after removing 'age':", db.data)
    print("Value of 'name':", db.get_entry("name"))
    print("Value of 'age':", db.get_entry("age"))
