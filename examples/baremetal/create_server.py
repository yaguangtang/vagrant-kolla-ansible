from keystoneauth1 import identity
from keystoneauth1 import session
from neutronclient.v2_0 import client
from keystoneclient.v3 import client as keystone_client
from novaclient import client as nova_client

username='admin'
password='sBPKGOLzOflJshNrVpDWuFOJnKnSEPWZrQRuq923'
project_name='admin'
project_domain_id='default'
user_domain_id='default'
auth_url='http://192.168.56.10:5000/v3'

provider_network_id = "963dca13-bf19-4577-8fe5-83ff2056dcd7"

auth = identity.Password(auth_url=auth_url,
                         username=username,
                         password=password,
                         project_name=project_name,
                         project_domain_id=project_domain_id,
                         user_domain_id=user_domain_id)
sess = session.Session(auth=auth)

# if you are not in controller node, use publicURL as endpoint_type, else for security, use internalURL
# publicURL endpoint is accessable from internet, in production, we don't expose it to internet
nova = nova_client.Client("2.6", session=sess,region_name="RegionTwo",endpoint_type='publicURL')

networks = [{"net-id":provider_network_id}]
password = "mypasswd"

#used for set init ssh login password for vm
userdata = "#cloud-config\npassword: mypasswd\nchpasswd: { expire: False }\nssh_pwauth: True"

image_uuid = "e2e14247-dada-4088-b705-50804bb978fb"

#the baremetal server flavor has to be custom flavors for baremetal service
server = nova.servers.create(name="physicalvm1",
                             image="e2e14247-dada-4088-b705-50804bb978fb",
                             flavor="37b6d853-6537-4a82-a8ec-466c7668d42c",
                             nics=networks,
                             userdata=userdata)
