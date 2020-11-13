from Handlers.instagram_session_handler import sign_in
from Handlers.user_followers_handler import get_user_followers, etl_data

if __name__ == '__main__':
    session = sign_in()
    username = "batukargily"
    followers = get_user_followers(session, username, 370)
    etl_data(username, followers)
