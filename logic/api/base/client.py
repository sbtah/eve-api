import httpx
from logic.settings import endpoints
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

    def get_types(self, page_number: int = 1):
        params = {
            'page': page_number
        }
        res = self.get(url=endpoints.UNIVERSE_TYPES, extra_params=params)
        return res.json()


# ALIANCES = "https://login.eveonline.com/v2/oauth/authorize"
# TYPES = "https://esi.evetech.net/latest/universe/types"

# json_data = [
#     95465499,

# ]


# def get_types():
#     headers = {
#     'accept': 'application/json',
#     'Content-Type': 'application/json',
#     'Cache-Control': 'no-cache',
#     }
#     params = {
#         'datasource': 'tranquility',
#         'page': '1',
#     }
#     response = requests.get('https://esi.evetech.net/latest/universe/types', params=params, headers=headers)
#     return response.json()


# def get_names(ids_list: list):
#     headers = {
#     'accept': 'application/json',
#     'Content-Type': 'application/json',
#     'Cache-Control': 'no-cache',
#     }
#     params = {
#     'datasource': 'tranquility',
#     'page': '1',
#     }
#     response = requests.post('https://esi.evetech.net/latest/universe/names/', params=params, headers=headers, json=ids_list)
#     return response.json()


# print(get_names([3567,]))
# # print(get_types())

# def get_names_for_types():
#     types_response = get_types()
#     if types_response:
#         names_response = get_names(types_response)
#         return names_response

# # print(get_names_for_types())