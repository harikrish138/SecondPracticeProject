
import pytest
import requests
user_id=None
HEAdERS={'x-api-key':'reqres-free-v1'}
payload={'name':'Harikrishna',
         'surname':'sandrapalli',
         'ID':'1234'}
def test_get_request():
    respons=requests.get(url='https://reqres.in/api/users/2',headers=HEAdERS)
    data=respons.json()
    assert respons.status_code == 200 , 'Wrong status'
    assert respons.elapsed.total_seconds()<2 , 'Too late'
    user_id=data.get('id')
    print(user_id)
    print(data)

def test_post_request():
    respons=requests.post(url='https://reqres.in/api/users',json=payload,headers=HEAdERS)
    data=respons.json()
    assert respons.status_code == 201 , 'Wrong status'
    assert respons.elapsed.total_seconds()<2 , 'Too late'
    print(data)

def test_put_request():
    payload={'name':'vikram'}
    response=requests.put(url='https://reqres.in/api/users/2',json=payload,headers=HEAdERS)
    data=response.json()
    assert response.status_code == 200, 'Post request not working'
    print(data)


