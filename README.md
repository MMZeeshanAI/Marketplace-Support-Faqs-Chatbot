# Chatbot Expert System for Marketplace Support

## Introduction ℹ️

This chatbot is designed to provide support for a marketplace by answering common user questions. It acts as an expert system, utilizing a predefined dataset of questions and answers to assist users. If the chatbot encounters a question it doesn't know how to answer, it will politely inform the user and offer to connect them with a real person for further assistance.

## Requirements 🛠️

- Python 3 or higher
- Git https://github.com/MMZeeshanAI/Marketplace-Support-Faqs-Chatbot.git
- virtualenv (for creating a virtual environment)

## How to Run 🚀

### 1. Clone the Repository:

```bash
git clone https://github.com/MMZeeshanAI/Marketplace-Support-Faqs-Chatbot.git
cd Marketplace-Support-Chatbot
```


### 2. Create and Activate Virtual Environment:

If `virtualenv` is not installed, install it using pip:

```bash
pip install virtualenv
```

Then, create and activate the virtual environment:

```bash
python3 -m venv venv_chatbot
source venv_chatbot/bin/activate  # On Windows, use `venv_chatbot\Scripts\activate`
```

### 3. Install Dependencies:

Use pip to install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the Application:

Execute the provided `main.py` script:

```bash
python3 main.py
```

## Usage Instructions 📝

- Once the chatbot is running, it will prompt the user for input.
- Users can ask questions related to the marketplace, and the chatbot will respond based on the predefined dataset.
- If the chatbot cannot answer a question, it will politely inform the user and offer to connect them with a real person for assistance.

## Testing Environment 🧪

The code has been tested using Python 3 on Linux Ubuntu 22.04.4 LTS.

## Contributing 🤝

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.


