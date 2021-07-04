def sign_in(auth):
    auth_url = auth.get_authorization_url()
    print('visit this url to get pin: {}'.format(auth_url))
    auth_pin = input('Enter PIN: ')
    access_token,access_token_secret = auth.get_access_token(auth_pin)
    return access_token,access_token_secret