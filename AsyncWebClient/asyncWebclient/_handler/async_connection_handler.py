from Common.Exception.ConnectionException import ConnectionException
from Common.Contract.Logger import ICustomLogger
from .AsyncRequestHandler import AsyncRequestHandler
from .NodeHandler import NodeHandler


class AsyncConnectionHandler(AsyncRequestHandler):

    def __init__(self, agentId, logger: ICustomLogger, urls: list):
        self.logger = logger
        self.nodeHandler = NodeHandler(urls, self.logger)
        self.agentId = agentId

    async def getConnection(self, session, url):
        _url = self.nodeHandler.request(url)
        response = await self.getRequest(session, self.agentId, self.logger, _url)

        if not bool(response):
            try:
                self.nodeHandler.requestUrlErrorHandler()

            except ConnectionException as e:
                self.logger.error(str(e) + f'| Url: {_url}', 'ConnectionHandler', self.agentId, e)
                pass

            self.logger.debug('Response in Connection Handler is {}'.format(response),
                              'ConnectionHandler',
                              self.agentId)
        return response

    async def postConnection(self, session, url, data=None):

        _url = self.nodeHandler.request(url)
        response = await self.postRequest(session, self.agentId, self.logger, _url, data)

        if not bool(response):
            try:
                self.nodeHandler.requestUrlErrorHandler()

            except ConnectionException as e:
                self.logger.error(str(e) + f'| Url: {_url}', 'ConnectionHandler', self.agentId, e)
                pass

            self.logger.debug('Response in Connection Handler is {}'.format(response),
                              'ConnectionHandler',
                              self.agentId)

        self.logger.debug('Response in Connection Handler is {}'.format(response), 'ConnectionHandler', self.agentId)
        return response

