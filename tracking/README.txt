Tracking files
----------------
master-tracker.csv     All tasks (258+). Columns: Owner, Status, Due_Date, Evidence_Link, Notes — fill as you execute.
by-brand\*.csv         Same rows filtered by Brand (plus all.csv for Brand=ALL).

Regenerate from checklist definition (overwrites CSVs):
  py C:\Users\DELL\daily-group-pre-launch\tracking\build_tracker.py

Edit the task list in: build_tracker.py (ROWS / add() calls), then re-run.

If you already filled Status in Excel, export a backup before regenerating — the script resets Owner to TBD and Status to TODO.
