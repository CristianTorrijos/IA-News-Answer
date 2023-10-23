## IA News Answer by Cristian Torrijos

This project is a test consisting of the following:

- Python Scripts:
  - (/python/import.py) fetch news from an API
    - Insert the news into an SQLite database (in this case, to facilitate the testing of this script, SQLite was chosen over MySQL, although MySQL is recommended for production)
    - Calculate the embeddings of the news texts and save them in each news record


  - (/python/search.py) It is expected to receive a topic to search related to crypto news, perform a cosine similarity search, obtain the most relevant news, and pose the question to the openai API conditioning it, with the most appropriate news based on that search criterion
    - The result of this script is an output on screen in JSON format, with the search result, along with the sources used to obtain the information.
    - Execution example:
      - cd python
      - python3 search.py "What happened in November 2022 with FTX?"
    - Example response:
      - {"completion": "In November 2022, FTX, a prominent cryptocurrency exchange, faced a dire financial situation leading to its collapse and subsequent revelations of misconduct. The collapse of FTX uncovered a web of deceit within the cryptocurrency industry. Shocking revelations came to light concerning the alleged misuse of billions in customer funds and the disappearance of these funds. The exchange struggled with processing customer withdrawals, and it was reported that billions of dollars in customer funds were unaccounted for.\n\nDuring the trial of Sam Bankman-Fried, the former CEO of FTX, which took place in October 2022, dramatic testimony further deepened the legal troubles of the defendant. Can Sun, FTX's former General Counsel, testified that Bankman-Fried had asked him to provide \"legal justifications\" to explain the disappearance of customer funds.\n\nFurthermore, it was revealed that FTX sought financial support from industry giants like Google and BlackRock before its collapse, indicating that the exchange was facing a dire financial situation.\n\nOverall, the events surrounding FTX's downfall and subsequent trial revealed the dark underbelly of the crypto industry, showcasing the risks and personal tragedies faced by those involved.", "records": [{"name": "The raw reality of the FTX crash \u2013 Inside look at victims", "url": "https://www.cryptopolitan.com/raw-reality-ftx-crash-inside-look-at-victims/"}, {"name": "FTX Scandal Unveiled: Shocking Revelations of Misappropriated Funds in Crypto Exchange Trial", "url": "https://thecurrencyanalytics.com/altcoins/ftx-scandal-unveiled-shocking-revelations-of-misappropriated-funds-in-crypto-exchange-trial-76821.php"}, {"name": "Former FTX Crypto Exchange CEO's Trial Takes Startling Turn as Witness Testifies", "url": "https://thecurrencyanalytics.com/altcoins/former-ftx-crypto-exchange-ceos-trial-takes-startling-turn-as-witness-testifies-77011.php"}, {"name": "Google And BlackRock Considered Investing In FTX Before The Crisis", "url": "https://coincu.com/224590-google-and-blackrock-investing-ftx/?utm_source=snapi"}, {"name": "Google and BlackRock Considered Investing in FTX as It Crumbled", "url": "https://decrypt.co/202583/google-blackrock-considered-investing-ftx-before-bankruptcy"}, {"name": "Here's Why Sam Bankman-Fried's Leaked Chat Causes Concerns", "url": "https://u.today/heres-why-sam-bankman-frieds-leaked-chat-causes-concerns?utm_source=snapi"}, {"name": "Former FTX general counsel testifies about missing user funds", "url": "https://www.cryptopolitan.com/former-ftx-counsel-testifies-missing-funds/"}, {"name": "Ex-General Counsel Sheds Light on FTX's $7B Gap in Bankman-Fried Fraud Trial", "url": "https://news.bitcoin.com/ex-general-counsel-sheds-light-on-ftxs-7b-gap-in-bankman-fried-fraud-trial/"}, {"name": "The risks of phishing scams for FTX account holders: stay alert!", "url": "https://www.cryptopolitan.com/phishing-scams-risks-for-ftx-account-holders/"}, {"name": "FTX Creditors Warned of Phishing Threat as SBF Criminal Trial Progresses", "url": "https://beincrypto.com/ftx-creditors-phishing/"}]}

## Steps to make it work

### Laravel

1. git clone of this project ;)
2. Go inside of folder of cloned project:
   - cd name_of_new_directory_here
3. launch in terminal "composer install" for install laravel dependencies
4. launch "php artisan serve", and you'll see something like this (click on the link in your terminal or copy and paste the URL in your browser)

INFO  Server running on [http://127.0.0.1:8000].



### Python

1. Open new terminal tab
2. Go to the project folder
3. Go to python directory "cd python"
4. Launch "python3 -m venv pruebaCristianTorrijosIA"
5. Launch "source pruebaCristianTorrijosIA/bin/activate"
6. Launch "pip3 install -r requirements.txt"

**¿You have a Apple Silicon, and you have some problems? If**
Launch this 2 commands: (**If you doesn't have this problems, continue to the step 9**)
7. pip3 uninstall numpy
8. ARCHFLAGS="-arch arm64" pip install numpy  --compile --no-cache-dir


9. rename the .env.example file to .env, and set your own OPENAI KEY ;)
10. test the search utility:
    - python3 search.py "When will the fried Sam Bankman trial be?"
    - python3 search.py "Does Coinbase have its own blockchain?"
    - python3 search.py "When will the Spot Bitcoin ETF be approved?"
    - python3 search.py "What happened in November 2022 with FTX?"
    - python3 search.py "Are FTX related scams happening?"
