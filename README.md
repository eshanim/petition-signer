# Sign change.org petitions!

This script will automatically open links + fill in your info into change.org petitions (pulled from the `links.py` file) so all you have to do is submit (and maybe do the recaptcha)!

(creds to [ally.wiki](https://docs.google.com/document/d/e/2PACX-1vSrT26HMWX-_hlLfiyy9s95erjkOZVJdroXYkU-miaHRk58duAnJIUWKxImRkTITsYhwaFkghS8sfIF/pub) for the list of petitions)

Side note for anyone wondering why the submission wasn't automated as well: change.org starts putting recaptchas after the first few signed petitions and automating those are a lot harder (if anyone knows a way to get around this, let me know!)

## Instructions
- You should have python installed (if you don't already click [here](https://www.python.org/downloads/).)
- Download this code
  - option 1: click the green "Clone or download" button on the upper-right, then "Download ZIP".
    - unzip the files somewhere on your computer
  - option 2: `git clone https://github.com/eshanim/petition-signer.git`
    - requires: a Github account, a terminal, and git installation
    
- Install requirements from your terminal
  - run `pip3 install -r requirements.txt` 
  - make sure you are in the petition-signer directory
    - if you aren't, use the command `cd petition-signer`
    
- Run the program (using terminal)!
  - run `python3 signPetitions.py`
  - enter your first name, last name, email
  - if you want all the links to open, enter `y` (might cause change.org to block your requests for a while, so i recommend the option below)
  - if you only want to sign some portion of the links (**recommended**: see notes below) , enter `n`
    - enter a starting number for the links 
    - enter a ending number for the links (there are currently 65)
  - selenium will open a chrome browser with the link and type in your information
  - you have to click on the submit button
  - once you click submit, the program will close the window + open the next link
  
- Ending the program:
  - if you want to stop before it's done:
    - close your terminal (terminate the whole window)
  - if there was any errors with any links, they'll be listed at the end so you can manually sign them
  - if you're getting a "try again" error on change.org, note the number of the last petition you signed (printed on terminal), and try again later using that number when it asks for `link start index`

  
## Notes
- It may be easier to run only a few at a time (so only enter range 0-15 first, and then do 15-30 later, etc.)

## Feedback
- If anyone has more petitions to add, please let me know!
- Also let me know if you run into issues or have any feedback!
