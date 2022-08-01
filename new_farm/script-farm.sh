#if the test in actions work run the sh file this file copys new main file over current file

cd $GITHUB_WORKSPACE
mkdir vogel
cd ..
cp /my-project/new_farm/main.py home/farm
systemctl restart farm
