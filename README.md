
# 📇 Contact Management System (CMS)

A simple command-line Contact Management System in Python that allows users to **add**, **display**, **search**, and **delete** contacts. Data is stored persistently in a JSON file (`contacts.json`).

---

## 📁 Files

- `cms.py` – Main Python script for managing contacts.
- `contacts.json` – JSON file used to store all contact information persistently.

---

## 🛠 Features

- ✅ Add new contacts (name, age, phone, email)
- ✅ View all saved contacts
- ✅ Delete a contact by index
- ✅ Search contact by name (partial match supported)
- ✅ JSON-based storage for data persistence

---

## 💻 How to Run

1. **Install Python** (if not already installed):  
   [Download Python](https://www.python.org/downloads/)

2. **Run the program** using terminal or command prompt:

   ```bash
   python cms.py
   ```

3. **Follow the menu options** to manage your contacts.

---

## 🧪 Example Usage

```
.....Welcome to Contact Management System.....

1. Add People  
2. Display People  
3. Delete People  
4. Search Contact  
5. Exit  

Enter the choice: 1
Name: Alice
Age: 23
Phone: 9876543210
Email: alice@example.com
Person Added Successfully!
```

---

## 📦 Contact Data Format

Each contact is stored as:

```json
{
  "name": "Alice",
  "age": "23",
  "phone": 9876543210,
  "email": "alice@example.com"
}
```

All contacts are saved under `"contacts"` in `contacts.json`.

---

## 🔒 Notes

- Contact list is auto-loaded from `contacts.json` at startup.
- All changes (add/delete) are saved automatically after each action.
- Validations for input types are included.

---

## 📄 License

This project is free to use for learning and educational purposes.
