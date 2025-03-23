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

### 📌 **Saving & Loading Articles**
- Easily save and revisit your favorite articles anytime.

### 😈 **Evil Mode**
- Activate a playful twist with reversed text and a whimsical interface, designed purely for fun!

---

## 🐳 Docker Setup

BookWorm is conveniently packaged in Docker for effortless deployment:

### **Docker Hub**
The official Docker image is hosted on Docker Hub under `mwcurtis20/bookworm`. Tags include:
- `latest`: Most recent build
- `stable`: Most recent stable release
- Specific version tags based on application releases

Pull the image easily:
```bash
docker pull mwcurtis20/bookworm:stable
```

### **Docker Compose & Watchtower**
- Deploy using Docker Compose provided (`docker-compose.yaml`).
- Automated deployment and updates are powered by [Watchtower](https://github.com/containrrr/watchtower), ensuring the application is always up-to-date without manual intervention.

Run deployment:
```bash
docker-compose up -d
```

---

## 🔄 Continuous Integration (CI/CD)

Our project utilizes GitHub Actions for automated builds and deployments:
- **Multi-Architecture Builds:** Automatically builds Docker images for AMD64 and ARM64.
- **Automated Deployment:** Images are automatically pushed to Docker Hub upon successful builds on the `main` branch.
- **Version Tagging:** Images are tagged with `latest`, `stable`, and specific version numbers extracted from `app/params.json`.

---

## 🛠️ Tech Stack
- **Languages:** Python, JavaScript
- **Frameworks:** Flask, Tailwind CSS
- **Libraries:** Fontawesome, Rich
- **Tools:** Docker, Conda, Waitress
- **APIs:** Google Gemini API

---

## 📂 Project Structure
```
BookWorm/
├── app/
│   ├── static/         # CSS, JS, Images
│   ├── templates/      # HTML views
├── requirements.txt    # Dependencies
├── run.py              # Entry point
├── Dockerfile          # Docker setup
└── docker-compose.yaml # Docker Compose setup
```

---

## 🖥️ Installation & Setup

See instructions above for Docker deployments or follow the manual development setup provided.

---

## 📖 How to Use BookWorm

1. Paste your article URL into the input field.
2. Click **"Read"** to enjoy a distraction-free interface.
3. Customize your reading using fonts, spacing, and colors.
4. Enable **Focus Mode** to grow your virtual garden.
5. Use annotation and highlight tools to engage actively.
6. Enable **Magic Highlight** for instant insights.
7. Revisit articles for later revisits.


---

## 📄 License
This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

© 2025 BookWorm - Reading online, reimagined for focus and accessibility