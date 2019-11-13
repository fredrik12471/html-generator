cd ../../git/http-sandbox/
#cd ..\\..\\git\\http-sandbox\\
git pull
git checkout -b newbranch
DATE=$(date +"%Y%m%d%H%M")
#echo 'Updated ' $DATE >> /data/data/com.termux/files/home/git/http-sandbox/index.html
#sed -i 's/<h2>Updated [0-9]*/<h2>Updated '$DATE'/g' /data/data/com.termux/files/home/git/http-sandbox/index.html
python /data/data/com.termux/files/home/git/html-generator/start.py
echo "$(tail -50 /data/data/com.termux/files/home/git/http-sandbox/twitter/aikfotboll/unfollowers.txt)" > /data/data/com.termux/files/home/git/http-sandbox/twitter/aikfotboll/unfollowers.txt
#python C:\\Users\\Fredrik\\git\\html-generator\\start.py
git add --all
git commit -m 'Update' -m "'$DATE'"
git push origin newbranch:master
git checkout master
git pull
git branch -D newbranch
 

