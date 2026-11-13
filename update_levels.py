#!/usr/bin/env python3
import os
import re
import shutil

src_dir = "/opt/circlemud/circle-3.1/src"
structs_file = os.path.join(src_dir, "structs.h")
class_file = os.path.join(src_dir, "class.c")

def main():
    print(f"Targeting source directory: {src_dir}")
    if not os.path.exists(structs_file) or not os.path.exists(class_file):
        print("Error: Could not find structs.h or class.c in /opt/circlemud/circle-3.1/src. Make sure the path is correct.")
        return

    # Backups
    shutil.copy(structs_file, structs_file + ".bak")
    shutil.copy(class_file, class_file + ".bak")
    print("Created backups: structs.h.bak, class.c.bak")

    # 1. Update structs.h
    with open(structs_file, "r") as f:
        s_data = f.read()
    
    old_levels = r'#define LVL_IMPL\s+\d+.*?#define LVL_FREEZE\s+LVL_GRGOD'
    new_levels = """#define LVL_IMPL\t105
#define LVL_GRGOD\t104
#define LVL_GOD\t\t103
#define LVL_BUILDER\t102
#define LVL_IMMORT\t101
#define LVL_DEMIGOD\t100

/* Level of the 'freeze' command */
#define LVL_FREEZE\tLVL_GRGOD"""

    if "#define LVL_IMPL\t105" not in s_data:
        s_data = re.sub(old_levels, new_levels, s_data, flags=re.DOTALL)
        with open(structs_file, "w") as f:
            f.write(s_data)
        print("Successfully updated structs.h (Levels 1-105)")
    else:
        print("structs.h already has LVL_IMPL set to 105. Skipping.")

    # 2. Update class.c
    with open(class_file, "r") as f:
        c_lines = f.readlines()

    out_lines = []
    in_titles = False
    level_count = 0
    last_xp = 0

    for line in c_lines:
        if "const struct title_type titles[NUM_CLASSES]" in line:
            in_titles = True
            out_lines.append(line)
            continue
        
        if in_titles:
            if "};" in line and level_count == 0:
                in_titles = False
                out_lines.append(line)
                continue
                
            if "{" in line and "}" in line and "const" not in line:
                level_count += 1
                out_lines.append(line)
                
                match = re.search(r'(\d+)', line.split(',')[-1])
                if match:
                    last_xp = int(match.group(1))

                # Inject levels 31-105 right after level 30 (which is the 31st element)
                if level_count == 31: 
                    xp = last_xp
                    for lvl in range(31, 100):
                        xp += 500000
                        out_lines.append(f'    {{"Mortal Legend", "Mortal Legend", {xp}}}, /* Level {lvl} */\n')
                    
                    out_lines.append(f'    {{"Demigod", "Demigoddess", {xp + 1000000}}}, /* Level 100 */\n')
                    out_lines.append(f'    {{"Immortal", "Immortal", {xp + 2000000}}}, /* Level 101 */\n')
                    out_lines.append(f'    {{"Builder", "Builder", {xp + 3000000}}}, /* Level 102 */\n')
                    out_lines.append(f'    {{"God", "Goddess", {xp + 4000000}}}, /* Level 103 */\n')
                    out_lines.append(f'    {{"Greater God", "Greater Goddess", {xp + 5000000}}}, /* Level 104 */\n')
                    out_lines.append(f'    {{"Implementor", "Implementress", {xp + 6000000}}}, /* Level 105 */\n')
                    
                # Discard the original immortal levels (31-34) from array
                if level_count > 31 and level_count <= 35:
                    out_lines.pop() 
                    
                if level_count == 35:
                    level_count = 0
            else:
                out_lines.append(line)
        else:
            out_lines.append(line)

    # Simple validation before writing
    if any("Level 105" in l for l in out_lines):
        with open(class_file, "w") as f:
            f.writelines(out_lines)
        print("Successfully updated class.c (Expanded arrays to 105)")
    else:
        print("class.c titles array already expanded or unreadable. Skipping.")
        
    print("\nUpdate complete. Run 'make clean && make' in your src directory!")

if __name__ == "__main__":
    main()
