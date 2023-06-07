import re
import os
import flywheel

fw = flywheel.Client(os.environ.get('FW_KEY'))
# =================================================================
file ='/MR.yaml' #classification file
for project in fw.projects():
  if re.match('.*_v2',project.label): #identify flywheel projects
   print('%s: %s' % (project.id, project.label))
   fw.upload_file_to_project(project.id,file) # upload classiciation file


