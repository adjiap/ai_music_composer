# -*- coding: utf-8 -*-
from midi_handler import MidiHandler

from mido import MidiFile, MetaMessage

if __name__ == "__main__":
    cleaned_midi_files = MidiHandler.clean_broken_midi(MidiHandler.get_all_midis(r"D:\Data\Online Download\midi_test_files"))
    for midi_path in cleaned_midi_files:
        midi_file = MidiFile(midi_path)
        for msg in midi_file.tracks[0]:
            if isinstance(msg, MetaMessage):
                print("---")
                print(msg)
