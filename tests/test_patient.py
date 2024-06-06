def test_patient_dashboard(test_client, init_database):
    response = test_client.post('/login', data=dict(
        username='testuser1',
        password='Password1'
    ), follow_redirects=True)
    assert response.status_code == 200

    response = test_client.get('/patients', follow_redirects=True)
    assert response.status_code == 200
    assert b'Patient Dashboard' in response.data
