import dataikuapi
import sys

#Define the connections

#Design
host = sys.argv[1]
apiKey = sys.argv[2]

#Automation
host_auto = "https://prod-dataiku-cloud-automation.ren.apps.ge.com" # example to be changed
apiKey_auto = "lZ5gd7KdpU65eMHHoHT83HQI2Ivb12Jl" # example to be changed

design_client= dataikuapi.DSSClient(host, apiKey)
auto_client = dataikuapi.DSSClient(host_auto, apiKey_auto)

version_bundle = "bundle_v1"
#Export bundle
project = design_client.get_project(sys.argv[3])
project.export_bundle(version_bundle)
project.download_exported_bundle_archive_to_file(version_bundle, "temp_bundle.zip")

#Import bundle
project_automation = auto_client.get_project(sys.argv[3])
project_automation.import_bundle_from_archive("temp_bundle.zip")

# Preload and activate bundle
project_automation.preload_bundle(version_bundle) # for code envs
project_automation.activate_bundle(version_bundle)

