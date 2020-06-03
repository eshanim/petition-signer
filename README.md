# Sign change.org petitions!

This will automatically open links + fill in your info into change.org petitions (in the `links.py` file) so all you have to do is (maybe do the recaptcha) and submit!

(creds to [ally.wiki](www.ally.wiki) for the list of petitions).

### Instructions
- You should have python installed (if you don't already click [here](https://www.python.org/downloads/).
- Download this code
  - option 1: click the green "Clone or download" button on the upper-right, then "Download ZIP".
    - Then, decompress the files somewhere on your computer
  - Option 2: `git clone https://github.com/eshanim/petition-signer.git`
    - Requires: a Github account, a terminal, and git installation
- Install requirements from your terminal
  - run `pip3 install -r requirements.txt` 
  - Make sure you are in the petition-signer directory
    - If you aren't, use the command `cd petition-signer`
- Run the program (using terminal)!
  - run `python3 signPetitions.py`
  - Enter your first name, last name, email
  - If you want all the links to open (might cause change.org to pause your requests for a while), enter `y`
  - If you only want to sign some portion of the linke, enter `n`
    - Enter a starting number for the links 
    - Enter a ending number for the links
  - Selenium will open a Chrome browser with the link and type in your information
  - You have to click on the submit button (this is because you can't automate the recaptchas)
- If you want to stop before it's done:
  - close your terminal (terminate the whole window)
  
## Notes
- It may be easier to run only a few at a time (so only enter range 0-10 first, and then do 10-20 later, etc.)
- If anyone has more petitions to add, please let me know!
- Also let me know if you run into issues or have any feedback!
