# Code for "Prevalence and prevention of large language model use in crowd work"

### `./experiments`

Here we share the HTML + JS files we used to create the human intelligence task.

- `./html_study1.html`: summarization task for study #1. Note that it only works with a url parameter `PROLIFIC_ID`.
- `./html_study2.html`: summarization task for study #2. Note that it only works with a url parameter `PROLIFIC_ID`.
- `./html_survey.html`: post-task survey for study #2.
- `./images_better/`: these are the images used for study #2.

### `./data`

The original data collected by Prolific can be found [here](https://osf.io/rt2xy/). 
in this folder, we share this very data augmented with metrics related to LLM use.

#### `Study-1-augmented.csv.gz`
Rows kept from the original file:
- `original_text`: original summary
- `key_strokes`: Key strokes, separated by spaces. 
- `log_of_what_they_did`: Key strokes. Broken up into [keystroke, timestamp].
- `datetime`: Time when completed.
- `text`: Text summary. 
- `started_at`: When task was started
- `completed_at`: When task was completed.
- `time_taken`: How many seconds it took to complete the task.
- `total_approvals`: Total number of times the workers has had a task approved.
- Demographic-related columns: `age`, `sex`, `ethnicity_simplified`, `country_of_birth`, `Nationality`, `language`, 
`student_status`, `employment_status`.

Rows added:
- `y_cc`: classifier prediction (`real`|`synthetic`).
- `cal_logit`: classifier logits.
- `cal_prob`: classifier probabilities [0,1].
- `copied`: whether the worker copy-pasted, (`0`|`1`).
- `character_pred`: heuristic: contains line-breaks typical of ChatGPT (`real`|`synthetic`).
- `speed_pred`: heuristic: over 400 words per minute reading and 80 wpm writting (`real`|`synthetic`).


#### `Test-set-model.csv.gz`
This is the data from the test set, unseen by the model and used for calibration. 
Contains synthetic summaries and real summaries from the 2019 paper.

- `text`: Text summary.
- `target`: whether the summary is real or synthetic  (`real`|`synthetic`).
- `y_cc`: classifier prediction (`real`|`synthetic`).



### `./analyses`