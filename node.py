from mido import Message, MidiFile, MidiTrack
import os


class node():
    def __init__(self, note):
        self.note = note
        self.velocity = 64

    def add_to_track(self, track, beat):
        bpm=60
        time=int(60*60*10/bpm)
        base_node = 48 #c3
        track.append(Message("note_on", note=base_node+self.note, velocity=self.velocity, time=0, channel=0))
        track.append(Message("note_off", note=base_node+self.note, velocity=self.velocity, time=time*beat, channel=0))