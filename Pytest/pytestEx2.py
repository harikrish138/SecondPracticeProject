import pytest

@pytest.mark.dependency()
@pytest.mark.order(1)
def test_open_aoo():
    print("App opened")

@pytest.mark.dependency(depends=['test_login'])
@pytest.mark.order(3)
def test_dashboard():
    print(' Dashboard loaded')

@pytest.mark.dependency(depends=['test_open_aoo'])
@pytest.mark.order(2)
def test_login():
    print('Log in successful')