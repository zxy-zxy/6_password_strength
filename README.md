# Password Strength Calculator
Script for evaluation complexity of password. 
Password complexity will be scored from 1 to 10.

Password evaluation requirements:
1. Length more than 10 symbols.
2. Use numbers.
3. Use lowercase and uppercase letters.
4. Use special characters such as **&!#**.
5. Avoid to use blacklisted words.

## Usage
Python >= 3.5 required.

To run script open shell and run password_strength.py. 

You should keep **blacklist.txt** in same directory with python file to be able to
run check for a match with blacklisted words.
```bash
python password_strength.py
```
### Example input & output
```bash 
Enter a password (minimum length 6 is required): 
Your password security score is 9
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
