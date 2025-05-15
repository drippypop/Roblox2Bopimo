# this is VERY VERY outdated and no longer maintained, if you use this expect it to not work

# Roblox2Bopimo

**Roblox2Bopimo** is a tool that helps convert Roblox `.rbxlx` files into a format that works with Bopimo. It takes Roblox levels and turns them into BOPJSON, so you can use them in Bopimo.

## How it works

- It parses `.rbxlx` files and extracts essential data, including block positions, sizes, colors, and rotations.
- It then generates a `.bopjson` file that’s fully formatted and ready to be integrated into your level.

## Requirements

- Python 3.x

## Installation

1. **Download or Clone** this repo to your computer.
2. Make sure you have **Python 3.x** installed. You can get it from [python.org](https://www.python.org/downloads/).

## Usage

1. Place the script `Roblox2Bopimo.py` in the folder with your `.rbxlx` files.
2. Run the script with the following command:

   ```bash
   python Roblox2Bopimo.py
   ```

3. The script will show all the `.rbxlx` files in the folder. Pick the one you want to convert by entering the corresponding number.
4. Once you select the file, the script will process it and save a `.bopjson` file with the same name in the directory.
   
### Example:

If you have a file called `level1.rbxlx`, after running the script, you'll get `level1.bopjson` as the output.

## Output Structure

The output `.bopjson` file will look something like this:

```json
{
  "GAME_VERSION": "1.0.3",
  "TIME_OF_SAVE": "2024-12-14 21:46:06",
  "level_blocks": [
    {
      "__gdtype": "Dictionary",
      "pairs": [
        {
          "key": {"__gdtype": "StringName", "name": "uid"},
          "value": "unique_block_id"
        },
        {
          "key": {"__gdtype": "StringName", "name": "block_id"},
          "value": 0
        },
        {
          "key": {"__gdtype": "StringName", "name": "block_name"},
          "value": "BlockName"
        },
        {
          "key": {"__gdtype": "StringName", "name": "block_color"},
          "value": {
            "__gdtype": "Color",
            "values": [0.5, 0.5, 0.5, 1]
          }
        },
        {
          "key": {"__gdtype": "StringName", "name": "block_position"},
          "value": {
            "__gdtype": "Vector3",
            "values": [0.0, 10.0, 0.0]
          }
        },
        {
          "key": {"__gdtype": "StringName", "name": "block_rotation"},
          "value": {
            "__gdtype": "Vector3",
            "values": [0.0, 90.0, 0.0]
          }
        },
        {
          "key": {"__gdtype": "StringName", "name": "block_scale"},
          "value": {
            "__gdtype": "Vector3",
            "values": [1.0, 1.0, 1.0]
          }
        }
      ]
    }
  ]
}
```

### Key Elements:
  - `level_blocks`: A list of blocks in the level, with details like:
  - `block_id`: Currently set to `0`, representing a block type.
  - `block_name`: The name of the block.
  - `block_color`: The block’s color (RGBA).
  - `block_position`: The block’s position in 3D space.
  - `block_rotation`: The block’s rotation (Euler angles in degrees).
  - `block_scale`: The size of the block.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

Feel free to fork the repo, report issues, or suggest improvements. Pull requests are always welcome!
