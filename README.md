# 📖 BookWorm

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey.svg)
![GrizzHacks](https://img.shields.io/badge/GrizzHacks-2025-orange.svg)

> **Reading online, reimagined for focus and accessibility.**

---

## 🌟 What is BookWorm?
BookWorm is an innovative Flask-based web application created during the GrizzHacks 2025 Hackathon, designed to transform any webpage into a customizable, distraction-free reading experience. Enhance focus, accessibility, and interactivity with unique tools such as our Interactive Garden, Magic Highlight, and Read-Aloud functionality.

---

## 🚀 Features

### 🧹 **Clean & Customizable Interface**
- **Distraction-Free View:** Automatically removes clutter and distractions from articles.
- **Personalized Reading:** Customizable fonts, adjustable spacing, and responsive design.
- **Accessibility:** Light/Dark mode toggle for comfortable viewing at any time.

### 🌱 **Interactive Focus Garden**
- Cultivate a virtual garden that grows dynamically the longer you read, motivating consistent focus and attention.

### 🔮 **Magic Highlight**
- Instantly identify and highlight key points and essential information in your articles automatically.

### 📝 **Annotation Tools**
- Highlight important text and add personalized notes directly onto web articles for enhanced engagement.

### 🔊 **Read Aloud**
- Listen to your articles with built-in text-to-speech support, increasing accessibility and convenience.

### 📌 **Bookmarking & Saved Articles**
- Easily bookmark and revisit your favorite articles anytime.

### 😈 **Evil Mode**
- Activate a playful twist with reversed text and a whimsical interface, designed purely for fun!

### 🍪 **Cookie Consent Management**
- Seamlessly handles cookie consent, respecting user privacy and preferences.

---

## 🛠️ Tech Stack
- **Languages:** Python, JavaScript
- **Frameworks:** Flask, Tailwind CSS
- **Libraries:** Fontawesome, Shadcn UI, Rich
- **Tools:** Docker, Conda, Waitress
- **APIs:** Google Gemini API

---

## 📂 Project Structure
```
BookWorm/
├── app/
│   ├── static/         # CSS, JS, Images
│   ├── templates/      # HTML views
│   └── __pycache__/    # Compiled files
├── requirements.txt    # Dependencies
├── run.py              # Entry point
├── Dockerfile          # Docker setup
└── docker-compose.yaml # Docker Compose setup
```

---

## 🖥️ Installation & Setup

### **Prerequisites**
- Python 3.10+
- Conda

### **Setup Steps**

1. **Clone Repository**
   ```bash
   git clone https://github.com/SKel1817/BookWorm.git
   cd BookWorm
   ```

2. **Create & Activate Environment**
   ```bash
   conda create -n bookworm python=3.10
   conda activate bookworm
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create `.env` from `.env.example` and fill in:
   ```env
   SECRET_KEY=your_secret_key_here
   GOOGLE_GEMINI_API_KEY=api_key_here
   FLASK_RUN_HOST=0.0.0.0
   FLASK_RUN_PORT=8080
   ```

5. **Run the Application**
   ```bash
   python run.py
   ```
   Open `http://127.0.0.1:8080` in your browser.

### **Using Waitress (Production)**
- Install Waitress:
  ```bash
  pip install waitress
  ```
- Start server:
  ```bash
  python run.py
  ```

---

## 📖 How to Use BookWorm

1. Paste your article URL into the input field.
2. Click **"Read"** to enjoy a distraction-free interface.
3. Customize your reading using fonts, spacing, and colors.
4. Enable **Focus Mode** to grow your virtual garden.
5. Use annotation and highlight tools to engage actively.
6. Enable **Magic Highlight** for instant insights.
7. Bookmark articles for later revisits.

---

## 🤝 Contributing
We welcome contributions from everyone! See our [Contribution Guidelines](CONTRIBUTING.md).

---

## 📄 License
This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

© 2025 BookWorm - Reading online, reimagined for focus and accessibility

