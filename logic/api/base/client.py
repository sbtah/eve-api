import httpx
from logic.settings.logging import logger


class BaseClient:
    """
    Base Api Client
    """
    def __init__(self):
        self.logger = logger

    @property
    def headers(self):
        return {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Cache-Control': 'no-cache',
        }

    @property
    def base_params(self):
        """
        Basic params for api call. Since we
        """
        return {
            'datasource': 'tranquility',
        }

    def get(self, url: str, extra_params: dict = None):
        """
        Base synchronous get method.
        """
        params = self.base_params
        if extra_params:
            params = {**self.base_params, **extra_params}
        try:
            response = httpx.get(
                url=url,
                params=params,
                headers=self.headers,
            )
            return response
        except Exception as e:
            self.logger.error(f':Exception in {BaseClient.get.__qualname__}: {e}')
            return None

    def post(self, url: str, extra_data: dict, extra_params: dict = None):
        """
        Base synchronous post method.
        """
        params = self.base_params
        if extra_params:
            params = {**self.base_params, **extra_params}
        try:
            response = httpx.post(
                url=url,
                params=params,
                headers=self.headers,
                json=extra_data,
            )
            return response
        except Exception as e:
            self.logger.error(f':Exception in {BaseClient.post.__qualname__}: {e}')
            return None
