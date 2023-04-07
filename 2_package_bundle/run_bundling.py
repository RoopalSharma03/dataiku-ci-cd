import dataiku-api-client
# from dataikuapi import DSSClient
import sys
from datetime import datetime

host = sys.argv[1]
apiKey = sys.argv[2]
project = sys.argv[3]
bundle_id = sys.argv[4]

client = dataiku-api-client.DSSClient(host,apiKey )
test_project = client.get_project(project)

test_project.export_bundle(bundle_id)
# Publish bundle to Project Deployer
test_project.publish_bundle(bundle_id)

# Optional - Export the bundel zip to be archived
test_project.download_exported_bundle_archive_to_file(bundle_id, bundle_id + ".zip")
