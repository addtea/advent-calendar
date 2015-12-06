#!/usr/bin/zsh

SECRET_KEY="yzbqklnj"
milestone=10
i=1

echo "Start time: `date`"
while true; do
  if [ $i -eq $milestone ]; then
    echo "Reached: $i at `date`"
    milestone=$((milestone*10))
  fi

  str=""$SECRET_KEY"$i";
  echo -n $str | md5sum | grep -e "^000000.*"
  if [ $? -eq 0 ]; then
    echo "Found solution!"
    echo "$str at `date`"
    exit 0
  fi 
  i=$((i+1))
done
