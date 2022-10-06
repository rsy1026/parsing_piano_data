
# Functions for parsing piano MIDI

Prepare requirements: 

	python3 install -r requirements.txt

Default setting is to split into all measures
    
	python3 main.py /home/user/data /home/user/savedir

To split particular measures: 

	python3 main.py /home/user/data /home/user/savedir <start_measure> <end_measure>

The current code includes several steps:
- Before parsing, perform WAV, score XML, score MIDI, and perform MIDI should be prepared

## Aligning perform WAV to perform MIDI
- When temporally aligning performance audio with performance MIDI
	- Use function: align_wav_midi()
	- Output: midi file("*_aligned.mid")
- Reference: https://github.com/craffel/pretty-midi/blob/master/examples/align_midi.py

## Aligning score MIDI to perform MIDI 
- When matching score MIDI to performance MIDI with Nakamura algorithm 
	- Use function: save_corresp_files() 
	- Output: corresp file("*_corresp.text")
- Reference: https://midialignment.github.io/demo.html (Nakamura et al., 2017)
	
## Aligning score XML to score MIDI 
- When matching note-by-note between score XML and score MIDI 
	- Use function: match_XML_to_scoreMIDI()
	- Output: variable "xml_score_pairs"
- Rule-based	

## Aligning score XML to score MIDI to perform MIDI 
- When note-by-note matching between **xml_score_pairs** and **corresp file**("*_corresp.txt")
	- Use function: match_score_to_performMIDI()
	- Output: variable "xml_score_perform_pairs"

## Spliting perform WAV by measures 
- When spliting wav file according to **xml_score_perform_pairs** 
	- It can split all measures at once 
	- Also, it can split particular range of measures 
	- Use function: split_wav_by_measure()
	- Output: splitted wav file("*.measure*.wav")

## Other things
- incomplete measure is counted as measure number.
 
