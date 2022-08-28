from mido import Message, MidiFile, MidiTrack
import os
def play_note(note, velocity, track, beat):
    bpm=60
    time=int(60*60*10/bpm)
    base_node = 48 #c3
    track.append(Message("note_on", note=base_node+note, velocity=velocity, time=0, channel=0))
    track.append(Message("note_off", note=base_node+note, velocity=velocity, time=time*beat, channel=0))


if __name__ =="__main__":
    mid=MidiFile()
    track=MidiTrack()
    track.append(Message("program_change", channel=0, program=2, time=0))
    play_note(0, 64, track, 1)
    play_note(0, 64, track, 1)
    play_note(7, 64, track, 1)
    play_note(7, 64, track, 1)
    play_note(9, 64, track, 1)
    play_note(9, 64, track, 1)
    play_note(7, 64, track, 2)

    play_note(5, 64, track, 1)
    play_note(5, 64, track, 1)
    play_note(4, 64, track, 1)
    play_note(4, 64, track, 1)
    play_note(2, 64, track, 1)
    play_note(2, 64, track, 1)
    play_note(0, 64, track, 1)

    mid.tracks.append(track)
    os.remove("test.mid")
    mid.save("test.mid")



