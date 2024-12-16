import xml.etree.ElementTree as ET
import json
import math
import os

def rotation_matrix_to_euler(matrix):
    r00, r01, r02 = matrix[0]
    r10, r11, r12 = matrix[1]
    r20, r21, r22 = matrix[2]

    pitch = math.asin(-r20)
    yaw = math.atan2(r10, r00)
    roll = math.atan2(r21, r22)

    return [math.degrees(roll), math.degrees(pitch), math.degrees(yaw)]

def parse_rbxlx(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    level_data = {
        "GAME_VERSION": "1.0.3",
        "TIME_OF_SAVE": "2024-12-14 21:46:06",
        "level_blocks": [],
        "level_death_plane": -1000,
        "level_description": "",
        "level_fog_color": {"__gdtype": "Color", "values": [0.5, 0.5, 0.5, 1]},
        "level_fog_distance": 0,
        "level_fog_enabled": False,
        "level_gravity": 85,
        "level_lives": 0,
        "level_music": {"__gdtype": "PackedInt32Array", "values": [0, 1, 2]},
        "level_name": "drippy",
        "level_players_damage_players": True,
        "level_sky": 0,
        "level_sky_energy": 1,
        "level_weather": 0
    }

    for item in root.findall('.//Item[@class="Part"]'):
        properties = item.find('Properties')

        cframe = properties.find('CoordinateFrame')
        position = [
            float(cframe.find('X').text),
            float(cframe.find('Y').text),
            float(cframe.find('Z').text)
        ]

        size = properties.find('Vector3[@name="size"]')
        block_size = [
            float(size.find('X').text),
            float(size.find('Y').text),
            float(size.find('Z').text)
        ]

        color3uint8_element = properties.find('Color3uint8[@name="Color3uint8"]')
        if color3uint8_element is not None:
            color3uint8 = int(color3uint8_element.text)
            r = (color3uint8 >> 16) & 0xFF
            g = (color3uint8 >> 8) & 0xFF
            b = color3uint8 & 0xFF
            color = [r / 255, g / 255, b / 255, 1]
        else:
            color = [0, 0, 0, 1]  # default to black if not found

        rotation_matrix = [
            [float(cframe.find('R00').text), float(cframe.find('R01').text), float(cframe.find('R02').text)],
            [float(cframe.find('R10').text), float(cframe.find('R11').text), float(cframe.find('R12').text)],
            [float(cframe.find('R20').text), float(cframe.find('R21').text), float(cframe.find('R22').text)],
        ]
        rotation = rotation_matrix_to_euler(rotation_matrix)

        block_data = {
            "__gdtype": "Dictionary",
            "pairs": [
                {"key": {"__gdtype": "StringName", "name": "block_id"}, "value": 0},  # All treated as blocks, only temporary while i work out shapes
                {"key": {"__gdtype": "StringName", "name": "block_name"}, "value": properties.find('string[@name="Name"]').text},
                {"key": {"__gdtype": "StringName", "name": "block_color"}, "value": {
                    "__gdtype": "Color", "values": color
                }},
                {"key": {"__gdtype": "StringName", "name": "block_position"}, "value": {
                    "__gdtype": "Vector3", "values": position
                }},
                {"key": {"__gdtype": "StringName", "name": "block_rotation"}, "value": {
                    "__gdtype": "Vector3", "values": rotation
                }},
                {"key": {"__gdtype": "StringName", "name": "block_scale"}, "value": {
                    "__gdtype": "Vector3", "values": block_size
                }},
                {"key": "position_enabled", "value": False},
                {"key": "position_points", "value": {"__gdtype": "PackedVector3Array", "values": []}},
                {"key": "position_travel_speed", "value": 5},
                {"key": "rotation_enabled", "value": False},
                {"key": "rotation_pivot_offset", "value": {"__gdtype": "Vector3", "values": [0, 0, 0]}},
                {"key": "rotation_direction", "value": {"__gdtype": "Vector3", "values": [0, 0, 0]}},
                {"key": "rotation_speed", "value": 1},
                {"key": {"__gdtype": "StringName", "name": "transparency"}, "value": 7},
                {"key": {"__gdtype": "StringName", "name": "collision_enabled"}, "value": True},
                {"key": {"__gdtype": "StringName", "name": "transparency_enabled"}, "value": False}
            ]
        }
        level_data["level_blocks"].append(block_data)

    return level_data

def save_to_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

def choose_rbxlx_file():
    files = [f for f in os.listdir('.') if f.endswith('.rbxlx')]
    
    if not files:
        print("No .rbxlx files found in the current directory.")
        return None
    
    print("Choose a .rbxlx file to process:")
    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {file}")
    
    choice = input("Enter the number of the file you want to process: ")
    try:
        chosen_file = files[int(choice) - 1]
        return chosen_file
    except (ValueError, IndexError):
        print("Invalid choice.")
        return None

input_file_path = choose_rbxlx_file()
if input_file_path:
    output_file_path = f"{input_file_path.split('.')[0]}.bopjson"
    level_data = parse_rbxlx(input_file_path)
    save_to_json(level_data, output_file_path)
    print(f"Data saved to {output_file_path}")
