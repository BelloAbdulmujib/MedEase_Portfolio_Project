from datetime import datetime

def test_book_appointment(test_client, init_database):
    response = test_client.post('/login', data=dict(
        username='testuser1',
        password='Password1'
    ), follow_redirects=True)
    assert response.status_code == 200

    response = test_client.post('/appointments', data=dict(
        doctor_id='1',
        date=datetime.now().strftime('%Y-%m-%d'),
        notes='Annual check-up'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b'Your Appointments' in response.data
    assert b'Annual check-up' in response.data
