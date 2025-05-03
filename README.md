# 🤖 AutoSuggest System

The **AutoSuggest System** is a web-based NLP application that suggests the most related word from a large text corpus based on user input.

---

## 🚀 Features

- 🔍 Suggests relevant content based on **jaccard similarity**
- 📑 Displays **top 5 matched words** from the dataset
- 🌐 Runs a simple and interactive **web interface** using Flask

---

## 🧠 Tech Stack

- **Frontend**: HTML
- **Backend**: Python with Flask
- **Similarity method**: Jaccard Similarity
- **Libraries**: Flask, NumPy, pandas

---

## ⚙️ How It Works

1. Load `Book_Corpus.txt` and split into paragraphs.
2. Preprocess the corpus.
3. Calcualte the probability and then similarity.
4. Take user input through interface.
5. Display the **top 5 most relevant words** to the user.

---

## 🛠️ How to Run This Project Locally (Step-by-Step)

Follow these instructions to get the AutoSuggest System up and running on your machine:

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/Deepanshu7573Bansal/Computation-Linguistics-and-NLP-Project.git
cd Computation-Linguistics-and-NLP-Project

✅ Step 2: Create and Activate a Virtual Environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

✅ Step 3: Install All Required Packages
pip install flask torch sentence-transformers numpy scikit-learn

✅ Step 5: Run the Flask App
python app.py

✅ Step 6: Open in Your Browser
Visit: http://localhost:5000