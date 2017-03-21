Small script to group and count winners for our annual Readers' Choice awards. Previously this was done by doing a Text Facet and sort by count in Google Refine, then typing related information into a blank spreadsheet.

## Set up

```
>>> mkvirtualenv pandas
(pandas) >>> pip install pandas
```

Get cleaned CSV (without cheaters) and plug in to script. 

Run script.

Clean results. See: "Fisherman" & "Newman" in Best Seafood

## Notes

* This method simply appends to the output file if it exists, so there's the possibility that if you run it multiple times with the same output it will add new data to old data. I should add some checking for that. Maybe recursive test to see if file exists that recurs with a counter for some sort of testout.csv, testout-1.csv, testout-2.csv thing...
* The output of the real data will have a few rows at the bottom re: names, times, etc. that need to be purged before putting up on Drive (BUT HEY, this could be a way to catch cheaters next year!)