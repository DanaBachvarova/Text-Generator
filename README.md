# Collaborative To-Do List

## Overview
This project is a text generation application built with Gradio and markovify. It enables users to generate text in the style of a given author based on predefined or user-uploaded corpora.

## Key Features:
- **Preloaded Corpora**: Generate text using existing datasets.
- **Custom Uploads**: Users can upload their own text files as corpora.
- **Markov Chain-Based Generation**: Uses markovify to create stylistically consistent text.
- **Interactive Interface**: Powered by Gradio, allowing easy interaction via a web-based UI.
- **File Management**: Save, open, and delete generated texts.
- **Author-Based Exploration**: View all texts generated for a specific author.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package manager)

### Setup Instructions
1. **Clone the repository**
   ```sh
   git clone https://github.com/DanaBachvarova/Text-Generator
   cd Text-Generator
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```sh
   python app.py
   ```