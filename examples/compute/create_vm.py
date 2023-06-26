from keystoneauth1 import identity
from keystoneauth1 import session
from neutronclient.v2_0 import client
from keystoneclient.v3 import client as keystone_client

from novaclient import client as nova_client
from novaclient import exceptions as nova_exceptions


username='admin'
password='sBPKGOLzOflJshNrVpDWuFOJnKnSEPWZrQRuq923'
project_name='admin'
project_domain_id='default'
user_domain_id='default'
auth_url='http://192.168.56.10:5000/v3'

provider_network_id = "a0336d25-77a7-40b2-b46c-48fdecd4d1df"

auth = identity.Password(auth_url=auth_url,
                         username=username,
                         password=password,
                         project_name=project_name,
                         project_domain_id=project_domain_id,
                         user_domain_id=user_domain_id)

sess = session.Session(auth=auth)

# if you are not in controller node, use publicURL as endpoint_type, else for security, use internalURL
# publicURL endpoint is accessable from internet, in production, we don't expose it to internet
nova = nova_client.Client("2.6", session=sess,region_name="RegionOne",endpoint_type='publicURL')

networks = [{"net-id":provider_network_id}]
#user provided vm password
password = "mypasswd"

#used for set init ssh login password for vm
userdata = "#cloud-config\npassword: %s\nchpasswd: { expire: False }\nssh_pwauth: True" %(password)

image_uuid = "e2e14247-dada-4088-b705-50804bb978fb"

block_device_mapping_v2 = {'boot_index': 0,
                           'source_type': 'image',
                           'uuid': image_uuid,
                           'volume_size':10,
                           #'volume_type': 'LUKS',
                           'destination_type': 'volume',
                           'delete_on_termination': False}

server = nova.servers.create(name="vm1",
                             image="",
                             flavor="2",
                             block_device_mapping_v2 = [block_device_mapping_v2],
                             nics=networks,
                             userdata=userdata)
