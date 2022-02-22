from myapp import index

def test_index():
    assert index() == "This is a <h1>Home page!</h1>"