# BookWorm

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey.svg)
![GrizzHacks](https://img.shields.io/badge/GrizzHacks-2025-orange.svg)

## Overview

BookWorm is a Flask-based web application developed for the GrizzHacks 2025 Hackathon that transforms online reading experiences. Our platform simplifies web content consumption by providing a clean, distraction-free interface similar to document editors.

### Key Features

- **Clean Reading Interface**: Strips unnecessary elements from web pages
- **Annotation Tools**: Highlight text and add notes
- **Customization Options**: Adjust font type, size, and spacing
- **Accessibility**: Light/dark mode toggle and responsive design
- **Focus Mode**: Interactive garden that grows as you read

## Technical Architecture

- **Backend**: Python Flask server
- **Frontend**: Shadcn component library with Fontawesome icons
- **Design**: Responsive layout with nature-inspired pastel color palette

## Development Setup

### Prerequisites
- Python 3.10+
- Conda

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SKel1817/BookWorm.git
    cd BookWorm
    ```

2. Create and activate a conda environment:
    ```bash
    conda create -n bookworm python=3.10
    conda activate bookworm
    ```

3. Install dependencies:
    ```bash
    python3 -m pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory of the project and add the following variables. A sample `.env.example` file is provided for reference:
    ```env
    SECRET_KEY=your_secret_key_here
    GOOGLE_GEMINI_API_KEY=api_key_here
    FLASK_RUN_HOST=0.0.0.0
    FLASK_RUN_PORT=8080
    ```

5. Run the development server:
    ```bash
    python3 run.py
    ```

6. Open your browser and navigate to `http://127.0.0.1:8080`

### Running with Waitress

To run the application using Waitress, follow these steps:

1. Ensure you have installed Waitress:
    ```bash
    pip install waitress
    ```

2. Start the server using the `run.py` script:
    ```bash
    python run.py
    ```

### Development Tips

- **Using Rich for Logging**: The application uses the Rich library for enhanced logging. Ensure your terminal supports Rich's output for the best experience.
- **Handling Signals**: The `run.py` script includes a signal handler to gracefully shut down the server using `CTRL+C`.

## Contributing

We welcome contributions! Please see our contribution guidelines for more information.

## License

This project is licensed under the MIT License - see the LICENSE file for details.