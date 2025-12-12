# OpenAI Bot

A conversational bot powered by OpenAI's GPT-5.2 model.

## Features
- Interactive command-line interface (`bot.py`)
- Web-based Streamlit interface (`app.py`)
- Uses OpenAI's latest GPT-5.2 model
- Simple and easy to use

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Jay202425/openaibot.git
cd openaibot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set your OpenAI API key:
```bash
set OPENAI_API_KEY=your-api-key-here  # On Windows
export OPENAI_API_KEY=your-api-key-here  # On macOS/Linux
```

## Usage

### Command-Line Version
```bash
python bot.py
```
Type your messages and press Enter. Type `exit` to quit.

### Streamlit Web Version
```bash
streamlit run app.py
```
Open your browser to `http://localhost:8501`

## Requirements
- Python 3.7+
- OpenAI API key

## License
MIT
