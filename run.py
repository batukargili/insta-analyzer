from Handlers.instagram_session_handler import sign_in
from Handlers.user_followers_handler import get_user_followers, get_following_data

if __name__ == '__main__':
    session = sign_in()
    username = "batukargily"
    followers = get_user_followers(session, username)
    get_following_data(username, followers)
