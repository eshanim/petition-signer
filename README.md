# Sign change.org petitions!

This script will automatically open links + fill in your info into change.org petitions (pulled from the `links.py` file) so all you have to do is submit (and maybe do the recaptcha)!

(creds to [ally.wiki](www.ally.wiki) for the list of petitions)

Side note for anyone wondering why the submission wasn't automated as well: change.org starts putting recaptchas after the first few signed petitions and automating those are a lot harder (if anyone knows a way to get around this, let me know!)

## Instructions
- You should have python installed (if you don't already click [here](https://www.python.org/downloads/).
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
  - if you want all the links to open (might cause change.org to pause your requests for a while), enter `y`
  - if you only want to sign some portion of the links (**recommended**) , enter `n`
    - enter a starting number for the links 
    - enter a ending number for the links
  - selenium will open a chrome browser with the link and type in your information
  - you have to click on the submit button (unfortunately can't automate this because of the recaptchas)
- Ending the program:
  - if you want to stop before it's done:
    - close your terminal (terminate the whole window)
  - if there was any errors with any links, they'll be listed at the end so you can manually sign them

  
## Notes
- It may be easier to run only a few at a time (so only enter range 0-10 first, and then do 10-20 later, etc.)
- If anyone has more petitions to add, please let me know!
- Also let me know if you run into issues or have any feedback!
