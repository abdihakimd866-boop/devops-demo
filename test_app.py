def test_movie_list():
    from app import MOVIES
    assert len(MOVIES) >= 5, "Need at least 5 movies in the list"
    print(f" Test passed: {len(MOVIES)} movies found.")

def test_app_starts():
    from app import app
    assert app is not None, "Flask app instance should not be None"
    print(" Test passed: Flask app instance is valid.")


if __name__ == '__main__':
    test_movie_list()
    test_app_starts()
    print("All tests passed!")