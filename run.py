from Handlers.instagram_session_handler import sign_in
from Handlers.user_followers_handler import get_user_followers, get_following_data
#from Handlers.n_layer_data_handler import n_layer_data_extraction

if __name__ == '__main__':
    session = sign_in()
    # TODO:  Take Center User's username and password from terminal !!!!
    initial_username = input
    username = initial_username
    n_layer_data_extraction(username, initial_username)

