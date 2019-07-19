
# Description

This is a Spanish Emotional free recall task (EFRT) developed for a research project
conducted in a collaboration between the neurocognitive laboratory and the
Psychosocial laboratory at Ponce Health Sciences University. This project
compares people with a history of suicidal behavior vs a control
group (no history of suicidal behavior) on this and other tasks.

The EST was developed using Psychopy 3 builder but includes code
components. It can't be run with Psychopy 2 because it uses Unicode
characters (i.e., words with accents) and Psychopy crashes with this sort of
stimuli or doesn't display it correctly. It includes practice and experiment trials.

The Free recall task consists of presenting "lists" of words to the participant
and then asking the participant to recall as many as possible.


## Practice trials

The EFRT includes a single practice trial. The trial consists of a list of 15
words(i.e., name colors) that participants have to remember at the end of
the trial. Words are presented individually on the screen for two seconds each.
The participant must type the words they remember, separated by spaces.


### Practice trial structure

-   instructions
-   fixation cross for 1 sec
-   blank screen for .5 secs
-   each word is presented for 2 seconds
-   participant types all the words he or she remembers


## Experimental trials

A total of 150 words will be presented to the participant. The words are from three
different valence: positive, negative, and neutral. Just as in the practice trials,
words are presented individually on the screen for two seconds each and the
participant must type the words that he or she remembers, separated by spaces.

Participants are allowed 3 breaks to rest (one rest after completing every 3
blocks. The participant continues by pressing a key.


### Experiment trial structure

-   instructions
-   fixation cross for 1 sec
-   blank screen for .5 secs
-   each word is presented for 2 seconds
-   participant types all the words he or she remembers


### Technical details about blocks

-   Words are organized into blocks (lists) to get semi-randomization:
    -   10 lists
    -   Each list has 15 words: 5 words from each valence

The following table represents one block:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-right" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">text</th>
<th scope="col" class="org-left">condition</th>
<th scope="col" class="org-right">list</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">negative1</td>
<td class="org-left">negative</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">negative2</td>
<td class="org-left">negative</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">negative3</td>
<td class="org-left">negative</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">negative4</td>
<td class="org-left">negative</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">negative5</td>
<td class="org-left">negative</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">neutral1</td>
<td class="org-left">neutral</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">neutral2</td>
<td class="org-left">neutral</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">neutral3</td>
<td class="org-left">neutral</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">neutral4</td>
<td class="org-left">neutral</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">neutral5</td>
<td class="org-left">neutral</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">positive1</td>
<td class="org-left">positive</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">positive2</td>
<td class="org-left">positive</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">positive3</td>
<td class="org-left">positive</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">positive4</td>
<td class="org-left">positive</td>
<td class="org-right">1</td>
</tr>


<tr>
<td class="org-left">positive5</td>
<td class="org-left">positive</td>
<td class="org-right">1</td>
</tr>
</tbody>
</table>


## Contact

If you have any questions don't hesitate to conctact me at [mbermonti@psm.edu](mailto:mbermonti@psm.edu).
If you find any errors or bugs, please open an issue and I'll work on it
as soon as possible.
