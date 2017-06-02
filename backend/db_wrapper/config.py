import sys
import os
sys.path.append(os.path.dirname(__file__))
import configparser
from main import *

# Start the Database Connection
config = configparser.ConfigParser()
config.read('setting.conf')
database_config = config['database']
connection_string = database_config['server'] + '://' +  database_config['user'] + ':' \
                    + database_config['password'] + '@' + database_config['address'] + '/' \
                    + database_config['database'] + database_config['extra']


provider = ConnectionProvider(connection_string)
configure_provider(provider)
provider.start()
engine = provider._engine

#neutron_config = config['neutron_database']
#neutron_connection_string = neutron_config['server'] + '://' +  neutron_config['user'] + ':' \
#                    + neutron_config['password'] + '@' + neutron_config['address'] + '/' \
#                    + neutron_config['database'] + neutron_config['extra']

#configure_neutron_engine(neutron_connection_string)
