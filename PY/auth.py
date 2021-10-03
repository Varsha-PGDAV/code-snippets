def __init__(self, url, mutual_auth, cert=None, verify='true', **kwargs):

        self._logger = logging.getLogger("SPOT.INGEST.HDFS_client")
        session = Session()

        if verify == 'true':
            self._logger.info('SSL verification enabled')
            session.verify = True
            if cert is not None:
                self._logger.info('SSL Cert: ' + cert)
                if ',' in cert:
                    session.cert = [path.strip() for path in cert.split(',')]
                else:
                    session.cert = cert
        elif verify == 'false':
            session.verify = False

        super(SecureKerberosClient, self).__init__(url, mutual_auth, session=session, **kwargs)
