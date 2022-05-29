# -*- coding: utf-8 -*-

import pytest
from midi_handler import get_all_midis

class TestMidiHandler():
    
    @pytest.mark.skip(reason="Not yet implemented")
    def test_get_all_midis(self,):
        raise NotImplementedError

    @pytest.mark.skip(reason="Not yet implemented")
    def test_clean_duplicate_tracks(self,):
        raise NotImplementedError
    
    @pytest.mark.skip(reason="Not yet implemented")
    def test_clean_broken_midi(self,):
        raise NotImplementedError
    
if __name__ == '__main__':
    pytest.main()
