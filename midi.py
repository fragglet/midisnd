#!/usr/bin/env python
#
# Copyright (c) 2015, Simon Howard
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

INSTRUMENTS = [
	"Acoustic Grand Piano", "Bright Acoustic Piano",
	"Electric Grand Piano", "Honky-tonk Piano", "Electric Piano 1",
	"Electric Piano 2", "Harpsichord", "Clavi", "Celesta", "Glockenspiel",
	"Music Box", "Vibraphone", "Marimba", "Xylophone", "Tubular Bells",
	"Dulcimer", "Drawbar Organ", "Percussive Organ", "Rock Organ",
	"Church Organ", "Reed Organ", "Accordion", "Harmonica",
	"Tango Accordion", "Acoustic Guitar (nylon)",
	"Acoustic Guitar (steel)", "Electric Guitar (jazz)",
	"Electric Guitar (clean)", "Electric Guitar (muted)",
	"Overdriven Guitar", "Distortion Guitar", "Guitar harmonics",
	"Acoustic Bass", "Electric Bass (finger)", "Electric Bass (pick)",
	"Fretless Bass", "Slap Bass 1", "Slap Bass 2", "Synth Bass 1",
	"Synth Bass 2", "Violin", "Viola", "Cello", "Contrabass",
	"Tremolo Strings", "Pizzicato Strings", "Orchestral Harp", "Timpani",
	"String Ensemble 1", "String Ensemble 2", "SynthStrings 1",
	"SynthStrings 2", "Choir Aahs", "Voice Oohs", "Synth Voice",
	"Orchestra Hit", "Trumpet", "Trombone", "Tuba", "Muted Trumpet",
	"French Horn", "Brass Section", "SynthBrass 1", "SynthBrass 2",
	"Soprano Sax", "Alto Sax", "Tenor Sax", "Baritone Sax", "Oboe",
	"English Horn", "Bassoon", "Clarinet", "Piccolo", "Flute", "Recorder",
	"Pan Flute", "Blown Bottle", "Shakuhachi", "Whistle", "Ocarina",
	"Lead 1 (square)", "Lead 2 (sawtooth)", "Lead 3 (calliope)",
	"Lead 4 (chiff)", "Lead 5 (charang)", "Lead 6 (voice)",
	"Lead 7 (fifths)", "Lead 8 (bass + lead)", "Pad 1 (new age)",
	"Pad 2 (warm)", "Pad 3 (polysynth)", "Pad 4 (choir)", "Pad 5 (bowed)",
	"Pad 6 (metallic)", "Pad 7 (halo)", "Pad 8 (sweep)", "FX 1 (rain)",
	"FX 2 (soundtrack)", "FX 3 (crystal)", "FX 4 (atmosphere)",
	"FX 5 (brightness)", "FX 6 (goblins)", "FX 7 (echoes)",
	"FX 8 (sci-fi)", "Sitar", "Banjo", "Shamisen", "Koto", "Kalimba",
	"Bag pipe", "Fiddle", "Shanai", "Tinkle Bell", "Agogo", "Steel Drums",
	"Woodblock", "Taiko Drum", "Melodic Tom", "Synth Drum",
	"Reverse Cymbal", "Guitar Fret Noise", "Breath Noise", "Seashore",
	"Bird Tweet", "Telephone Ring", "Helicopter", "Applause", "Gunshot",

	# Percussion instruments:
	"Acoustic Bass Drum", "Bass Drum 1", "Side Stick", "Acoustic Snare",
	"Hand Clap", "Electric Snare", "Low Floor Tom", "Closed Hi Hat",
	"High Floor Tom", "Pedal Hi-Hat", "Low Tom", "Open Hi-Hat",
	"Low-Mid Tom", "Hi-Mid Tom", "Crash Cymbal 1", "High Tom",
	"Ride Cymbal 1", "Chinese Cymbal", "Ride Bell", "Tambourine",
	"Splash Cymbal", "Cowbell", "Crash Cymbal 2", "Vibraslap",
	"Ride Cymbal 2", "Hi Bongo", "Low Bongo", "Mute Hi Conga",
	"Open Hi Conga", "Low Conga", "High Timbale", "Low Timbale",
	"High Agogo", "Low Agogo", "Cabasa", "Maracas", "Short Whistle",
	"Long Whistle", "Short Guiro", "Long Guiro", "Claves", "Hi Wood Block",
	"Low Wood Block", "Mute Cuica", "Open Cuica", "Mute Triangle",
	"Open Triangle",
]

# Constants for MIDI notes.
#
# For example:
#    F# in Octave 3:      O3.Fs
#    C# in Octave -2:     On2.Cs
#    D-flat in Octave 1:  O1.Db
#    D in Octave 0:       O0.D
#    E in Octave 2:       O2.E

class Octave:
	def __init__(self, base):
		self.C  = base
		self.Cs = base + 1
		self.Db = base + 1
		self.D  = base + 2
		self.Ds = base + 3
		self.Eb = base + 3
		self.E  = base + 4
		self.F  = base + 5
		self.Fs = base + 6
		self.Gb = base + 6
		self.G  = base + 7
		self.Gs = base + 8
		self.Ab = base + 8
		self.A  = base + 9
		self.As = base + 10
		self.Bb = base + 10
		self.B  = base + 11

On5 = Octave(0)      # Octave -5
On4 = Octave(12)     # Octave -4
On3 = Octave(24)     # Octave -3
On2 = Octave(36)     # Octave -2
On1 = Octave(48)     # Octave -1
O0  = Octave(60)     # Octave 0
O1  = Octave(72)     # Octave 1
O2  = Octave(84)     # Octave 2
O3  = Octave(96)     # Octave 3
O4  = Octave(108)    # Octave 4
O5  = Octave(120)    # Octave 5

# Given a MIDI note number, return a note definition in terms of the
# constants above.

def def_for_note(note):
	OCTAVES = [ "On5", "On4", "On3", "On2", "On1",
	            "O0", "O1", "O2", "O3", "O4", "O5" ]
	NOTES = [ "C", "Cs", "D", "Ds", "E", "F", "Fs",
	          "G", "Gs", "A", "As", "B" ]

	return "%s.%s" % (OCTAVES[note // 12], NOTES[note % 12])

