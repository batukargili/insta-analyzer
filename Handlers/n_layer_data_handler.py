from Handlers.user_followers_handler import get_user_followers, get_following_data
from Utils.log import init_logger

def n_layer_data_extraction(username, initial_username):
    username = username
    following = []
    # First layer
    if username == initial_username:
        logger.warning("Users Following list extracting from instagram")
        following = get_user_followers(session, username)
        get_following_data(username, following)
    
    else :
        logger.warning("Second Layer Following list extracting from instagram")
        for fl in following:
            user = fl.split('https://www.instagram.com/', 1)[1]
            if user == "yarenyilmazz":
                following_second_layer = get_user_followers(session, user)
                get_following_data(user, following_second_layer)