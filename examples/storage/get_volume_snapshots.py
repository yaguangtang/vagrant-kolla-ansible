from keystoneauth1 import identity
from keystoneauth1 import session
from neutronclient.v2_0 import client
from keystoneclient.v3 import client as keystone_client

from cinderclient.v3 import client as cinder_client

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
cinder = cinder_client.Client(3, session=sess,region_name="RegionOne",endpoint_type='publicURL')

volume_id = 'ed6b5d93-dbc2-4048-b11d-0241a2e6fd68'

snapshots = cinder.volume_snapshots.list(search_opts={'volume_id':volume_id})

for snapshot in snapshots:
    print('Snapshot ID: {}'.format(snapshot.id))
    print('Snapshot Name: {}'.format(snapshot.name))
    # You can also access other attributes of the snapshot, such as status, created_at, etc.
    print('Snapshot Status: {}'.format(snapshot.status))
    print('Snapshot Created At: {}'.format(snapshot.created_at))
    print('Snapshot Size: {} GB'.format(snapshot.size))
