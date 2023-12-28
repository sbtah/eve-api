from logic.api.base.client import BaseClient
from logic.settings import endpoints

client = BaseClient()

regions_ids = client.get(url=endpoints.UNIVERSE_SINGLE_REGION.format(region_id=10000001)).json()
print(regions_ids)

# print(client.post(url=UNIVERSE_NAMES, extra_data=regions_ids).json())
