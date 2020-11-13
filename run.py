from Handlers.instagram_session_handler import sign_in
from Handlers.mongodb_handler import insert_value
from Handlers.user_followers_handler import get_user_followers

if __name__ == '__main__':
    session = sign_in()
    get_user_followers(session, "batukargily", 360)
    insert_value()
