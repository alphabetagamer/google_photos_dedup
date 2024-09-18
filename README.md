# google_photos_dedup
A python Script bundled with a JS tamper monkey script for removing duplicate google photos media.

# Steps to use ( may god have mercy if you reach this stage )

1. Create a test app in both the google accounts through developer portal
2. Activate Google Photos API for the accounts.
3. Generate Google Photos API credentials.
4. Run get_photos.py with the credentials.
5. Repeat for second account.
6. Run check_dupes.py and pure_list.py.
7. Open chrome, log into the account you want to delete the dupes from.
8. Install Tampermonkey and enable development mode in chrome ( else the script does not work )
9. Add google_photos_delete as a script to tm and paste the list of photos to delete to the script.
10. open google.photos and wait for the script to finish execution.
