
# Web Scraping and Data Extraction Script

## Overview:
This Python script logs into a customer management website, extracts data such as customer names, phone numbers, addresses, and registration dates from multiple pages, and saves this information into a CSV file.

## Prerequisites:
Before running the script, ensure the following Python libraries are installed:
1. `requests` - For sending HTTP requests.
2. `beautifulsoup4` - For parsing the HTML content.
3. `lxml` - Parser used by BeautifulSoup.
4. `unidecode` - For normalizing text data.
5. `csv` - For writing the output data to a CSV file.

You can install these libraries using `pip`:
```bash
pip install requests beautifulsoup4 lxml unidecode
```

## Files:
- **script.py**: The main Python script for scraping customer data and saving it into a CSV file.
- **Book1.csv**: The output file that contains scraped customer information.

## How It Works:
1. **Login to Website**: The script first logs into the customer management system using a session and the provided PIN.
2. **Scrape Data**: It scrapes customer data (name, phone, address, and registration date) from each page of the website.
3. **Save Data to CSV**: Once the data is collected from all pages, it writes the data into a CSV file (`Book1.csv`).

## Instructions for Use:
1. Open the script and make sure the URL and login credentials are correct for your target website.
2. Run the script using Python:
   ```bash
   python main.py
   ```
3. After execution, check the output file `Book1.csv` in the specified location. It will contain the following columns:
   - Name
   - Phone
   - Address
   - Registered (Date)

## Known Issues:
- **Error Handling**: If there is an issue in scraping, an "error" message will be printed, and the script will continue to the next page.
- **Page Limits**: The script is currently set to stop after reaching the page limit (10472 entries). You may need to adjust this value depending on the actual number of pages.

## Future Improvements:
- Implement more robust error handling to prevent data loss.
- Add logging for easier debugging.
- Enhance pagination logic to handle dynamic page limits.
