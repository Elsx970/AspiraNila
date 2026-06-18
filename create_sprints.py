import os
import shutil

source_dir = "."
base_dest = "../Agile_Sprints"

def ignore_files(dir, contents):
    # Ignore build artifacts and git to save space
    return ['.git', 'build', '.dart_tool', '.pub-cache']

def create_sprint(sprint_name, is_mock):
    dest = os.path.join(base_dest, sprint_name)
    print(f"Creating {sprint_name}...")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source_dir, dest, ignore=ignore_files)
    
    # Modify config.dart to simulate progression
    config_path = os.path.join(dest, 'lib', 'core', 'config.dart')
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if is_mock:
            content = content.replace('static const bool useMockMode = false;', 'static const bool useMockMode = true;')
        
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(content)

if not os.path.exists(base_dest):
    os.makedirs(base_dest)

print("Mulai memperbarui folder Agile Sprints dengan kode terbaru...")

# Tahap 1: Setup & UI Mockup (Gunakan Mock Mode)
create_sprint("1_Sprint_Setup_and_UI_Mockup", is_mock=True)

# Tahap 2: Database Connectivity (Mock Mode False)
create_sprint("2_Sprint_Database_and_Auth", is_mock=False)

# Tahap 3: Aspirasi Features 
create_sprint("3_Sprint_Aspirasi_Feature", is_mock=False)

# Tahap 4: Final Polish & Admin Fixes
create_sprint("4_Sprint_Final_Release", is_mock=False)

print("Selesai! Folder Agile_Sprints berhasil diperbarui.")
