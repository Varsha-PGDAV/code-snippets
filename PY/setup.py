def setupDomain(domain):
    endpoint = config.get("hsds_endpoint")
    print("setupdomain: ", domain)
    headers = getRequestHeaders(domain=domain)
    req = endpoint + "/"
    rsp = requests.get(req, headers=headers)
    if rsp.status_code == 200:
        return  # already have domain
    if rsp.status_code != 404:
        # something other than "not found"
        raise ValueError("Unexpected get domain error: {}".format(rsp.status_code))

    parent_domain = getParentDomain(domain)
    if parent_domain is None:
        raise ValueError("Invalid parent domain: {}".format(domain))
    # create parent domain if needed
    setupDomain(parent_domain)  
     
    headers = getRequestHeaders(domain=domain)
    rsp = requests.put(req, headers=headers)
    if rsp.status_code != 201:
        raise ValueError("Unexpected put domain error: {}".format(rsp.status_code)) 
