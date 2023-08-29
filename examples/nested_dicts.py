from rosdatabase.yamldatabase import Database
import numpy as np

# Example usage
if __name__ == "__main__":
    db = Database("nested_db.yaml")
    numpy_array = np.random.random(3)
    entry_0 = dict(a=3,b=[3.0, 3.0])
    key_0 = "first_item"
    db.add_entry("numpy_array", numpy_array)
    db.add_entry(key_0, entry_0)
    db.add_entry("age", 30)
    print("Database:", db)
