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

volume_id = 'cfaf65d3-5d02-4c01-9f6c-49ff72335a6d'

backup = cinder.backups.create(volume_id=volume_id,name="vol1-backup",force=True,description="vol1 backup")

backup = cinder.backups.get(backup.id)
while backup.status == 'creating':
    backup = cinder.backups.get(backup.id)

# Check the backup status
if backup.status == 'available':
    print("Volume backup created successfully!")
else:
    print("Failed to create volume backup.")

# Retrieve the backup details
print("Backup ID: ", backup.id)
print("Backup Name: ", backup.name)
print("Backup Description: ", backup.description)
print("Backup Status: ", backup.status)
print("Backup Created At: ", backup.created_at)
print("Backup Size: ", backup.size)
