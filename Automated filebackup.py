import os
import shutil
import datetime
import schedule
import time

source_dir = "c:/users/hp/pictures/screenshots"
destination_dir = "c:/users/hp/Desktop/Backups"

def copy_folder_to_directory(source, dest):
  today = datetime.date.today()
  dest_dir = os.path.join(dest,str(today))
  
  try:
    shutil.copytree(source, dest_dir)
    print(f"folder copied to: {dest_dir}")
  except FileExsistError:
    print(f"folder already exists: {dest_dir}")
    
def l():
    copy_folder_to_directory(source_dir, destination_dir)
schedule.every().day.at("6:55").do(1)

while True:
  schedule.run_pending()
  time.sleep(60)
  

