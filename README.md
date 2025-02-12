### Python Dictionaries (Chapter 6)

---

#### **Summary**  
Dictionaries are dynamic, ordered collections of **key-value pairs** that allow efficient data storage and retrieval. Key features include:  
- **Flexibility**: Store strings, numbers, lists, or even other dictionaries.  
- **Mutability**: Add, modify, or remove key-value pairs dynamically.  
- **Nesting**: Combine dictionaries with lists or other dictionaries for complex data structures.

---

### **Key Concepts**  
#### **Creating Dictionaries**  
- Use curly braces `{}` and colons `:` to define key-value pairs.  
  ```python
  alien = {"color": "green", "points": 5}
  ```

#### **Accessing/Modifying Values**  
- Access values using square brackets `[]` or the `get()` method (to avoid errors for missing keys):  
  ```python
  print(alien["color"])  # Output: green
  speed = alien.get("speed", "slow")  # Returns "slow" if key doesn't exist
  ```
- Add or modify values:  
  ```python
  alien["speed"] = "medium"  # Adds new key-value pair
  alien["color"] = "yellow"  # Updates existing key
  ```

#### **Removing Key-Value Pairs**  
- Use the `del` keyword:  
  ```python
  del alien["points"]
  ```

#### **Looping Through Dictionaries**  
- Loop through keys, values, or both:  
  ```python
  # All key-value pairs
  for key, value in alien.items():
      print(f"{key}: {value}")

  # Only keys (default behavior)
  for key in alien.keys():
      print(key)

  # Only values
  for value in alien.values():
      print(value)
  ```

#### **Nesting**  
- **Dictionaries in Lists**:  
  ```python
  aliens = [{"color": "green", "points": 5}, {"color": "yellow", "points": 10}]
  ```
- **Lists in Dictionaries**:  
  ```python
  pizza = {"crust": "thick", "toppings": ["mushrooms", "pepperoni"]}
  ```
- **Dictionaries in Dictionaries**:  
  ```python
  users = {
      "user1": {"name": "Roy", "location": "Scranton"},
      "user2": {"name": "Andy", "location": "Italy"}
  }
  ```

#### **Tips**  
- Use `sorted()` to loop through keys in order:  
  ```python
  for name in sorted(favorite_languages.keys()):
      print(name)
  ```
- Use `set()` to remove duplicate values:  
  ```python
  unique_languages = set(favorite_languages.values())
  ```

