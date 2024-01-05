from logic.api.base.client import BaseClient
from logic.settings import endpoints


class EvEApiClient(BaseClient):
    """
    Specialized EvE Api Client that utilizes some of the ESI Endpoints.
    """

    def __init__(self):
        super().__init__()

    def get_regions_ids(self) -> list | None:
        """
        Request UNIVERSE_REGIONS endpoint.
        Return list of regions IDS.
        """
        regions_response = self.get(url=endpoints.UNIVERSE_REGIONS)
        if regions_response is not None:
            return regions_response.json()
        self.logger.error('Received no response from UNIVERSE_REGIONS endpoint.')
        return None

    def get_region_id(self, region_id: int):
        """
        Request UNIVERSE_SINGLE_REGION endpoint.
        Return region specific data.
        """
        region_response = self.get(url=endpoints.UNIVERSE_SINGLE_REGION.format(region_id=region_id))
        if region_response is not None:
            return region_response.json()
        self.logger.error('Received no response from UNIVERSE_SINGLE_REGION endpoint.')
        return None

    def get_types_ids(self, page_num: int = None) -> list | None:
        """
        Request UNIVERSE_TYPES endpoint.
        Return list of types IDS.
        """
        extra_params = {
            'page': page_num,
        }
        types_response = self.get(url=endpoints.UNIVERSE_TYPES, extra_params=extra_params)
        if types_response is not None:
            return types_response.json()
        self.logger.error('Received no response from UNIVERSE_TYPES endpoint.')
        return None

    def get_type_id(self, type_id: int) -> dict | None:
        """
        Request UNIVERSE_SINGLE_TYPE endpoint.
        Return type specific data.
        """
        type_response = self.get(url=endpoints.UNIVERSE_SINGLE_TYPE.format(type_id=type_id))
        if type_response is not None:
            return type_response.json()
        self.logger.error('Received no response from UNIVERSE_SINGLE_TYPE endpoint.')
        return None
