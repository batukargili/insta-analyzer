from Handlers.instagram_session_handler import sign_in
from Handlers.user_followers_handler import get_user_followers

if __name__ == '__main__':
    session = sign_in()
    get_user_followers(session, "batukargily", 360)
