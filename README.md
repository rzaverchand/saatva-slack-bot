# Saatva Product Slack Chatbot

This Python application scrapes product descriptions from [www.saatva.com](https://www.saatva.com) and saves the product details in a CSV file. The CSV data is then utilized to create a vectorstore for a language model to enable interactions with users in a Slack environment.

## Getting Started

### Prerequisites

1. **Environment Variables**: You'll need the following environment variables set:

    - `OPENAI_API_KEY`
    - `SLACK_APP_TOKEN`
    - `SLACK_BOT_TOKEN`

2. **Python**: Make sure you have Python installed. This project was developed using Python 3.

### Installation

1. **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Set Up a Virtual Environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

3. **Install Required Libraries**:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. **Run the Scraper Notebook**:

    Open the `saatva_scraper.ipynb` notebook and run all cells. This will generate a CSV file with product details from Saatva, which will be saved in the `data` folder.

    > **Note**: If you choose to change the default path where the CSV is saved in the notebook, ensure you update the file name in `slack_app.py` in the `chatgpt_chain` function to reflect the correct path.

2. **Run the Slack Application**:

    ```bash
    python slack_app.py
    ```

    On successful startup, you should see the message: 

    ```
    Bolt app is running!
    ```

3. **Chatting with the Bot**:

    Go to your Slack workspace. In any channel where the bot is a member, you can ask questions about Saatva products. The bot will provide answers based on the scraped data.

1. **Sample Questions**: These are some questions you could ask the bot.

    - Which product has the highest price? And which has the lowest?
    - Which product has the highest rating? And which has the lowest?
    - Which product has the highest number of reviews? And which has the lowest?
    - What is the average price of all of a certain product type?
    - What is the average rating across all products of a certain type?
    - What is the average number of reviews across all products of a certain type?
    - How would you recommend I furnish my empty bedroom?
    - Compare these products (of similar product types).

