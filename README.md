# AI Chat and Debate

Some example Python for chatting with OpenAI's ChatGPT and Google's Gemini.

The fun part, however, is having them debate each other!  Run ```python debate.py``` to see them debate the existence of God.

## Installation 

Before running the scripts, you'll need to do a couple steps:

### Dependencies

First, install the required dependencies:

```bash
pip install -r requirements.txt
```

### Configuration

To configure the application, you need to set up your API keys. We use a `.env` file for this. Follow the steps below:

1. Create a new file in the project root directory and name it `.env`.
2. Open the `.env` file and add your API keys in the following format:

```bash
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```

You get these keys from OpenAI and Google's Gemini websites, respectively.  Google it, as they say.

## Usage

Chat with OpenAI

```bash
python chat.py
```

You might find this one's responses.....unique!  Oh, and it is currently configured to use Chat-GPT4-Turbo Preview, which you might need to adjust to what you have access too and/or is available.

Chat with Gemini

```bash
python gchat.py
```

Have ChatGPT and Gemini debate the existence of God.

```bash
python debate.py
```

## Notes

Occasionally, the Gemini API may raise safety exceptions during the debate about the existence of God. While this may seem surprising, it reflects the current state of AI and the policies of major AI providers.

## License

This project is licensed under the terms of the MIT license.

