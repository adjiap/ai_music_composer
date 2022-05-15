# -*- coding: utf-8 -*-
from pathlib import Path
from typing import List, Optional, Union

def get_all_midis(optional_path: Optional[Union[str, Path]]= None) -> List[Path]:
    if optional_path:
        midi_files = Path(optional_path).rglob("*.mid")
    else:
        midi_files = Path.cwd().rglob("*.mid")
    return midi_files

if __name__ == "__main__":
    for midi in get_all_midis():
        print(midi)
    