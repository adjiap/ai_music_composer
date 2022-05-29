# -*- coding: utf-8 -*-
from midi_handler import MidiHandler

from mido import MidiFile, MetaMessage

if __name__ == "__main__":
    cleaned_midi_files = MidiHandler.clean_broken_midi(MidiHandler.get_all_midis())
    for midi_path in cleaned_midi_files:
        midi_file = MidiFile(midi_path, clip=True)
        for msg in midi_file.tracks[0]:
            if isinstance(msg, MetaMessage):
                print(msg)
