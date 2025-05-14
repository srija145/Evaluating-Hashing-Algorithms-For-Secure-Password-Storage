🔐 Hash Functions & Password Security

 ### 📌 Project Title:

**Hashing Plain Text Passwords and Performance Comparison**

🧠 Project Overview

This project explores the concept of password hashing using different cryptographic hash functions. It evaluates their **performance**, **security**, and **practical implementation** for password storage and verification systems.


### 🗂 Project Agenda

1. **Synthetic Dataset Creation**

   * 1000 fake user records (name, email, plaintext password)

2. **SQLite Database Setup**

   * Store all user data and password hashes in a structured format

3. **Hashing Algorithms**

   * Hash passwords using:

     * SHA-256
     * bcrypt
     * MD5
     * PBKDF2

4. **Performance Evaluation**

   * Measure time/resource usage of each algorithm
   * Analyze and visualize performance results

5. **Visualization**

   * Generate charts to compare speed and efficiency of algorithms

6. **Password Verification System**

   * Validate login by hashing input and comparing it with stored hashes

### 💻 Tools & Technologies Used

* Python (pandas, hashlib, bcrypt, sqlite3, matplotlib, time)
* Jupyter Notebook
* SQLite for lightweight database storage


### 📊 Results

* Performance metrics were visualized to show how algorithms differ in speed and complexity.
* **SHA-256** provides a balance between speed and security.
* **bcrypt** and **PBKDF2** were more secure but slower.
* **MD5** was fastest but least secure and outdated.


### ✅ Key Learnings

* Importance of using **strong hashing algorithms** for password storage.
* **Trade-off** between security and performance.
* Practical experience with **database integration**, **data simulation**, and **visual analysis**.

### 🚀 How to Run

1. Clone this repository:

```bash
git clone https://github.com/yourusername/hash-functions-project.git
```

2. Navigate to the project folder and open `Project.ipynb` in Jupyter Notebook.

3. Run all cells to:

   * Generate the dataset
   * Store data in SQLite
   * Hash passwords using various algorithms
   * Evaluate performance and visualize results
     
