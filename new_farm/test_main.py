import main


def test_index():
    assert main.index(2) == "Good Night"
    assert main.index(5) == "Good Morning"
    assert main.index(18) == "Good Evening"
    assert main.index(17) == "Good Afternoon"


def test_cow():
    assert main.cow() == 'Help a Cow to find a friend'


def test_flying_cow():
    assert main.fly() == 'Whooooo ooooo ... HOW?! - a flying Cow!!'

