
import os
import mido

# Define your directories here
INPUT_DIR = '/Users/cameronholt/Documents/git_repos/filtered_pokemon/black_white_unfiltered'
OUTPUT_DIR = '/Users/cameronholt/Documents/git_repos/filtered_pokemon/black_white_filtered'

def filter_midi_file(input_file, output_file):
    # Load the MIDI file
    midi = mido.MidiFile(input_file)
    # Create a new MIDI file with the same ticks per beat
    filtered_midi = mido.MidiFile(ticks_per_beat=midi.ticks_per_beat)
    
    # Process each track in the original MIDI file
    for track in midi.tracks:
        new_track = mido.MidiTrack()
        for msg in track:
            # Check if the message has a channel attribute and if it's on the percussion channel (channel 10, index 9)
            if hasattr(msg, 'channel') and msg.channel == 9:
                continue  # Skip percussion messages
            new_track.append(msg)
        filtered_midi.tracks.append(new_track)
    
    # Save the filtered MIDI file to the output path
    filtered_midi.save(output_file)
    print(f"Filtered MIDI file saved to {output_file}")
    return midi.length

def main():
    total_length = 0.0  # Total length in seconds

    # Create the output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # Iterate over all MIDI files in the input directory
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.mid', '.midi')):
            input_file = os.path.join(INPUT_DIR, filename)
            output_file = os.path.join(OUTPUT_DIR, filename)
            # Filter the file and accumulate its length
            file_length = filter_midi_file(input_file, output_file)
            total_length += file_length

    # Output the total length processed (in seconds)
    print(f"\nTotal length of MIDI processed: {total_length:.2f} seconds")

if __name__ == "__main__":
    main()
