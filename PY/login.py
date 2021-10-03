def __init__(self, scheme='http', marker=None, timeout=None):
        self.logger = logging.getLogger(__name__)
        self.__session = requests.Session()

        self.set_auth()

        self.marker = marker
        self.__session.headers.update({'X-Context-Marker': marker})

        self.prom_url = self._get_prom_url()
        self.port = self.prom_url.port
        self.host = self.prom_url.hostname
        self.scheme = scheme

        if self.port:
            self.base_url = "%s://%s:%s/api/" % (self.scheme, self.host,
                                                 self.port)
        else:
            # assume default port for scheme
            self.base_url = "%s://%s/api/" % (self.scheme, self.host)

        self.default_timeout = self._calc_timeout_tuple((20, 30), timeout) 
