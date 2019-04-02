Welcome to the Theunissen lab data directory.  This readme file was written February 15, 2008.

****************************

         CONTENTS:

1) Text description of the data

2) Getting started guide with sample MATLAB code


****************************

1) Text description of the data

We have provided single-unit auditory recordings from two areas in male zebra finches.  The data are organized first by brain area, then by neuron name, then by stimulus.  The neuron name directories follow the schema birdname "_" cell_id, where cell_id is the n-th cell recorded from, usually (but not always) followed by the letter designation of the rig used to record; so 4_A and 4_B were recorded simultaneously (probably in two different brain areas).  Inside these directories are two stimulus types: conspecific song ("conspecific") and modulation-limited noise ("flatrip").  Modulation limited noise is white noise (band-passed between 250Hz and 8 kHz in this case) that has been filtered in the modulation spectrum to limit fast spectral and temporal modulations.  Modulation-limited noise has also been called Ripple noise.

The root directory has a special stimulus directory: "all_stims", which has every auditory stimulus in full, with a name equal to the md5 hash of the auditory file.  All other references to these stims are pointers to these raw stimulus files.  If we were to have included a full .wav file in each neuron's directory, the data would become excessively large.  We decided to not use a system of pointer files (a.k.a. "shortcuts," a.k.a. "aliases") in each stimulus directory because not all file systems (like the ones used on CDs) support them.  Instead, alongside files of spike times we use text files with the md5 hashes of the stimulus they replace.  The stim1, stim2, etc. files in "all_cells," "sure_L," and other directories are plain text files, and contain just the stimulus name.  So, if a conspecific stim file (like "Field_L_cells/gg0304_10_B/conspecific/stim6") has the text "DB500570216F0412EE8D9F7D64F38232.wav" it means the corresponding wav file is in all_stims/conspecific/DB500570216F0412EE8D9F7D64F38232.wav.  Note than each stim file has a line break character at the end of it which should not be treated as part of the stim name, since the file "all_stims/conspecific/DB500570216F0412EE8D9F7D64F38232.wav***EOL***" does not exist.

All .wav files here had a sampling rate of 32000 Hz and a sampling depth of 16 bits.  

Spike files are plain text files with spike arival times in milliseconds relative to the stimulus onset.  Negative spike times are pre-onset spikes, and spike times later than the stimulus duration are permitted.

More details about bird rearing conditions and experimental methods can be found in the accompanying file "Detailed Methods.txt".  Please contact Frederic Theunissen (theunissen@berkeley.edu) if you have any further questions.


****************************

2) Getting started guide with sample MATLAB code


To get the spike times, do the following.  Navigate to a directory where there are stim files (like "Field_L_cells/gg0304_10_B/conspecific" for example).  Next, read the plain-text spike arrival times file:

>> fid = fopen('spike1','r');
>> spike_times_stim_1 = char(fread(fid,'char')');
>> fclose(fid);

The variable "spike_times_stim_1" should now look like this:

spike_times_stim_1 =
-464.938 159.375 837.125 960.343 1271.781 1285.843 1475.437 1516.593 1567.625 1639.687 1643.875 1978.093 2072.125 2109.125 2278.718 2759.125 3742.812
-1898.157 -474.125 428.281 705.500 995.468 1676.281 1976.187 1977.093 2184.312 2649.375 3251.843
-1574.813 -1446.250 154.656 581.406 761.250 1126.281 1511.875 1845.562 1871.437 2172.093 2223.718 2362.343 3110.937 3191.968
-1690.094 105.750 390.218 1233.093 1475.968 2175.218 2538.625
-1311.907 370.218 567.000 961.406 2074.750 2235.875
-475.188 710.187 1522.000 1840.562 1869.937 2265.218
-1981.250 -1343.532 669.718 1230.750 1523.125 1674.687 2213.937 2707.031
469.406 919.812 1678.437 3010.187 3770.218
636.875 841.125 1634.343 1963.031 1977.312 2211.125 3392.937
1705.500 1967.843 2222.250
These are the recorded spike arrival times (in ms) relative to stimulus onset.  Spikes up to 2000 ms before the stimulus onset will be included with these data.  Successive spikes are separated with a space, while trials are terminated with a line break character ASCII 10.  

To read the corresponding stimulus in MATLAB, use the following:

>> fid = fopen('stim1','r');
>> stim_name = char(fread(fid,'char')');
>> fclose(fid);
>> stim_wav = wavread(['../../../all_stims/conspecific/' stim_name(1:(end-1))]);
In the first line we chose "stim1" because stimXXX is the stimulus played when we recorded spikeXXX.

"stim_wav" is now a T x 1 vector of the sound pressure amplitude where T is the number of sound samples.  Since our sampling rate was 32000 Hz, divide T by 32 to get the duration of the stimulus in ms.

