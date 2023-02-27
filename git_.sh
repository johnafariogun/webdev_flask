read -p "please input a commit message  
" m
if [ "$m" = "no" ];
    then 
        echo "Remember that you have to stay commited and keep your repo up to date"
else
    git add .
    git commit -m "$m"
    git push
fi