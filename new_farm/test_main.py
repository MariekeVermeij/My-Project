import main

def test_index():
    assert farm2.index(2) == "Good Night"
    assert farm2.index(5) == "Good Morning"
    assert farm2.index(18) == "Good Evening"
    assert farm2.index(17) == "Good Afternoon"
def test_cow():
    assert farm2.cow() == 'Help a Cow to find a friend'

def test_flying_cow():
    assert farm2.fly() == 'Whooooo ooooo ... HOW?! - a flying Cow!!'
