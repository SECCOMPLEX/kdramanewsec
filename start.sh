if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/SECCOMPLEX/hbolkbot.git /hbolkbot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /hbolkbot
fi
cd /hbolkbot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
