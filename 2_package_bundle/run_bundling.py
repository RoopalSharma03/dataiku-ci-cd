import dataikuapi

import sys

from datetime import datetime

import os




host = sys.argv[1]

apiKey = sys.argv[2]

project = sys.argv[3]

bundle_id = sys.argv[4]

auto_host = sys.argv[5]

auto_apiKey = sys.argv[6]




client = dataikuapi.DSSClient(host,apiKey )

auto_client = dataikuapi.DSSClient(auto_host,auto_apiKey)

test_project = client.get_project(project)

auto_test_deployer = auto_client.get_projectdeployer()




test_project.export_bundle(bundle_id)





# Optional - Export the bundel zip to be archived

test_project.download_exported_bundle_archive_to_file(bundle_id, bundle_id + ".zip")





with test_project.get_exported_bundle_archive_stream(bundle_id) as fp:

    auto_test_deployer.upload_bundle(fp.content)
