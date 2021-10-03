def setupDomain(domain, folder=False):
    endpoint = config.get("hsds_endpoint")
    headers = getRequestHeaders(domain=domain)
    req = endpoint + "/"
    rsp = requests.get(req, headers=headers)
    if rsp.status_code == 200:
        return  # already have domain
    if rsp.status_code != 404:
        # something other than "not found"
        raise ValueError(f"Unexpected get domain error: {rsp.status_code}")
    parent_domain = getParentDomain(domain)
    if parent_domain is None:
        raise ValueError(f"Invalid parent domain: {domain}")
    # create parent domain if needed
    setupDomain(parent_domain, folder=True)

    headers = getRequestHeaders(domain=domain)
    body=None
    if folder:
        body = {"folder": True}
        rsp = requests.put(req, data=json.dumps(body), headers=headers)
    else:
        rsp = requests.put(req, headers=headers)
    if rsp.status_code != 201:
        raise ValueError(f"Unexpected put domain error: {rsp.status_code}") 
