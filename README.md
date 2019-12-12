# pastebin scraper
A simple scraper to get the 8 most recent public pastes from pastebin.com

## A note...
This is super basic. For now it will print the name, link, syntax, and time since creation in the console.

## Usage
Run the script, and press enter to view next paste. If the user input is anything other than an empty string, it will stop printing the pastes.
When the script is dont printing pastes (or the user stopped it), the user can press enter again to close the browser and exit.

## Requirements
* Python:
    * beautifulsoup4
    * selenium
    * pandas (optional, commented out for now. Used to export as CSV if desired. Not implemented.)
* General:
    * chromedriver.exe (should be placed in C:/Windows/chromedriver.exe)
