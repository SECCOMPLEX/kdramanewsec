if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/SECCOMPLEX/applelkbot.git /applelkbot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /applelkbot
fi
cd /applelkbot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
