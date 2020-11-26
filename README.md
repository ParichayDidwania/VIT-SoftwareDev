# VIT-SoftwareDev

Problem Statement:  
https://docs.google.com/document/d/16CNXNQ-VLLSoVe7CvJFBzueawgrCjWorB7zMLNvOF94/edit?usp=sharing

#Working
Created array of all characters,
Variables for holding Lives left,
and a dictionary of all the possible moves to be entered for the particular character.

The dictionary contains the index which needs to be added to the base index to get the new position.

Handled all possible exceptions when taking inputs from user for
1. Selecting invalid character
2. Repeating the character

Handled all possible exceptions for moves:
1. Check for a valid selection
  (A) Character Doesnot exist
  (B) Character Dead

2. Check for valid Moves from a particular character (eg. FL cannot be for P1 or H1)

3. Check for Resulting index
  (A) Out of Board
  (B) Overlapping with own character
