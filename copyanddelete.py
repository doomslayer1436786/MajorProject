import shutil
import os



def copy_and_delete_folder():
    
    src_folder = r'.//runs//classify//predict'
    dest_folder = r'.//static//detections'

    if not os.path.exists(src_folder):
        #print(f"Source folder '{src_folder}' does not exist.")
        return

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"Destination folder '{dest_folder}' created.")

    try:
        for item in os.listdir(src_folder):
            src_item = os.path.join(src_folder, item)
            dest_item = os.path.join(dest_folder, item)

            if os.path.isdir(src_item):
                shutil.copytree(src_item, dest_item)
            else:
                shutil.copy2(src_item, dest_item)
            

       # print(f"All files from '{src_folder}' copied to '{dest_folder}'.")


        shutil.rmtree("runs")
        return str(dest_item)
        #print(f"Source folder '{src_folder}' deleted.")

    except Exception as e:
        print(f"Error occurred: {e}")
    
    


copy_and_delete_folder()