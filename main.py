from logic.api.base.client import BaseClient
from logic.api.eve.client import EvEApiClient
from logic.settings import endpoints


client = EvEApiClient()

regions_ids = client.get_region_id(11000029)
print(regions_ids)
