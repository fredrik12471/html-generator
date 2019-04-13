cd git/http-sandbox/
git pull
git checkout -b newbranch
DATE=$(date +"%Y%m%d%H%M")
#echo 'Updated ' $DATE >> /data/data/com.termux/files/home/git/http-sandbox/index.html
sed -i 's/<h2>Updated [0-9]*/<h2>Updated '$DATE'/g' /data/data/com.termux/files/home/git/http-sandbox/index.html
git add index.html
git commit -m 'Update' -m "'$DATE'"
git push origin newbranch:master
git checkout master
git pull
git branch -D newbranch
 

