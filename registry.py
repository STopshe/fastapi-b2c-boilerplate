import json  # Python's built-in JSON library — no pip install needed
from pathlib import Path  # Modern way to handle file paths in Python


def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to the Mini User Registry."


def describe_user(user: dict) -> str:
    return f"User: {user['name']} | Email: {user['email']} | Age: {user['age']}"


def create_user(name: str, email: str, age: int) -> dict:
    return {"name": name, "email": email, "age": age}


def print_all_users(users: list) -> None:
    print(f"Registered users: {len(users)}\n")
    for user in users:
        print(greet(user["name"]))
        print(describe_user(user))
        print()


def find_user_by_name(users: list, name: str) -> dict | None:
    for user in users:
        if user["name"] == name:
            return user
    return None


def save_users(users: list, filepath: str) -> None:
    """Save the users list to a JSON file.
    
    JSON (JavaScript Object Notation) is the data format of the web.
    Every REST API sends and receives JSON. Every database has JSON support.
    Python dicts convert to JSON naturally — they're the same shape.
    
    In Phase 3, this function gets replaced by a database INSERT.
    In Phase 1, FastAPI will automatically convert our dicts to JSON
    for HTTP responses. This is foundational.
    """
    path = Path(filepath)
    with path.open("w") as file:
        json.dump(users, file, indent=2)
    print(f"✅ Saved {len(users)} users to {filepath}")


def load_users(filepath: str) -> list:
    """Load users from a JSON file. Returns empty list if file doesn't exist.
    
    The 'with' statement is a context manager — it automatically closes
    the file when the block ends, even if an error occurs.
    In C, you'd do: FILE* f = fopen(...); ... fclose(f);
    In Python, 'with' handles the fclose for you. No resource leaks.
    """
    path = Path(filepath)
    if not path.exists():
        return []  # First run — no file yet. Return empty list.
    
    with path.open("r") as file:
        return json.load(file)


def main() -> None:
    DATA_FILE = "users.json"
    
    # Load existing users (if any)
    users = load_users(DATA_FILE)
    print(f"Loaded {len(users)} users from {DATA_FILE}\n")
    
    # Add a new user
    users.append(create_user("Ada", "ada@example.com", 28))
    users.append(create_user("Linus", "linus@example.com", 54))
    users.append(create_user("Grace", "grace@example.com", 41))
    
    # Print all
    print_all_users(users)
    
    # Search
    found = find_user_by_name(users, "Grace")
    if found is not None:
        print(f"Found: {describe_user(found)}\n")
    
    # Save to disk
    save_users(users, DATA_FILE)


if __name__ == "__main__":
    main()