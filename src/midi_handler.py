# -*- coding: utf-8 -*-

from pathlib import Path
import shutil
from typing import Generator, List, Optional, Union

from mido import MidiFile
class MidiHandler(object):
    
    def get_all_midis(optional_path: Optional[Union[str, Path]]= None) -> Generator[Path, None, None]:
        if optional_path:
            midi_files = Path(optional_path).rglob("*.mid")
        else:
            midi_files = Path.cwd().rglob("*.mid")
        return midi_files

    def clean_broken_midi(midi_files_gen: Generator[Path, None, None], optional_archive_path: Optional[Union[str, Path]]= None) -> List[Path]:
        cleaned_midi_paths = [] # type: List[Path]
        while True:
            midi_path = next(midi_files_gen, "end")
            if midi_path == "end":
                break
            try:
                MidiFile(midi_path, clip=True)
                cleaned_midi_paths.append(midi_path)
            except EOFError:
                broken_archive_folder = optional_archive_path if optional_archive_path else Path(__file__).parent / "midi_src" / "broken_midi"
                if not broken_archive_folder.exists():
                    broken_archive_folder.mkdir(parents=True, exist_ok=True)
                shutil.move(midi_path, broken_archive_folder / midi_path.name)
        return cleaned_midi_paths

    def clean_duplicate_tracks(midi_file: MidiFile, optional_archive_path: Optional[Union[str, Path]]= None) -> List[Path]:
        message_numbers = []
        duplicates = []
        
        for track in midi_file.tracks:
            if len(track) in message_numbers:
                duplicates.append(track)
            else:
                message_numbers.append(len(track))
        
        for track in duplicates:
            midi_file.tracks.remove(track)
        
        midi_file.save("")
