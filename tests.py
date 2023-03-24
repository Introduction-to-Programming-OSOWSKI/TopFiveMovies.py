#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2023
month = 4
day = 1

def test_code():
    assert main.topFiveMovies("a", "b", "c", "d", "e") == "a b c d e", "Failed using arguments 'a', 'b', 'c', 'd', 'e'"
    assert main.topFiveMovies("Shrek", "Shrek 2", "Shrek 3", "Shrek 4", "Shrek 5") == "Shrek Shrek 2 Shrek 3 Shrek 4 Shrek 5", "Failed using arguments 'Shrek', 'Shrek 2', 'Shrek 3', 'Shrek 4', 'Shrek 5'"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
