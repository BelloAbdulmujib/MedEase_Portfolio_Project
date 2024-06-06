def test_doctor_dashboard(test_client, init_database):
    response = test_client.post('/login', data=dict(
        username='testuser2',
        password='Password2'
    ), follow_redirects=True)
    assert response.status_code == 200

    response = test_client.get('/doctors', follow_redirects=True)
    assert response.status_code == 200
    assert b'Doctor Dashboard' in response.data
