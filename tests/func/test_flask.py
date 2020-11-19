
def test_home_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Created by Kairick 2020' in response.data
    assert "Доставка" in response.data.decode()
    assert "осуществляется" in response.data.decode()


