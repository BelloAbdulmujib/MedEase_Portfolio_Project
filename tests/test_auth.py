def test_register(test_client, init_database):
    response = test_client.post('/register', data=dict(
        username='testuser3',
        email='test3@example.com',
        password='Password3',
        password2='Password3'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'Congratulations, you are now a registered user!' in response.data

def test_login(test_client, init_database):
    response = test_client.post('/login', data=dict(
        username='testuser1',
        password='Password1'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'Welcome, testuser1!' in response.data

def test_logout(test_client):
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b'You have been logged out' in response.data
