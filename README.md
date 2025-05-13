### LLM Chatbot
A simple Python script that connects to the OpenAI API to create an interactive chatbot. The script accepts user questions, sends them to the OpenAI GPT-4o model using the Responses API, and prints the responses. It includes basic error handling and a loop for multiple questions until the user types "exit".
Requirements

### Requirements
- Python 3.8+
- OpenAI API key (sign up at platform.openai.com)
- Required Python packages:
`openai`
`python-dotenv`

### Setup Instructions
1. Clone the repository:
- `git clone <repository-url>`
- `cd <repository-name>`

2. Set up a virtual environment (recommended) to isolate dependencies and avoid conflicts with your global Python environment and activate it
- `python -m venv venv`
- `source venv/bin/activate`

3. Install dependencies
- `pip install -r requirements.txt`

4. Set up the OpenAI API key
- Create a `.env` file in the project root
- Add your OpenAI API key to the .env file:OPENAI_API_KEY=your-api-key-here

You can get an API key from platform.openai.com/api-keys

### Run the script:
python main.py

Usage

When you run the script, it prompts you to enter a question.
Type your question and press Enter to see the response from the OpenAI model.
To ask another question, simply type it and press Enter.
To exit the program, type exit and press Enter.

Example
Welcome to the LLM Chatbot! Ask a question or type 'exit' to quit.

Your question: What is the capital of France?

Response: The capital of France is Paris.

Your question: exit
Goodbye!

Error Handling
The script includes basic error handling for:

Network connection issues (e.g., no internet).
Invalid API key.
Unexpected API errors.

If the API key is not set in the .env file, the script will display an error and exit.
Notes

The script uses the gpt-4o model via the OpenAI Responses API. You can modify the model parameter in main.py to use other OpenAI models if you have access.
Ensure your OpenAI API key is kept secure and not shared publicly.

License
This project is licensed under the MIT License.
