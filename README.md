# Sill Diff tool for Pyfa

Sometime when you are messing around with setting skills in the fitting tool you improve skills
past needed level and pyfa can only export needed skills. This should allow you to diff your base
character against a modified character. When you are done modifing you skills save the character and then go to the character editor and you can export your skills to clipboard, do that for both characters
and save them to a text file called `base.txt` and `improved.txt`.


## Steps
1. Modify skills as needed until you are happy with it.
2. Save character as...
3. Go to character editor and choose your eve user, export skills to clipboard, save to text file called
`base.txt`
4. repeat 3 for new saved character and called text file `improved.txt`
5. Place those files in the same directory as the script
6. `python skill_diff.py` from a command line

## TODO
1. Reformat to eve format for import, need to figure out what that is
2. use files as command line arguments