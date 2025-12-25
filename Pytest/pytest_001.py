import json

import pytest
def load_data():
    with open('./Files/data.json') as f:
        return json.load(f)


def test_openBrowser(browser):
    browser.get('https://google.com')

@pytest.mark.parametrize('x,y,result',[(12,23,35),(1,2,3),(21,2,23)])
def test_addition(x,y,result):
    assert x+y ==  result

@pytest.mark.parametrize('data',load_data())
def test_add(data):
    assert data["x"] + data["y"] == data["result"]

