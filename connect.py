#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#
import os
from dotenv import load_dotenv
import logging
# Importing models and REST client class from Community Edition version
from tb_rest_client32.rest_client_pe import *
from tb_rest_client32.rest import ApiException
import numpy as np

load_dotenv()


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(module)s - %(lineno)d - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# ThingsBoard REST API URL
url = os.getenv('TB_URL')

# Default Tenant Administrator credentials
username = os.getenv('TB_USERNAME')
password = os.getenv('TB_PASSWORD')

# Creating the REST client object with context manager to get auto token refresh
with RestClientPE(base_url=url) as rest_client:
    try:
        # Auth with credentials
        rest_client.login(username=username, password=password)

        # Getting current user
        current_user = rest_client.get_user()

        # for i in np.arange(24.0, 63.0,0.1):
        # for i in range(61):
        rest_client.telemetry_controller.delete_entity_timeseries_using_delete('DEVICE', os.getenv('TB_DEVICE_ID'),"60ETemperature3", delete_all_data_for_keys='true', rewrite_latest_if_deleted='false')
        rest_client.telemetry_controller.delete_entity_timeseries_using_delete('DEVICE', os.getenv('TB_DEVICE_ID'),"BLEB", delete_all_data_for_keys='true', rewrite_latest_if_deleted='false')
        rest_client.telemetry_controller.delete_entity_timeseries_using_delete('DEVICE', os.getenv('TB_DEVICE_ID'),"BLEH", delete_all_data_for_keys='true', rewrite_latest_if_deleted='false')
        rest_client.telemetry_controller.delete_entity_timeseries_using_delete('DEVICE', os.getenv('TB_DEVICE_ID'),"BLET", delete_all_data_for_keys='true', rewrite_latest_if_deleted='false')
        
        # # Creating an Asset
        # asset = Asset(name="Building 1", type="building")
        # asset = rest_client.save_asset(asset)

        # logging.info("Asset was created:\n%r\n", asset)

        # # creating a Device
        # device = Device(name="Thermometer 1", type="thermometer")
        # device = rest_client.save_device(device)

        # logging.info(" Device was created:\n%r\n", device)

        # # Creating relations from device to asset
        # relation = EntityRelation(_from=asset.id, to=device.id, type="Contains")
        # relation = rest_client.save_relation(relation)

        # logging.info(" Relation was created:\n%r\n", relation)
    except ApiException as e:
        logging.exception(e)
