from keystoneauth1 import identity
from keystoneauth1 import session
from neutronclient.v2_0 import client
from keystoneclient.v3 import client as keystone_client

from cinderclient.v3 import client as cinder_client
from cinderclient import api_versions

username='admin'
password='sBPKGOLzOflJshNrVpDWuFOJnKnSEPWZrQRuq923'
project_name='admin'
project_domain_id='default'
user_domain_id='default'
auth_url='http://192.168.56.10:5000/v3'
provider_network_id = "a85131d4-c18e-4a34-862c-c27540cfbad3"

auth = identity.Password(auth_url=auth_url,
                         username=username,
                         password=password,
                         project_name=project_name,
                         project_domain_id=project_domain_id,
                         user_domain_id=user_domain_id)
sess = session.Session(auth=auth)

# if you are not in controller node, use publicURL as endpoint_type, else for security, use internalURL
# publicURL endpoint is accessable from internet, in production, we don't expose it to internet
cinder = cinder_client.Client(api_version=api_versions.APIVersion("3.40"), session=sess,region_name="RegionOne",endpoint_type='publicURL')

# snapshot should be the latest created of the volume to be reverted
# volume to be reverted should be in available status, not attached by VM
snapshot_id = 'f278b62d-4a13-49e3-aea9-6f561e0a2adc'

volume = cinder.volumes.revert_to_snapshot("5e302221-d3d1-4749-a53a-d8287530c51f",snapshot_id)
