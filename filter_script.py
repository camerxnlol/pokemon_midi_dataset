
import os
import mido

INPUT_DIR = '/Users/cameronholt/Documents/git_repos/filtered_pokemon/black_white_unfiltered'
OUTPUT_DIR = '/Users/cameronholt/Documents/git_repos/filtered_pokemon/black_white_filtered'

def filter_midi_file(input_file, output_file):
    midi = mido.MidiFile(input_file)
    filtered_midi = mido.MidiFile(ticks_per_beat=midi.ticks_per_beat)
    
    # process each track in the original midi file
    for track in midi.tracks:
        new_track = mido.MidiTrack()
        for msg in track:
            # check if the message has a channel attribute and if it's on the percussion channel (channel 10, index 9)
            if hasattr(msg, 'channel') and msg.channel == 9:
                continue  # skip percussion messages
            new_track.append(msg)
        filtered_midi.tracks.append(new_track)
    
    # save the filtered midi file to the output path
    filtered_midi.save(output_file)
    print(f"Filtered MIDI file saved to {output_file}")
    return midi.length

def main():
    total_length = 0.0

    # create the output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # iterate over all midi files in the input directory
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.mid', '.midi')):
            input_file = os.path.join(INPUT_DIR, filename)
            output_file = os.path.join(OUTPUT_DIR, filename)
            # filter the file and accumulate its length
            file_length = filter_midi_file(input_file, output_file)
            total_length += file_length

    # output the total length processed (seconds)
    print(f"\nTotal length of MIDI processed: {total_length:.2f} seconds")

if __name__ == "__main__":
    main()
