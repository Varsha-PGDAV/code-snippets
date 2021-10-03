def get_session(k8s_api_verify_tls):
    global session
    if session is None:
        with open('/var/run/secrets/kubernetes.io/serviceaccount/token') as token_file:
            token = token_file.read()
        session = requests.Session()
        session.headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json',
            'User-Agent': user_agent('Deis Controller', deis_version)
        }
        if k8s_api_verify_tls:
            session.verify = '/var/run/secrets/kubernetes.io/serviceaccount/ca.crt'
        else:
            session.verify = False
    return session 
